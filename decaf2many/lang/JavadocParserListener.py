# Generated from JavadocParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JavadocParser import JavadocParser
else:
    from JavadocParser import JavadocParser

# This class defines a complete listener for a parse tree produced by JavadocParser.
class JavadocParserListener(ParseTreeListener):

    # Enter a parse tree produced by JavadocParser#documentation.
    def enterDocumentation(self, ctx:JavadocParser.DocumentationContext):
        pass

    # Exit a parse tree produced by JavadocParser#documentation.
    def exitDocumentation(self, ctx:JavadocParser.DocumentationContext):
        pass


    # Enter a parse tree produced by JavadocParser#documentationContent.
    def enterDocumentationContent(self, ctx:JavadocParser.DocumentationContentContext):
        pass

    # Exit a parse tree produced by JavadocParser#documentationContent.
    def exitDocumentationContent(self, ctx:JavadocParser.DocumentationContentContext):
        pass


    # Enter a parse tree produced by JavadocParser#skipWhitespace.
    def enterSkipWhitespace(self, ctx:JavadocParser.SkipWhitespaceContext):
        pass

    # Exit a parse tree produced by JavadocParser#skipWhitespace.
    def exitSkipWhitespace(self, ctx:JavadocParser.SkipWhitespaceContext):
        pass


    # Enter a parse tree produced by JavadocParser#description.
    def enterDescription(self, ctx:JavadocParser.DescriptionContext):
        pass

    # Exit a parse tree produced by JavadocParser#description.
    def exitDescription(self, ctx:JavadocParser.DescriptionContext):
        pass


    # Enter a parse tree produced by JavadocParser#descriptionLine.
    def enterDescriptionLine(self, ctx:JavadocParser.DescriptionLineContext):
        pass

    # Exit a parse tree produced by JavadocParser#descriptionLine.
    def exitDescriptionLine(self, ctx:JavadocParser.DescriptionLineContext):
        pass


    # Enter a parse tree produced by JavadocParser#descriptionLineStart.
    def enterDescriptionLineStart(self, ctx:JavadocParser.DescriptionLineStartContext):
        pass

    # Exit a parse tree produced by JavadocParser#descriptionLineStart.
    def exitDescriptionLineStart(self, ctx:JavadocParser.DescriptionLineStartContext):
        pass


    # Enter a parse tree produced by JavadocParser#descriptionLineNoSpaceNoAt.
    def enterDescriptionLineNoSpaceNoAt(self, ctx:JavadocParser.DescriptionLineNoSpaceNoAtContext):
        pass

    # Exit a parse tree produced by JavadocParser#descriptionLineNoSpaceNoAt.
    def exitDescriptionLineNoSpaceNoAt(self, ctx:JavadocParser.DescriptionLineNoSpaceNoAtContext):
        pass


    # Enter a parse tree produced by JavadocParser#descriptionLineElement.
    def enterDescriptionLineElement(self, ctx:JavadocParser.DescriptionLineElementContext):
        pass

    # Exit a parse tree produced by JavadocParser#descriptionLineElement.
    def exitDescriptionLineElement(self, ctx:JavadocParser.DescriptionLineElementContext):
        pass


    # Enter a parse tree produced by JavadocParser#descriptionLineText.
    def enterDescriptionLineText(self, ctx:JavadocParser.DescriptionLineTextContext):
        pass

    # Exit a parse tree produced by JavadocParser#descriptionLineText.
    def exitDescriptionLineText(self, ctx:JavadocParser.DescriptionLineTextContext):
        pass


    # Enter a parse tree produced by JavadocParser#descriptionNewline.
    def enterDescriptionNewline(self, ctx:JavadocParser.DescriptionNewlineContext):
        pass

    # Exit a parse tree produced by JavadocParser#descriptionNewline.
    def exitDescriptionNewline(self, ctx:JavadocParser.DescriptionNewlineContext):
        pass


    # Enter a parse tree produced by JavadocParser#tagSection.
    def enterTagSection(self, ctx:JavadocParser.TagSectionContext):
        pass

    # Exit a parse tree produced by JavadocParser#tagSection.
    def exitTagSection(self, ctx:JavadocParser.TagSectionContext):
        pass


    # Enter a parse tree produced by JavadocParser#blockTag.
    def enterBlockTag(self, ctx:JavadocParser.BlockTagContext):
        pass

    # Exit a parse tree produced by JavadocParser#blockTag.
    def exitBlockTag(self, ctx:JavadocParser.BlockTagContext):
        pass


    # Enter a parse tree produced by JavadocParser#blockTagName.
    def enterBlockTagName(self, ctx:JavadocParser.BlockTagNameContext):
        pass

    # Exit a parse tree produced by JavadocParser#blockTagName.
    def exitBlockTagName(self, ctx:JavadocParser.BlockTagNameContext):
        pass


    # Enter a parse tree produced by JavadocParser#blockTagContent.
    def enterBlockTagContent(self, ctx:JavadocParser.BlockTagContentContext):
        pass

    # Exit a parse tree produced by JavadocParser#blockTagContent.
    def exitBlockTagContent(self, ctx:JavadocParser.BlockTagContentContext):
        pass


    # Enter a parse tree produced by JavadocParser#blockTagText.
    def enterBlockTagText(self, ctx:JavadocParser.BlockTagTextContext):
        pass

    # Exit a parse tree produced by JavadocParser#blockTagText.
    def exitBlockTagText(self, ctx:JavadocParser.BlockTagTextContext):
        pass


    # Enter a parse tree produced by JavadocParser#blockTagTextElement.
    def enterBlockTagTextElement(self, ctx:JavadocParser.BlockTagTextElementContext):
        pass

    # Exit a parse tree produced by JavadocParser#blockTagTextElement.
    def exitBlockTagTextElement(self, ctx:JavadocParser.BlockTagTextElementContext):
        pass


    # Enter a parse tree produced by JavadocParser#inlineTag.
    def enterInlineTag(self, ctx:JavadocParser.InlineTagContext):
        pass

    # Exit a parse tree produced by JavadocParser#inlineTag.
    def exitInlineTag(self, ctx:JavadocParser.InlineTagContext):
        pass


    # Enter a parse tree produced by JavadocParser#inlineTagName.
    def enterInlineTagName(self, ctx:JavadocParser.InlineTagNameContext):
        pass

    # Exit a parse tree produced by JavadocParser#inlineTagName.
    def exitInlineTagName(self, ctx:JavadocParser.InlineTagNameContext):
        pass


    # Enter a parse tree produced by JavadocParser#inlineTagContent.
    def enterInlineTagContent(self, ctx:JavadocParser.InlineTagContentContext):
        pass

    # Exit a parse tree produced by JavadocParser#inlineTagContent.
    def exitInlineTagContent(self, ctx:JavadocParser.InlineTagContentContext):
        pass


    # Enter a parse tree produced by JavadocParser#braceExpression.
    def enterBraceExpression(self, ctx:JavadocParser.BraceExpressionContext):
        pass

    # Exit a parse tree produced by JavadocParser#braceExpression.
    def exitBraceExpression(self, ctx:JavadocParser.BraceExpressionContext):
        pass


    # Enter a parse tree produced by JavadocParser#braceContent.
    def enterBraceContent(self, ctx:JavadocParser.BraceContentContext):
        pass

    # Exit a parse tree produced by JavadocParser#braceContent.
    def exitBraceContent(self, ctx:JavadocParser.BraceContentContext):
        pass


    # Enter a parse tree produced by JavadocParser#braceText.
    def enterBraceText(self, ctx:JavadocParser.BraceTextContext):
        pass

    # Exit a parse tree produced by JavadocParser#braceText.
    def exitBraceText(self, ctx:JavadocParser.BraceTextContext):
        pass


