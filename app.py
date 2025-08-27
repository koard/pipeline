#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minimal hello script for Jenkins pipeline testing.

Usage:
  python3 hello.py
  NAME=Jenkins python3 hello.py
"""
import os
import sys

def greet(name: str = "world") -> str:
    return f"Hello, {name}!"

def main() -> int:
    name = os.environ.get("NAME", "world")
    print(greet(name))
    return 0

if __name__ == "__main__":
    sys.exit(main())
