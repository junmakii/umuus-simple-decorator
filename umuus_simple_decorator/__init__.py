#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018  Jun Makii <junmakii@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""A decorator for Python's class.


umuus-simple-decorator
=====================

Installation
------------

    $ pip install git+https://github.com/junmakii/umuus-simple-decorator.git

----

    >>> import umuus_simple_decorator

    >>> import attr

    >>> @attr.s()
    ... class A(object):
    ...     x = attr.ib()
    ...     y = attr.ib()

    >>> @umuus_simple_decorator.decorator()
    ... def f(a: A, i: int):
    ...     a.x += i
    ...     return a

    >>> a = A(x=1, y=1)
    >>> [f(a, i) for i in range(3)]
    [A(x=4, y=1), A(x=4, y=1), A(x=4, y=1)]

    >>> @umuus_simple_decorator.decorator(copy_data=True)
    ... def f(a: A, i: int):
    ...     a.x += i
    ...     return a

    >>> a = A(x=1, y=1)
    >>> [f(a, i) for i in range(3)]
    [A(x=1, y=1), A(x=2, y=1), A(x=3, y=1)]

----

    >>> import addict

    >>> @umuus_simple_decorator.decorator()
    ... def f(a: addict.Dict):
    ...     return a.x

    >>> f(a=dict(x=1))
    1

Authors
-------

- Jun Makii <junmakii@gmail.com>

License
-------

GPLv3 <https://www.gnu.org/licenses/>

"""
import functools
import copy
import inspect
__version__ = '0.1'
__url__ = 'https://github.com/junmakii/umuus-simple-decorator'
__author__ = 'Jun Makii'
__author_email__ = 'junmakii@gmail.com'
__author_username__ = 'junmakii'
__keywords__ = []
__license__ = 'GPLv3'
__scripts__ = []
__install_requires__ = []
__dependency_links__ = []
__classifiers__ = []
__entry_points__ = {}
__project_urls__ = {}
__setup_requires__ = []
__test_suite__ = 'umuus_simple_decorator'
__tests_require__ = []
__extras_require__ = {}
__package_data__ = {}
__python_requires__ = ''
__include_package_data__ = True
__zip_safe__ = True
__static_files__ = {}
__extra_options__ = {}
__all__ = []


def decorator(fn=None,
              copy_data=False,
              data_types={},
              return_error=False,
              *args,
              **kwargs):
    if not fn:
        return functools.partial(
            decorator,
            data_types=data_types,
            copy_data=copy_data,
            return_error=return_error,
            **kwargs)
    spec = inspect.getfullargspec(fn)

    @functools.wraps(fn)
    def wrapper(*_args, **_kwargs):
        _arg_kwargs = dict(zip(spec.args[:len(_args)], _args))
        _rest_args = (_args)[len(spec.args):]
        _new_args = (args + _args)[len(spec.args):]
        _new_kwargs = functools.reduce(lambda a, b: dict(a, **b), [
            kwargs,
            _arg_kwargs,
            _kwargs,
        ])
        _new_kwargs = {
            key: value
            for key, value in _new_kwargs.items()
            if spec.varkw or key in spec.args
        }
        for key, value in _new_kwargs.items():
            annotation = spec.annotations.get(key)
            data_type = data_types.get(key)
            if (annotation and not isinstance(value, annotation)
                    and isinstance(value, dict)):
                _new_kwargs[key] = annotation(**value)
            elif data_type:
                if isinstance(value, data_type):
                    _new_kwargs[key] = value
                elif isinstance(value, dict):
                    _new_kwargs[key] = data_type(**value)
                else:
                    _new_kwargs[key] = data_type(value)
        if copy_data:
            for key, value in _new_kwargs.items():
                _new_kwargs[key] = copy.deepcopy(value)
        try:
            return fn(*_rest_args, **_new_kwargs)
        except Exception as err:
            if return_error:
                return err
            else:
                raise err

    return wrapper
