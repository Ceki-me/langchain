"""Namespace alias — the real package is ``langchain-ceki``.

``ceki-langchain`` exists so the ``ceki`` org owns the alias on PyPI.
Every public name re-exported here lives in ``langchain_ceki``; install
either distribution and you get the same symbols.
"""
from langchain_ceki import *  # noqa: F401,F403
from langchain_ceki import __version__  # noqa: F401
