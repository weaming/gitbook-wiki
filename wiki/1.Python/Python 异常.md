`test.py`:

```
#coding: utf-8

import pprint

di = __builtins__.__dict__
iprint = pprint.pprint
iprint(di)
print('='*100)
for k,v in di.items():
    try:
        if issubclass(v, Exception):
            print '{}: {}\n'.format(k, v.__doc__)
    except TypeError:
        pass

```

```
$ python test.py
{'ArithmeticError': <type 'exceptions.ArithmeticError'>,
 'AssertionError': <type 'exceptions.AssertionError'>,
 'AttributeError': <type 'exceptions.AttributeError'>,
 'BaseException': <type 'exceptions.BaseException'>,
 'BufferError': <type 'exceptions.BufferError'>,
 'BytesWarning': <type 'exceptions.BytesWarning'>,
 'DeprecationWarning': <type 'exceptions.DeprecationWarning'>,
 'EOFError': <type 'exceptions.EOFError'>,
 'Ellipsis': Ellipsis,
 'EnvironmentError': <type 'exceptions.EnvironmentError'>,
 'Exception': <type 'exceptions.Exception'>,
 'False': False,
 'FloatingPointError': <type 'exceptions.FloatingPointError'>,
 'FutureWarning': <type 'exceptions.FutureWarning'>,
 'GeneratorExit': <type 'exceptions.GeneratorExit'>,
 'IOError': <type 'exceptions.IOError'>,
 'ImportError': <type 'exceptions.ImportError'>,
 'ImportWarning': <type 'exceptions.ImportWarning'>,
 'IndentationError': <type 'exceptions.IndentationError'>,
 'IndexError': <type 'exceptions.IndexError'>,
 'KeyError': <type 'exceptions.KeyError'>,
 'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>,
 'LookupError': <type 'exceptions.LookupError'>,
 'MemoryError': <type 'exceptions.MemoryError'>,
 'NameError': <type 'exceptions.NameError'>,
 'None': None,
 'NotImplemented': NotImplemented,
 'NotImplementedError': <type 'exceptions.NotImplementedError'>,
 'OSError': <type 'exceptions.OSError'>,
 'OverflowError': <type 'exceptions.OverflowError'>,
 'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>,
 'ReferenceError': <type 'exceptions.ReferenceError'>,
 'RuntimeError': <type 'exceptions.RuntimeError'>,
 'RuntimeWarning': <type 'exceptions.RuntimeWarning'>,
 'StandardError': <type 'exceptions.StandardError'>,
 'StopIteration': <type 'exceptions.StopIteration'>,
 'SyntaxError': <type 'exceptions.SyntaxError'>,
 'SyntaxWarning': <type 'exceptions.SyntaxWarning'>,
 'SystemError': <type 'exceptions.SystemError'>,
 'SystemExit': <type 'exceptions.SystemExit'>,
 'TabError': <type 'exceptions.TabError'>,
 'True': True,
 'TypeError': <type 'exceptions.TypeError'>,
 'UnboundLocalError': <type 'exceptions.UnboundLocalError'>,
 'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>,
 'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>,
 'UnicodeError': <type 'exceptions.UnicodeError'>,
 'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>,
 'UnicodeWarning': <type 'exceptions.UnicodeWarning'>,
 'UserWarning': <type 'exceptions.UserWarning'>,
 'ValueError': <type 'exceptions.ValueError'>,
 'Warning': <type 'exceptions.Warning'>,
 'WindowsError': <type 'exceptions.WindowsError'>,
 'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>,
 '__debug__': True,
 '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis repres
ents `...' in slices.",
 '__import__': <built-in function __import__>,
 '__name__': '__builtin__',
 '__package__': None,
 'abs': <built-in function abs>,
 'all': <built-in function all>,
 'any': <built-in function any>,
 'apply': <built-in function apply>,
 'basestring': <type 'basestring'>,
 'bin': <built-in function bin>,
 'bool': <type 'bool'>,
 'buffer': <type 'buffer'>,
 'bytearray': <type 'bytearray'>,
 'bytes': <type 'str'>,
 'callable': <built-in function callable>,
 'chr': <built-in function chr>,
 'classmethod': <type 'classmethod'>,
 'cmp': <built-in function cmp>,
 'coerce': <built-in function coerce>,
 'compile': <built-in function compile>,
 'complex': <type 'complex'>,
 'copyright': Copyright (c) 2001-2015 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.,
 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.,
 'delattr': <built-in function delattr>,
 'dict': <type 'dict'>,
 'dir': <built-in function dir>,
 'divmod': <built-in function divmod>,
 'enumerate': <type 'enumerate'>,
 'eval': <built-in function eval>,
 'execfile': <built-in function execfile>,
 'exit': Use exit() or Ctrl-Z plus Return to exit,
 'file': <type 'file'>,
 'filter': <built-in function filter>,
 'float': <type 'float'>,
 'format': <built-in function format>,
 'frozenset': <type 'frozenset'>,
 'getattr': <built-in function getattr>,
 'globals': <built-in function globals>,
 'hasattr': <built-in function hasattr>,
 'hash': <built-in function hash>,
 'help': Type help() for interactive help, or help(object) for help about object.,
 'hex': <built-in function hex>,
 'id': <built-in function id>,
 'input': <built-in function input>,
 'int': <type 'int'>,
 'intern': <built-in function intern>,
 'isinstance': <built-in function isinstance>,
 'issubclass': <built-in function issubclass>,
 'iter': <built-in function iter>,
 'len': <built-in function len>,
 'license': Type license() to see the full license text,
 'list': <type 'list'>,
 'locals': <built-in function locals>,
 'long': <type 'long'>,
 'map': <built-in function map>,
 'max': <built-in function max>,
 'memoryview': <type 'memoryview'>,
 'min': <built-in function min>,
 'next': <built-in function next>,
 'object': <type 'object'>,
 'oct': <built-in function oct>,
 'open': <built-in function open>,
 'ord': <built-in function ord>,
 'pow': <built-in function pow>,
 'print': <built-in function print>,
 'property': <type 'property'>,
 'quit': Use quit() or Ctrl-Z plus Return to exit,
 'range': <built-in function range>,
 'raw_input': <built-in function raw_input>,
 'reduce': <built-in function reduce>,
 'reload': <built-in function reload>,
 'repr': <built-in function repr>,
 'reversed': <type 'reversed'>,
 'round': <built-in function round>,
 'set': <type 'set'>,
 'setattr': <built-in function setattr>,
 'slice': <type 'slice'>,
 'sorted': <built-in function sorted>,
 'staticmethod': <type 'staticmethod'>,
 'str': <type 'str'>,
 'sum': <built-in function sum>,
 'super': <type 'super'>,
 'tuple': <type 'tuple'>,
 'type': <type 'type'>,
 'unichr': <built-in function unichr>,
 'unicode': <type 'unicode'>,
 'vars': <built-in function vars>,
 'xrange': <type 'xrange'>,
 'zip': <built-in function zip>}
====================================================================================================
IndexError: Sequence index out of range.

SyntaxError: Invalid syntax.

UnicodeDecodeError: Unicode decoding error.

NameError: Name not found globally.

BytesWarning: Base class for warnings about bytes and buffer related problems, mostly
related to conversion from str or comparing to str.

StandardError: Base class for all standard Python exceptions that do not represent
interpreter exiting.

RuntimeWarning: Base class for warnings about dubious runtime behavior.

Warning: Base class for warning categories.

EOFError: Read beyond end of file.

BufferError: Buffer error.

FloatingPointError: Floating point operation failed.

FutureWarning: Base class for warnings about constructs that will change semantically
in the future.

ImportWarning: Base class for warnings about probable mistakes in module imports

ReferenceError: Weak ref proxy used after referent went away.

TypeError: Inappropriate argument type.

UserWarning: Base class for warnings generated by user code.

SystemError: Internal error in the Python interpreter.

Please report this to the Python maintainer, along with the traceback,
the Python version, and the hardware/OS platform and version.

RuntimeError: Unspecified run-time error.

MemoryError: Out of memory.

StopIteration: Signal the end from iterator.next().

LookupError: Base class for lookup errors.

UnicodeError: Unicode related error.

ImportError: Import can't find module, or can't find name in module.

Exception: Common base class for all non-exit exceptions.

UnicodeTranslateError: Unicode translation error.

UnicodeEncodeError: Unicode encoding error.

IOError: I/O operation failed.

SyntaxWarning: Base class for warnings about dubious syntax.

ArithmeticError: Base class for arithmetic errors.

KeyError: Mapping key not found.

PendingDeprecationWarning: Base class for warnings about features which will be deprecated
in the future.

EnvironmentError: Base class for I/O related errors.

OSError: OS system call failed.

DeprecationWarning: Base class for warnings about deprecated features.

UnicodeWarning: Base class for warnings about Unicode related problems, mostly
related to conversion problems.

ValueError: Inappropriate argument value (of correct type).

TabError: Improper mixture of spaces and tabs.

ZeroDivisionError: Second argument to a division or modulo operation was zero.

IndentationError: Improper indentation.

AssertionError: Assertion failed.

UnboundLocalError: Local name referenced but not bound to a value.

NotImplementedError: Method or function hasn't been implemented yet.

AttributeError: Attribute not found.

OverflowError: Result too large to be represented.

WindowsError: MS-Windows OS system call failed.
```