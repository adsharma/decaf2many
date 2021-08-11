"""Main module."""

from .lang.JavaParserVisitor import JavaParserVisitor


class Transpiler(JavaParserVisitor):
    def visitCompilationUnit(self, ctx):
        print("Got here")
