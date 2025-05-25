"""
GameUtils.py

General utility functions and classes for the Pirates game.
"""

from direct.showbase import DConfig
import builtins

__all__ = ['Functor', 'recordFunctorCreationStacks']

class Functor:
    def __init__(self, function, *args, **kargs):
        assert callable(function), "function should be a callable obj"
        self._function = function
        self._args = args
        self._kargs = kargs
        self.__name__ = getattr(self._function, '__name__', type(self._function).__name__)
        self.__doc__ = getattr(self._function, '__doc__', self.__name__)

    def destroy(self):
        del self._function
        del self._args
        del self._kargs
        del self.__name__
        del self.__doc__

    def _do__call__(self, *args, **kargs):
        _kargs = self._kargs.copy()
        _kargs.update(kargs)
        return self._function(*self._args, *args, **_kargs)

    # this method is used in place of __call__ if we are recording creation stacks
    def _exceptionLoggedCreationStack__call__(self, *args, **kargs):
        try:
            return self._do__call__(*args, **kargs)
        except Exception as e:
            print('-->Functor creation stack ({}): {}'.format(
                self.__name__, getattr(self, 'getCreationStackTraceCompactStr', lambda: 'N/A')()))
            raise

    __call__ = _do__call__

    def __repr__(self):
        s = f'Functor({getattr(self._function, "__name__", repr(self._function))}'
        for arg in self._args:
            try:
                argStr = repr(arg)
            except Exception:
                argStr = f'bad repr: {type(arg)}'
            s += f', {argStr}'
        for karg, value in self._kargs.items():
            s += f', {karg}={repr(value)}'
        s += ')'
        return s

def recordFunctorCreationStacks():
    from .GameUtils import Functor
    if '__dev__' in globals() and __dev__ and DConfig.GetBool('record-functor-creation-stacks', 0):
        if not hasattr(Functor, '_functorCreationStacksRecorded'):
            def recordCreationStackStr(cls):
                return cls
            Functor = recordCreationStackStr(Functor)
            Functor._functorCreationStacksRecorded = True
            if hasattr(Functor, '_exceptionLoggedCreationStack__call__'):
                Functor.__call__ = Functor._exceptionLoggedCreationStack__call__

# Add utility functions and classes below 
builtins.recordFunctorCreationStacks = recordFunctorCreationStacks
builtins.Functor = Functor