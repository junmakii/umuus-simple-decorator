
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def run_tests(self):
        import sys
        import shlex
        import pytest
        errno = pytest.main(['--doctest-modules'])
        if errno != 0:
            raise Exception('An error occured during installution.')
        install.run(self)


setup(
    packages=setuptools.find_packages('.'),
    version='0.1',
    url='https://github.com/junmakii/umuus-simple-decorator',
    author='Jun Makii',
    author_email='junmakii@gmail.com',
    keywords=[],
    license='GPLv3',
    scripts=[],
    install_requires=[],
    dependency_links=[],
    classifiers=[],
    entry_points={},
    project_urls={},
    setup_requires=[],
    test_suite='umuus_simple_decorator',
    tests_require=[],
    extras_require={},
    package_data={},
    python_requires='',
    include_package_data=True,
    zip_safe=True,
    name='umuus-simple-decorator',
    description="A decorator for Python's class.",
    long_description=("A decorator for Python's class.\n"
 '\n'
 '\n'
 'umuus-simple-decorator\n'
 '=====================\n'
 '\n'
 'Installation\n'
 '------------\n'
 '\n'
 '    $ pip install '
 'git+https://github.com/junmakii/umuus-simple-decorator.git\n'
 '\n'
 '----\n'
 '\n'
 '    >>> import umuus_simple_decorator\n'
 '\n'
 '    >>> import attr\n'
 '\n'
 '    >>> @attr.s()\n'
 '    ... class A(object):\n'
 '    ...     x = attr.ib()\n'
 '    ...     y = attr.ib()\n'
 '\n'
 '    >>> @umuus_simple_decorator.decorator()\n'
 '    ... def f(a: A, i: int):\n'
 '    ...     a.x += i\n'
 '    ...     return a\n'
 '\n'
 '    >>> a = A(x=1, y=1)\n'
 '    >>> [f(a, i) for i in range(3)]\n'
 '    [A(x=4, y=1), A(x=4, y=1), A(x=4, y=1)]\n'
 '\n'
 '    >>> @umuus_simple_decorator.decorator(copy_data=True)\n'
 '    ... def f(a: A, i: int):\n'
 '    ...     a.x += i\n'
 '    ...     return a\n'
 '\n'
 '    >>> a = A(x=1, y=1)\n'
 '    >>> [f(a, i) for i in range(3)]\n'
 '    [A(x=1, y=1), A(x=2, y=1), A(x=3, y=1)]\n'
 '\n'
 '----\n'
 '\n'
 '    >>> import addict\n'
 '\n'
 '    >>> @umuus_simple_decorator.decorator()\n'
 '    ... def f(a: addict.Dict):\n'
 '    ...     return a.x\n'
 '\n'
 '    >>> f(a=dict(x=1))\n'
 '    1\n'
 '\n'
 'Authors\n'
 '-------\n'
 '\n'
 '- Jun Makii <junmakii@gmail.com>\n'
 '\n'
 'License\n'
 '-------\n'
 '\n'
 'GPLv3 <https://www.gnu.org/licenses/>'),
    cmdclass={"pytest": PyTest},
)
