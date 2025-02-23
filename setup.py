#!/usr/bin/env python3

from setuptools import setup
import sys

from plover_build_utils.setup import BuildPy, BuildUi, Develop

try:
    import plover
    assert plover.__version__ >= "5.0.0"
except (ImportError, AssertionError):
    sys.stderr.write("Error: plover>=5.0.0 is required but not installed.\n")
    sys.exit(1)

BuildPy.build_dependencies.append('build_ui')
BuildUi.hooks = ['plover_build_utils.pyqt:fix_icons']
Develop.build_dependencies.append('build_py')
CMDCLASS = {
    'build_py': BuildPy,
    'build_ui': BuildUi,
    'develop': Develop,
}

setup(cmdclass=CMDCLASS)
