"""Main module."""

from .lang.JavaParserListener import JavaParserListener


class Transpiler(JavaParserListener):
    def enterCompilationUnit(self, ctx):
        print("Got here")
