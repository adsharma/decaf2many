# Generated from JavadocParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JavadocParser import JavadocParser
else:
    from JavadocParser import JavadocParser

# This class defines a complete generic visitor for a parse tree produced by JavadocParser.

class JavadocParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JavadocParser#documentation.
    def visitDocumentation(self, ctx:JavadocParser.DocumentationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#documentationContent.
    def visitDocumentationContent(self, ctx:JavadocParser.DocumentationContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#skipWhitespace.
    def visitSkipWhitespace(self, ctx:JavadocParser.SkipWhitespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#description.
    def visitDescription(self, ctx:JavadocParser.DescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#descriptionLine.
    def visitDescriptionLine(self, ctx:JavadocParser.DescriptionLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#descriptionLineStart.
    def visitDescriptionLineStart(self, ctx:JavadocParser.DescriptionLineStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#descriptionLineNoSpaceNoAt.
    def visitDescriptionLineNoSpaceNoAt(self, ctx:JavadocParser.DescriptionLineNoSpaceNoAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#descriptionLineElement.
    def visitDescriptionLineElement(self, ctx:JavadocParser.DescriptionLineElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#descriptionLineText.
    def visitDescriptionLineText(self, ctx:JavadocParser.DescriptionLineTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#descriptionNewline.
    def visitDescriptionNewline(self, ctx:JavadocParser.DescriptionNewlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#tagSection.
    def visitTagSection(self, ctx:JavadocParser.TagSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#blockTag.
    def visitBlockTag(self, ctx:JavadocParser.BlockTagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#blockTagName.
    def visitBlockTagName(self, ctx:JavadocParser.BlockTagNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#blockTagContent.
    def visitBlockTagContent(self, ctx:JavadocParser.BlockTagContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#blockTagText.
    def visitBlockTagText(self, ctx:JavadocParser.BlockTagTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#blockTagTextElement.
    def visitBlockTagTextElement(self, ctx:JavadocParser.BlockTagTextElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#inlineTag.
    def visitInlineTag(self, ctx:JavadocParser.InlineTagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#inlineTagName.
    def visitInlineTagName(self, ctx:JavadocParser.InlineTagNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#inlineTagContent.
    def visitInlineTagContent(self, ctx:JavadocParser.InlineTagContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#braceExpression.
    def visitBraceExpression(self, ctx:JavadocParser.BraceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#braceContent.
    def visitBraceContent(self, ctx:JavadocParser.BraceContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavadocParser#braceText.
    def visitBraceText(self, ctx:JavadocParser.BraceTextContext):
        return self.visitChildren(ctx)



del JavadocParser