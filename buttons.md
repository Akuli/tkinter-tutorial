# Buttons

In [the previous section](getting-started.md) we learned to use tkinter,
and we also talked about some common issues and anti-patterns. Now we
have most of the boring stuff out of the way, and we can focus on doing
fun things with tkinter.

## Our first button

So far our programs just display text and that's it. In this chapter
we'll add a button that we can click.

```
,---------------------------.
| Button Test   | _ | o | X |
|---------------------------|
|   This is a button test.  |
|      ,-------------.      |
|      |  Click me!  |      |
|      `-------------'      |
|                           |
|                           |
|                           |
`---------------------------'
```

Here's the code:

[include]: # (boring-button.py)
```python
import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame, text="This is a button test.")
label.pack()
button = ttk.Button(big_frame, text="Click me!")
button.pack()

root.title("Button Test")
root.geometry('200x100')
root.minsize(150, 50)
root.mainloop()
```

As you can see, the code is mostly the same as in the hello world
example, but there are some new things. I didn't show these in the hello
world example because I wanted to keep it as simple as possible.

- We can create `ttk.Button` widgets just like `ttk.Label` widgets.
- We can `pack()` multiple widgets, and they end up below each other.
    We'll talk more about this in [the next chapter](geometry-managers.md).
- The title of our hello world window was "tk", but it can be changed
    like `root.title("new title")`.
- I changed the size of the root window with `root.geometry('200x100')`.
    It was 200 pixels wide and 100 pixels high by default, but you can
    still resize the window by dragging its edges with the mouse. If you
    aren't sure which default size you should use just try different
    sizes and see what looks best.
- `root.minsize(150, 50)` means that the root window can't be made
    smaller than 150 by 50 pixels. I have no idea why this method takes
    two integers and the geometry method takes a string, but this is how
    it works. You can also do `root.resizable(False, False)` if you want
    to prevent the user from resizing the window at all.

Run the program. If you click the button, nothing happens at all. That's
boring!

As usual, all possible [options](getting-started.md#widget-options) are
listed in the [ttk_button(3tk)] manual page. One of these
options is `command`, and if we set it to a function it will be ran when
the button is clicked. This program prints hello every time we click its
button:

[include]: # (working-button.py)
```python
import tkinter
from tkinter import ttk


def print_hello():
    print("hello")


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button = ttk.Button(big_frame, text="Print hello", command=print_hello)
button.pack()
root.mainloop()
```

In this example, `print_hello` was **a callback function**. We don't
actually call it anywhere like `print_hello()`, but tkinter calls it
when the button is clicked.

This is still boring because the program prints to the terminal or
command prompt instead of doing something with the GUI. This program is more
interesting. It changes the text of a label whenever the button is clicked.

[include]: # (button-changes-label.py)
```python
import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame, text='Hello')
label.pack()


def change_text():
    if label['text'] == 'Hello':
        label['text'] = 'World'
    else:
        label['text'] = 'Hello'


button = ttk.Button(big_frame, text="Click here", command=change_text)
button.pack()
root.mainloop()
```

## Blocking callback functions

In tkinter and other GUI toolkits, all callbacks should run about 0.1
seconds or less. Let's make a callback function that runs for 5 seconds
and see what happens:

[include]: # (stupid-callback.py)
```python
import time
import tkinter
from tkinter import ttk


def ok_callback():
    print("hello")


def stupid_callback():
    time.sleep(5)


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button1 = ttk.Button(big_frame, text="This is OK", command=ok_callback)
button1.pack()
button2 = ttk.Button(big_frame, text="This sucks", command=stupid_callback)
button2.pack()

root.mainloop()
```

Now run the program and click the "this sucks" button. It stays pressed
down for 5 seconds. But try to do something else while it's pressed
down. You can't click the "this is OK" button and you can't even close
the window! This program sucks.

The problem is that tkinter and other GUI toolkits do only one thing at
a time. Tkinter can't run our `ok_callback` while it's running
`stupid_callback`, and it can't even close the root window. This isn't
limited to button commands, all tkinter callbacks should take at most
0.1 seconds.

Doing multiple things at the same time is an advanced topic, and we'll
learn more about it [later](event-loop-stuff.md).

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

[include]: # (many-buttons.py)
```python
import functools
import tkinter
from tkinter import ttk


def print_hello_number(number):
    print("hello", number)


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

for i in range(1, 6):
    button = ttk.Button(big_frame, text="Hello %d" % i,
                        command=functools.partial(print_hello_number, i))
    button.pack()

root.mainloop()
```

Some people would use a lambda function instead, but using lambda
functions in loops can be
[confusing](https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result).

## Summary
- The `ttk.Button` widget displays a button.
- Buttons have a `command` option. It can be set to a function that runs
  when the button is clicked.
- Button commands and other callbacks should not block. It means that
  they should run only a short time, about 0.1 seconds or less.
- Use `functools.partial` when you need to pass arguments to callbacks.

[manpage list]: # (start)
[ttk_button(3tk)]: https://www.tcl.tk/man/tcl/TkCmd/ttk_button.htm
[manpage list]: # (end)
