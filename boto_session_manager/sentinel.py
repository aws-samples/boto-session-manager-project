# -*- coding: utf-8 -*-

import typing as T
import sys


def make_sentinel(name="_MISSING", var_name=None):  # pragma: no cover
    """Creates and returns a new **instance** of a new class, suitable for
    usage as a "sentinel", a kind of singleton often used to indicate
    a value is missing when ``None`` is a valid input.
    Args:
        name (str): Name of the Sentinel
        var_name (str): Set this name to the name of the variable in
            its respective module enable pickleability. Note:
            pickleable sentinels should be global constants at the top
            level of their module.
    >>> make_sentinel(var_name='_MISSING')
    _MISSING
    The most common use cases here in boltons are as default values
    for optional function arguments, partly because of its
    less-confusing appearance in automatically generated
    documentation. Sentinels also function well as placeholders in queues
    and linked lists.
    .. note::
      By design, additional calls to ``make_sentinel`` with the same
      values will not produce equivalent objects.
      >>> make_sentinel('TEST') == make_sentinel('TEST')
      False
      >>> type(make_sentinel('TEST')) == type(make_sentinel('TEST'))
      False
    """

    class Sentinel(object):
        def __init__(self):
            self.name = name
            self.var_name = var_name

        def __repr__(self):
            if self.var_name:
                return self.var_name
            return "%s(%r)" % (self.__class__.__name__, self.name)

        if var_name:

            def __reduce__(self):
                return self.var_name

        def __nonzero__(self):
            return False

        __bool__ = __nonzero__

    if var_name:
        frame = sys._getframe(1)
        module = frame.f_globals.get("__name__")
        if not module or module not in sys.modules:
            raise ValueError(
                "Pickleable sentinel objects (with var_name) can only"
                " be created from top-level module scopes"
            )
        Sentinel.__module__ = module

    return Sentinel()


NOTHING = make_sentinel(name="NOTHING")


def resolve_kwargs(
    _mapper: T.Optional[T.Dict[str, str]] = None,
    **kwargs,
) -> dict:
    if _mapper is None:  # pragma: no cover
        _mapper = dict()
    return {
        _mapper.get(key, key): value
        for key, value in kwargs.items()
        if value is not NOTHING
    }
