# decaf2many: Java to Python Transpiler

[![image](https://img.shields.io/pypi/v/decaf2many.svg)](https://pypi.python.org/pypi/decaf2many)
[![image](https://img.shields.io/travis/adsharma/decaf2many.svg)](https://travis-ci.com/adsharma/decaf2many)

## Overview

Transpiles Java8 to the [py2many](http://github.com/adsharma/py2many) dialect of python. Doing so preserves
some information about types (char, int, long map to u16, i32, i64 respectively) and can be further transpiled
to downstream languages supported by py2many, which include Kotlin and Rust among others.

This dialect can be thought of as a statically typed subset of python that's suitable as a universal
intermediate language. It can also benefit from the rich set of tools and libraries that make up the python ecosystem.

If you're looking to use dynamic typing, this is probably not a good path for you.

## Details

The tool is based on [antlr4](https://github.com/antlr/antlr4) and the "optimized"
[Java grammar](https://github.com/antlr/grammars-v4/tree/master/java/java)

## Usage

```
cat HelloWorld.java | decaf2many  # writes to stdout
decaf2many HelloWorld.java  # writes to HelloWorld.py
decaf2many --outdir /tmp HelloWorld.java  # writes /tmp/HelloWorld.py
```

To transpile to other languages

```
py2many --rust=1 HelloWorld.py
py2many --kotlin=1 HelloWorld.py
```

## Sample programs

* HelloWorld: [input](https://github.com/adsharma/decaf2many/blob/main/tests/cases/HelloWorld.java) [output](https://github.com/adsharma/decaf2many/blob/main/tests/expected/HelloWorld.py)
* Expression: [input](https://github.com/adsharma/decaf2many/blob/main/tests/cases/Expression.java) [output](https://github.com/adsharma/decaf2many/blob/main/tests/expected/Expression.py)
