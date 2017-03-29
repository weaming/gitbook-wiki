What is the difference between arguments and parameters?
--
Parameters are defined by the names that appear in a function definition, whereas arguments are the values actually passed to a function when calling it. Parameters define what types of arguments a function can accept. For example, given the function definition:

```
def func(foo, bar=None, **kwargs):
    pass
```

foo, bar and kwargs are parameters of func. However, when calling func, for example:

```
func(42, bar=314, extra=somevar)
```

the values 42, 314, and somevar are arguments.