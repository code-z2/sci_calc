from tkinter import *
import parser

root = Tk()
root.title('calculator')

# get user click
i = 0


def get_click(num):
    global i
    display.insert(i, num)
    i += 1


def clear_all():
    display.delete(0, END)


def undo():
    entire = display.get()
    if len(entire):
        new_str = entire[:-1]
        clear_all()
        display.insert(0, new_str)
    else:
        clear_all()
        display.insert(0, 'Error')


def arthimetic(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def calculate():
    expression = display.get()
    try:
        a = parser.expr(expression).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, 'Error')


def factorial():
    expression = display.get()
    try:
        a = parser.expr(expression).compile()
        n = eval(a)

        fact = 1
        for num in range(1, int(n) + 1):
            fact = fact * num
        clear_all()
        display.insert(0, fact)

    except Exception:
        clear_all()
        display.insert(0, 'Error')


# input field
display = Entry(root)
display.grid(row=0, columnspan=6, sticky=W + E)

# buttons
Button(root, text='1', command=lambda: get_click(1)).grid(row=1, column=0)
Button(root, text='2', command=lambda: get_click(2)).grid(row=1, column=1)
Button(root, text='3', command=lambda: get_click(3)).grid(row=1, column=2)

Button(root, text='4', command=lambda: get_click(4)).grid(row=2, column=0)
Button(root, text='5', command=lambda: get_click(5)).grid(row=2, column=1)
Button(root, text='6', command=lambda: get_click(6)).grid(row=2, column=2)

Button(root, text='7', command=lambda: get_click(7)).grid(row=3, column=0)
Button(root, text='8', command=lambda: get_click(8)).grid(row=3, column=1)
Button(root, text='9', command=lambda: get_click(9)).grid(row=3, column=2)

Button(root, text='AC', command=lambda: clear_all()).grid(row=4, column=0)
Button(root, text='0', command=lambda: get_click(0)).grid(row=4, column=1)
Button(root, text='=', command=lambda: calculate()).grid(row=4, column=2)

Button(root, text='+', command=lambda: arthimetic('+')).grid(row=1, column=3)
Button(root, text='-', command=lambda: arthimetic('-')).grid(row=2, column=3)
Button(root, text='*', command=lambda: arthimetic('*')).grid(row=3, column=3)
Button(root, text='/', command=lambda: arthimetic('/')).grid(row=4, column=3)

Button(root, text='pi', command=lambda: arthimetic('*3.143')).grid(row=1, column=4)
Button(root, text='%', command=lambda: arthimetic('%')).grid(row=2, column=4)
Button(root, text='(', command=lambda: arthimetic('(')).grid(row=3, column=4)
Button(root, text='pow', command=lambda: arthimetic('**')).grid(row=4, column=4)

Button(root, text='del', command=lambda: undo()).grid(row=1, column=5)
Button(root, text='!', command=lambda: factorial()).grid(row=2, column=5)
Button(root, text=')', command=lambda: arthimetic(')')).grid(row=3, column=5)
Button(root, text='^2', command=lambda: arthimetic('**2')).grid(row=4, column=5)

root.mainloop()
