"""Console script for decaf2many."""
import argparse
import sys

from antlr4 import CommonTokenStream, FileStream
from antlr4.tree.Trees import Trees

from .decaf2many import Transpiler
from .lang.JavaLexer import JavaLexer
from .lang.JavaParser import JavaParser


def run_one(args, filename):
    lexer = JavaLexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()
    if args.dump:
        print(Trees.toStringTree(tree, None, parser))
        return
    tx = Transpiler()
    out = tx.visit(tree)
    print(out)
    return


def main(args=None):
    """Console script for decaf2many."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--dump", default=False, action="store_true", help="dump ast instead of transpiling")
    args, rest = parser.parse_known_args(args=args)

    return run_one(args, rest[0])
