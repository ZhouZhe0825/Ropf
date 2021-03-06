from setuptools import find_packages
from distutils.core import setup
from setuptools.command.test import test as TestCommand
import sys
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from distutils.extension import Extension

powerflow = Extension("ropf.powerflow", ["ropf/powerflow.pyx"], extra_compile_args=['/EHsc'])

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='Ropf',
    version='0.1',
    packages=find_packages(),
    tests_require=['pytest'],
    cmdclass={'test': PyTest, 'build_ext': build_ext},
    url='',
    license='',
    include_package_data=True,
    author='Yassine Abdelouadoud',
    author_email='yassine.abdelouadoud@gmail.com',
    description='Optimal Power Flow in Radial Networks',
    install_requires=["numpy", "cvxpy", "Cython"],
    ext_modules=cythonize(powerflow)
    )

