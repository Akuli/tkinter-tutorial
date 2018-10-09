# Geometry Managers

So far we have used the `pack()` method to add labels and buttons to our
root window. Pack is one of the simplest geometry managers in Tk. In
this tutorial we'll learn more about pack and other geometry managers.

## Pack

The [pack(3tk)] geometry manager is really simple and easy to
use. Let's create a window like this with it:

```
,--------------------------------------------.
| Pack Test                      | _ | o | X |
|--------------------------------------------|
|,--------------------.                      |
||                    |                      |
||                    |                      |
||                    |                      |
||   This stretches   | This doesn't stretch |
||                    |                      |
||                    |                      |
||                    |                      |
|`--------------------'                      |
|--------------------------------------------|
|            This is a status bar            |
`--------------------------------------------'
```

Here's the code.

[include]: # (pack.py)
```python
import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button = ttk.Button(big_frame, text="This stretches")
label = ttk.Label(big_frame, text="This doesn't stretch")
statusbar = ttk.Label(big_frame, text="This is a status bar", relief='sunken')

statusbar.pack(side='bottom', fill='x')
button.pack(side='left', fill='both', expand=True)
label.pack(side='left')

root.title("Pack Test")
root.geometry('300x150')
root.mainloop()
```

Run the program and change the size of the window by dragging its edges
with the mouse. The button and status bar should stretch and shrink
nicely.

Let's go through the pack stuff in the code:

```python
statusbar.pack(side='bottom', fill='x')
```

The `fill='x'` means that the status bar will fill all of the space it
has horizontally. We can also do `fill='y'` or `fill='both'`.

Obviously, `side='bottom'` means that the status bar will appear at the
bottom of the window. The default is `side='top'`. Note that I packed
the status bar **before packing any other widgets**, because even with
`side='bottom'`, it won't go below widgets that are already packed with
`side='left'` or `side='right'`.

```python
button.pack(side='left', fill='both', expand=True)
```

We want the button to fill all the space it has, so we're using
`fill='both'`. But we also want to give it as much space as possible, so
we're using `expand=True`. If you remove the `expand=True` and run the
program again, you'll notice that the button doesn't stretch anymore
becuase it doesn't have any space to fill.

```python
label.pack(side='left')
```

We packed the button with `side='left'` first and then the label, so
they ended up next to each other so that the button is on the left side
of the label.

## Grid

Let's make a similar GUI as in the pack example, but with [grid(3tk)] instead
of pack.

[include]: # (grid.py)
```python
import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button = ttk.Button(big_frame, text="This stretches")
label = ttk.Label(big_frame, text="This doesn't stretch")
statusbar = ttk.Label(big_frame, text="This is a status bar", relief='sunken')

button.grid(row=0, column=0, sticky='nswe')
label.grid(row=0, column=1)
statusbar.grid(row=1, column=0, columnspan=2, sticky='we')

big_frame.grid_rowconfigure(0, weight=1)
big_frame.grid_columnconfigure(0, weight=1)

root.title("Grid Test")
root.geometry('300x150')
root.mainloop()
```

The code is mostly the same. Let's go through the differences:

```python
button.grid(row=0, column=0, sticky='nswe')
```

The `row=0` and `column=0` mean that the button will end up in the
**top** left corner of our root window. In math, the coordinate (0, 0)
usually means the bottom left corner, but in programming it almost
always means the top left corner.

`sticky='nswe'` might look weird at first, but it's actually simple to
understand. The n means north, s means south and so on. To be honest I
have no idea why Tk doesn't just use l like left, r like right etc.

The sticky option is kind of like the fill option of `pack()`.
`sticky='nswe'` is like `fill='both'`, `sticky='we'` is like `fill='x'`
and so on.

```python
label.grid(row=0, column=1)
```

This adds the label next to the button. It doesn't stretch because we
didn't set a sticky value, and it defaults to `''`.

```python
statusbar.grid(row=1, column=0, columnspan=2, sticky='we')
```

`columnspan=2` means that the status bar will be two columns wide, so it
fills the entire width of the window because we have two columns.

Note that we don't have to grid the statusbar before gridding other
widgets. Each widget goes to its own row and column so it doesn't matter
which order we add them in.

```python
big_frame.grid_rowconfigure(0, weight=1)
big_frame.grid_columnconfigure(0, weight=1)
```

This is like setting `expand=True` with pack. The button is packed to
row 0 and column 0, and this gives it as much space as possible.

Here's another, more advanced grid example:

```
,-------------------.
| Calculator    | X |
|-------------------|
| 7 | 8 | 9 | * | / |
|---+---+---+---+---|
| 4 | 5 | 6 | + | - |
|---+---+---+-------|
| 1 | 2 | 3 |       |
|-------+---|   =   |
|   0   | . |       |
`-------------------'
```

Something like this would be almost impossible to do with pack, but it's
easy with grid:

[include]: # (calculator.py)
```python
import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

# None means that we'll create the button later
rows = [
    ['7', '8', '9', '*', '/'],
    ['4', '5', '6', '+', '-'],
    ['1', '2', '3', None, None],
    [None, None, '.', None, None],
]

for y, row in enumerate(rows):
    for x, character in enumerate(row):
        if character is not None:
            # try this without width=3 so you'll know why i put it there
            button = ttk.Button(big_frame, text=character, width=3)
            button.grid(row=y, column=x, sticky='nswe')

# the widths of these buttons are set to smallest possible values because grid
# will make sure that they are wide enough, e.g. zerobutton is below '1' and
# '2', and it will have the same width as the '1' and '2' buttons together
zerobutton = ttk.Button(big_frame, text='0', width=1)
zerobutton.grid(row=3, column=0, columnspan=2, sticky='nswe')
equalbutton = ttk.Button(big_frame, text='=', width=1)
equalbutton.grid(row=2, column=3, rowspan=2, columnspan=2, sticky='nswe')

# let's make everything stretch when the window is resized
for x in range(5):
    big_frame.grid_columnconfigure(x, weight=1)
for y in range(4):
    big_frame.grid_rowconfigure(y, weight=1)

root.title("Calculator")
root.mainloop()
```

## Place

The [place(3tk)] geometry manager can be used for absolute
positioning with pixels, and that's almost always a bad idea. But place
supports relative positioning too, and it's useful for things like
message boxes. Tk has [built-in message
boxes](dialogs.md#built-in-dialogs) too, but place is useful if you want
a customized message box.

```
,-----------------------------------.
| Important Message     | _ | o | X |
|-----------------------------------|
|                                   |
|                                   |
| This is a very important message. |
|                                   |
|                                   |
|                                   |
|                                   |
|             ,------.              |
|             |  OK  |              |
|             `------'              |
`-----------------------------------'
```

Here's the code:

[include]: # (place.py)
```python
import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame, text="This is a very important message.")
label.place(relx=0.5, rely=0.3, anchor='center')
button = ttk.Button(big_frame, text="OK", command=root.destroy)
button.place(relx=0.5, rely=0.8, anchor='center')

root.title("Important Message")
root.geometry('250x150')
root.mainloop()
```

Run the program and resize the window. The label and the button should
"float" in it nicely.

```python
label.place(relx=0.5, rely=0.3, anchor='center')
```

The `relx` and `rely` options are actually short for "relative x" and
"relative y", not relaxing and relying. This means that the center of
the button will always be 50% from the left side of the window and 30%
from the top of the window. Other valid anchor values are n like north,
nw like north-west and so on.

```python
button = ttk.Button(..., command=root.destroy)
```

This example isn't as boring as our calculator is because the OK button
actually works. Calling `root.destroy()` stops `root.mainloop()`.

## Which geometry manager should I use?

Pack is good for laying out big things. If you have a program with a few
big widgets next to each other and a statusbar, pack is the best way to
add them to the root window.

Grid works for big things too, but it's best for things that are
obviously grids, like our calculator.

Place is the easiest choice when you want to use percents to position
widgets relatively, like we did in our pack example. This is useful with
things like message dialogs.

## Combining the geometry managers

**Only use one geometry manager in one widget.** The results can be
surprising if you first grid something and then pack something else.
Unfortunately tkinter doesn't raise an exception if you try to do that,
but don't do it.

You can still use multiple geometry managers in one program with
`ttk.Frame`. The frame is a simple widget that can be added to any other
parent widget, and then other widgets can be added into the frame with a
different geometry manager.

For example, this program uses pack, grid and place, but in separate
frames:

[include]: # (frames.py)
```python
import tkinter
from tkinter import ttk


def make_calculator_frame(big_frame):
    frame = ttk.Frame(big_frame)

    rows = [
        ['7', '8', '9', '*', '/'],
        ['4', '5', '6', '+', '-'],
        ['1', '2', '3', None, None],
        [None, None, '.', None, None],
    ]

    for y, row in enumerate(rows):
        for x, character in enumerate(row):
            if character is not None:
                button = ttk.Button(frame, text=character, width=3)
                button.grid(row=y, column=x, sticky='nswe')

    zerobutton = ttk.Button(frame, text='0', width=1)
    zerobutton.grid(row=3, column=0, columnspan=2, sticky='nswe')
    equalbutton = ttk.Button(frame, text='=', width=1)
    equalbutton.grid(row=2, column=3, rowspan=2, columnspan=2, sticky='nswe')

    for x in range(5):
        frame.grid_columnconfigure(x, weight=1)
    for y in range(4):
        frame.grid_rowconfigure(y, weight=1)

    return frame


def make_message_frame(big_frame):
    frame = ttk.Frame(big_frame)

    label = ttk.Label(frame, text="This is a very important message.")
    label.place(relx=0.5, rely=0.3, anchor='center')
    button = ttk.Button(frame, text="OK")
    button.place(relx=0.5, rely=0.8, anchor='center')

    return frame


def main():
    root = tkinter.Tk()
    big_frame = ttk.Frame(root)
    big_frame.pack(fill='both', expand=True)

    calculator = make_calculator_frame(big_frame)
    message = make_message_frame(big_frame)
    statusbar = ttk.Label(big_frame, text="This is a status bar.",
                          relief='sunken')

    statusbar.pack(side='bottom', fill='x')
    calculator.pack(side='left', fill='y')
    message.pack(side='left', fill='both', expand=True)

    root.title("Useless GUI")
    root.geometry('450x200')
    root.minsize(400, 100)
    root.mainloop()


if __name__ == '__main__':
    main()
```

## Summary

- Geometry managers are used for adding child widgets to parent widgets.
- Use pack for big and simple layouts, grid for griddy things and place
  for relative things.
- Don't use multiple geometry managers in one widget. You can mix
  different geometry managers with `ttk.Frame` by using one geometry
  manager in each frame.

[manpage list]: # (start)
[grid(3tk)]: https://www.tcl.tk/man/tcl/TkCmd/grid.htm
[pack(3tk)]: https://www.tcl.tk/man/tcl/TkCmd/pack.htm
[place(3tk)]: https://www.tcl.tk/man/tcl/TkCmd/place.htm
[manpage list]: # (end)
