"""PyDoctor's test suite."""

from __future__ import print_function
import sys
import pytest

py3only = pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python 3")
typecomment = pytest.mark.skipif(sys.version_info < (3, 8), reason="requires python 3.8")
