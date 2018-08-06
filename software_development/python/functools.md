#### functools - tools for manipulating functions

First, let's import functools.

```python
import functools
```

There is something called `partial`. This is a class. Let's see what this does.

```python
def my_func(a, b=2):
    "Docstring for my_func"
    print(' called my_func with:', (a, b))
```

Okay that is a some function. Whenever someone calls it, it will print something. Let's see
where this is going. Let's move on to the next function.

```python
def show_details(name, f, is_partial=False):
    "Show details of a callable object"
    print('{}:'.format(name))
    print(' object:', f)
    if not is_partial:
        print(' __name__:', f.__name__)
    if is_partial:
        print(' func:', f.func)
        print(' args:', f.args)
        print(' keywords:', f.keywords)
    return
```

So that was some function. Let's see how it works.

```python
show_details('my_func', my_func)
```

Okay, so it printed this:

```commandline
my_func:
 object: <function my_func at 0x7f92d5c05510>
 __name__: my_func
```

Now let's try some more code.

```python
p1 = functools.partial(my_func, b=4)
show_details('partial with named default', p1, True)
```

I got this now:

```commandline
partial with named default:
 object: functools.partial(<function my_func at 0x7f92d5c05510>, b=4)
 func: <function my_func at 0x7f92d5c05510>
 args: ()
 keywords: {'b': 4}
```

Now `p1` is a function. It is actually a `partial` object:

```python
p1('passing a')
p1('override b', b=5)
```

which gives:

```commandline
 called my_func with: ('passing a', 4)
 called my_func with: ('override b', 5)
```

Good. Now let's set a partial with both default values.

```python
p2 = functools.partial(my_func, 'default a', b=99)
show_details('partial with defaults', p2, True)
```

This gives the following output:

```commandline
partial with defaults:
 object: functools.partial(<function my_func at 0x7f92d5c05510>, 'default a', b=99)
 func: <function my_func at 0x7f92d5c05510>
 args: ('default a',)
 keywords: {'b': 99}
```

Okay, so now I get the idea. I can pass some default values to function arguments using `functools.partial`. But this
can also be done easily without using `functools.partial`. The main thing is that I can over-ride the default values
of the arguments in the function. So I can create a host of new functions from the existing function, by using different
default values for the arguments.

Now, these `functools.partial` objects do not have `__name__` or `__doc__` attributes by default and it seems that these
decorated functions now become difficult to debug without these attributes. Using `update_wrapper()` copies these
attributes from the original functions to the `partial` objects.

Consider the following snippet:

```python
def show_details(name, f):
    """Show details of a callable object."""
    print('{}'.format(name))
    print(' object:', f)
    try:
        print(' name:', f.__name__)
    except AttributeError:
        print(' name:', '(no __name__)')
    print(' __doc__', f.__doc__)
    
show_details('my_func', my_func)
p1 = functools.partial(my_func, b=5)
show_details('wrapper', p1)
```

This shows me:

```commandline
my_func
 object: <function my_func at 0x7f92d5c05510>
 name: my_func
 __doc__ Docstring for my_func
wrapper
 object: functools.partial(<function my_func at 0x7f92d5c05510>, b=5)
 name: (no __name__)
 __doc__ partial(func, *args, **keywords) - new function with partial application
    of the given arguments and keywords.
```

Now, if I use `update_wrapper`, using like `functools.update_wrapper(p1, my_func)`. Then our wrapper `p1` will have the
concerned attributes `__name__` and `__doc__` from the original function `my_func`.

Now, let's delve deeper.

```python
import functools

def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print(' decorated:', (a, b))
        return f(a, b=b)
    return decorated
    
    
def my_func(a, b=2):
    """my_func() is not complicated"""
    print(' my_func:', (a, b))
    return


@simple_decorator
def decorated_my_func(a, b):
    """This is docstring."""
    my_func(a,b)
    return
```

Okay, so we see that `functools.wraps` automatically applies the `update_wrapper()` which applies the attributes of the
original function to the decorated function.

That's it for now.
