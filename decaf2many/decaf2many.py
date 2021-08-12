"""Main module."""

import textwrap
from typing import DefaultDict
from .lang.JavaParserVisitor import JavaParserVisitor
from .lang.JavaParser import JavaParser


class Transpiler(JavaParserVisitor):
    DISPATCH_MAP = {"println": "print"}
    INDENT = " " * 4
    TYPE_MAP = {
        "String": "str",
        "Integer": "i32",
        "int": "i32",
        "Boolean": "bool",
        "boolean": "bool",
        "Double": "float",
        "double": "float",
        "char": "u16",
        "Long": "u64",
        "long": "u64",
    }
    BINARY_OPS = {
        JavaParser.ADD,
        JavaParser.SUB,
        JavaParser.MUL,
        JavaParser.DIV,
        JavaParser.MOD,

        JavaParser.BITAND,
        JavaParser.BITOR,
        JavaParser.CARET,

        JavaParser.GT,
        JavaParser.LT,
        JavaParser.GE,
        JavaParser.LE,
        JavaParser.EQUAL,
        JavaParser.NOTEQUAL,
        JavaParser.AND,
        JavaParser.OR,
    }

    def __init__(self) -> None:
        super().__init__()

    def indent(self, text):
        return textwrap.indent(text, self.INDENT)

    def defaultResult(self):
        return ""

    def aggregateResult(self, aggregate, nextResult):
        return aggregate + nextResult

    def _dispatch(self, fname):
        if fname in self.DISPATCH_MAP:
            return self.DISPATCH_MAP[fname]
        return fname

    def visitComment(self, comment, parser):
        if comment.type == parser.LINE_COMMENT:
            return comment.text.replace("//", "#")
        return comment.text

    def visitComments(self, ctx):
        pos = ctx.getSourceInterval()[0]
        comments = ctx.parser.getTokenStream().getHiddenTokensToLeft(pos)
        comments_str = [self.visitComment(c, ctx.parser) for c in comments]
        return "\n".join(comments_str)

    def visitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        c  = self.visitComments(ctx)
        return c + "\n".join([self.visit(t) for t in ctx.typeDeclaration()]) + "\n"

    def visitClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext):
        name = ctx.IDENTIFIER().getText()
        body = self.visit(ctx.classBody())
        body = self.indent(body)
        return textwrap.dedent(
            f"""\
            class {name}:
        """) + body

    def getDecorator(self, m: str) -> str:
        if m == "static":
            return "@staticmethod"
        return ""

    def visitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        fname = ctx.IDENTIFIER().getText()
        body = self.visit(ctx.methodBody())
        params = self.visit(ctx.formalParameters())
        body = self.indent(body)
        modifiers = "\n".join([self.getDecorator(m) for m in ctx.parentCtx.parentCtx.modifiers])
        return modifiers + "\n" + textwrap.dedent(
            f"""\
            def {fname}({params}):
        """) + body + "\n"

    def visitClassBodyDeclaration(self, ctx: JavaParser.ClassBodyDeclarationContext):
        ctx.modifiers = []
        return super().visitClassBodyDeclaration(ctx)

    def visitClassOrInterfaceModifier(self, ctx: JavaParser.ClassOrInterfaceModifierContext):
        ctx.parentCtx.parentCtx.modifiers.append(ctx.getText())
        return super().visitClassOrInterfaceModifier(ctx)

    def visitMethodCall(self, ctx: JavaParser.MethodCallContext):
        fname = ctx.IDENTIFIER().getText()
        fname = self._dispatch(fname)
        args = ctx.expressionList()
        args = [args.expression(i) for i in range(args.getChildCount())]
        args_str = ",".join([self.visit(a) for a in args])
        return f"{fname}({args_str})"

    def visitLiteral(self, ctx: JavaParser.LiteralContext):
        if ctx.STRING_LITERAL:
            return ctx.getText()
        # Possibly other transformations go here
        return ctx.getText()

    def visitFormalParameterList(self, ctx: JavaParser.FormalParameterListContext):
        params = [ctx.formalParameter(i) for i in range(ctx.getChildCount())]
        return ", ".join([self.visit(a) for a in params if a is not None])

    def visitFormalParameter(self, ctx: JavaParser.FormalParameterContext):
        name = self.visit(ctx.variableDeclaratorId())
        ptype = self.visit(ctx.typeType())
        return f"{name}: {ptype}"

    def visitVariableDeclaratorId(self, ctx: JavaParser.VariableDeclaratorIdContext):
        return ctx.getText()

    def visitClassOrInterfaceType(self, ctx: JavaParser.ClassOrInterfaceTypeContext):
        java_type = ctx.getText()
        return self.TYPE_MAP[java_type]

    def visitPrimitiveType(self, ctx: JavaParser.PrimitiveTypeContext):
        java_type = ctx.getText()
        return self.TYPE_MAP[java_type]

    def visitTypeType(self, ctx: JavaParser.TypeTypeContext):
        base = "UnknownType"
        if ctx.classOrInterfaceType():
            base = self.visit(ctx.classOrInterfaceType())
        elif ctx.primitiveType():
            base = self.visit(ctx.primitiveType())
        if len(ctx.LBRACK()):
            return f"List[{base}]"
        return base

    def visitPrimary(self, ctx: JavaParser.PrimaryContext):
        return ctx.getText()

    def visitExpression(self, ctx: JavaParser.ExpressionContext):
        if ctx.bop and ctx.bop.type in self.BINARY_OPS:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return f"{left} {ctx.bop.text} {right}"
        return super().visitExpression(ctx)

    def visitStatement(self, ctx: JavaParser.StatementContext):
        if ctx.RETURN():
            value = self.visit(ctx.expression(0))
            return f"return {value}"
        return super().visitStatement(ctx)