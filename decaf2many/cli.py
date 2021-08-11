"""Console script for decaf2many."""
import argparse
import sys


from antlr4 import *
from .lang.JavaLexer import JavaLexer
from .lang.JavaListener import JavaListener
from .lang.JavaParser import JavaParser

class JavaPrintListener(JavaListener):
    def enterCompilationUnit(self, ctx):
        print("Got here")

def run_one():
    lexer = JavaLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()
    printer = JavaPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


def main(args):
    """Console script for decaf2many."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args, rest = parser.parse_known_args(args=args)

    return run_one(rest[0])


if __name__ == "__main__":
    sys.exit(main(sys.args))  # pragma: no cover
