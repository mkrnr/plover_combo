#!/usr/bin/env python3

from setuptools import setup

from plover_build_utils.setup import BuildUi, Develop

Develop.build_dependencies.append('build_py')
CMDCLASS = {
    'build_ui': BuildUi,
    'develop': Develop,
}

setup(cmdclass=CMDCLASS)
