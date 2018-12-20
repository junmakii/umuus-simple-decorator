

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