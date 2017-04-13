# Tkinter Buttons

In [the previous section](getting-started.md) we learned to use tkinter,
and we also talked about some common issues and anti-patterns. Now we
have most of the boring stuff out of the way, and we can focus on doing
fun things with tkinter.

## Our first button

So far our program just displays some text and that's it. In this
chapter we'll add a button that we can click into it.

```
,---------------------------.
|  Button Test  | _ | o | X |
|---------------------------|
|   This is a button test.  |
|      ______________       |
|     |,-------------\      |
|     || Click me!   |      |
|     `--------------'      |
`---------------------------'
```

Here's the code:

```python
import tkinter as tk


root = tk.Tk()

label = tk.Label(root, text="This is a button test.")
label.pack()
button = tk.Button(root, text="Click me!")
button.pack()

root.title("Button Test")
root.mainloop()
```

As you can see, the code is mostly the same as in the hello world
example, but there are some new things:

- We can create `tk.Button` widgets just like `tk.Label` widgets.
- We can `pack()` multiple widgets, and they end up below each other.
    It's also possible to change that, we'll look into it more later.
- The title of our hello world window was "tk", and it can be changed
    like `root.title("new title")`. I didn't show this in the hello
    world example because I wanted to make it as minimal as possible.

Run the program. If you click the button, nothing happens at all. That's
boring!

The button has a `command` [option](getting-started.md#widget-options),
and if we set it to a function it will be ran when the button is
clicked. This program prints hello every time we click its button:

```python
import tkinter as tk

def print_hello():
    print("hello")

root = tk.Tk()
button = tk.Button(root, text="Print hello", command=print_hello)
button.pack()
root.mainloop()
```

In this example, `print_hello` was **a callback function**. We don't
actually call it anywhere like `print_hello()`, but tkinter calls it
when the button is clicked.

I know, I know, this is still boring because the program prints to the
terminal or command prompt instead of displaying a nice message box.
We'll learn to make message boxes later.

**TODO:** write about message boxes

## Blocking callback functions

In tkinter and other GUI toolkits, all callback functions should run
about 0.1 seconds or less. Let's make a callback function that runs for
5 seconds and see what happens:

```python
import time
import tkinter as tk

def ok_callback():
    print("hello")

def stupid_callback():
    time.sleep(5)

root = tk.Tk()
button1 = tk.Button(root, text="this is OK", command=ok_callback)
button1.pack()
button2 = tk.Button(root, text="this sucks", command=stupid_callback)
button2.pack()
root.mainloop()
```

Now run the program and click the "this sucks" button. It stays pressed
down for 5 seconds. But try to do something else while it's pressed
down. You can't click the "this is OK" button and you can't even close
the window! As you can see, this really sucks.

The problem is that tkinter and other GUI toolkits do only one thing at
a time. Tkinter can't run our `ok_callback` while it's running
`stupid_callback`, and it can't even close the root window. Doing
multiple things at the same time is an advanced topic, and I'll write
more about it later.

**TODO:** write more about it some day

## Passing arguments to callback functions

Let's say that we want to make a program with 5 buttons that print
"hello 1", "hello 2" and so on. Does it mean that we need to define 5
functions?

```python
def print_hello_1():
    print("hello 1")

def print_hello_2():
    print("hello 2")

...
```

That's awful. We don't want that.

There's a better way, and it's called
[functools.partial](https://docs.python.org/3/library/functools.html#functools.partial).
It works like this:

```python
>>> import functools
>>> thing = functools.partial(print, "hello")
>>> thing()         # runs print("hello")
hello
>>> thing("world")  # runs print("hello", "world")
hello world
>>> thing(1, 2, 3)  # runs print("hello", 1, 2, 3)
hello 1 2 3
```

So we can write code like this:

```python
import functools
import tkinter as tk

def print_hello_number(number):
    print("hello", number)

root = tk.Tk()
for i in range(1, 6):
    button = tk.Button(root, text="Hello %d" % i,
                       command=functools.partial(print_hello_number, i))
    button.pack()

root.mainloop()
```

Some people would use a lambda function instead, but using lambda
functions in loops can be
[confusing](https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result).
