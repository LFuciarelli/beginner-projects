import tkinter


def bt_click(item):
    """
    :param item: the digits from 0 to 9 and the operator +, -, x(*) and /.
    :return: None
    """
    global expression
    expression += item
    label_text.set(expression)


def bt_clear():
    """
    :return: None
    """
    global expression
    expression = ""
    label_text.set("0")


def bt_calc():
    """
    :return: None
    """
    global expression
    expression = expression.replace("x", "*")
    tot = str(eval(expression))                     # The function eval() solves the mathematical expression
    if tot != "0":
        expression = tot
    else:
        expression = ""
    label_text.set(tot)


window = tkinter.Tk()                               # Creates a window
window.title("Calculator")

window.geometry("270x422")                          # width x height

# The calculator screen

label_text = tkinter.StringVar()
expression = ""
label_text.set(expression)
screen = tkinter.Label(window, textvariable=label_text, anchor="e", height=4, width=37).grid(row=0, columnspan=4)

# The calculator buttons

bt_c = tkinter.Button(window, text="C", height=4, width=37, command=lambda: bt_clear()).grid(row=1, columnspan=4)

bt_7 = tkinter.Button(window, text="7", height=4, width=8, command=lambda: bt_click("7")).grid(row=2, column=0)
bt_8 = tkinter.Button(window, text="8", height=4, width=8, command=lambda: bt_click("8")).grid(row=2, column=1)
bt_9 = tkinter.Button(window, text="9", height=4, width=8, command=lambda: bt_click("9")).grid(row=2, column=2)
bt_plus = tkinter.Button(window, text="+", height=4, width=8, command=lambda: bt_click("+")).grid(row=2, column=3)

bt_4 = tkinter.Button(window, text="4", height=4, width=8, command=lambda: bt_click("4")).grid(row=3, column=0)
bt_5 = tkinter.Button(window, text="5", height=4, width=8, command=lambda: bt_click("5")).grid(row=3, column=1)
bt_6 = tkinter.Button(window, text="6", height=4, width=8, command=lambda: bt_click("6")).grid(row=3, column=2)
bt_minus = tkinter.Button(window, text="-", height=4, width=8, command=lambda: bt_click("-")).grid(row=3, column=3)

bt_1 = tkinter.Button(window, text="1", height=4, width=8, command=lambda: bt_click("1")).grid(row=4, column=0)
bt_2 = tkinter.Button(window, text="2", height=4, width=8, command=lambda: bt_click("2")).grid(row=4, column=1)
bt_3 = tkinter.Button(window, text="3", height=4, width=8, command=lambda: bt_click("3")).grid(row=4, column=2)
bt_mult = tkinter.Button(window, text="x", height=4, width=8, command=lambda: bt_click("x")).grid(row=4, column=3)

bt_p = tkinter.Button(window, text=".", height=4, width=8, command=lambda: bt_click(".")).grid(row=5, column=0)
bt_0 = tkinter.Button(window, text="0", height=4, width=8, command=lambda: bt_click("0")).grid(row=5, column=1)
bt_equals = tkinter.Button(window, text="=", height=4, width=8, command=lambda: bt_calc()).grid(row=5, column=2)
bt_div = tkinter.Button(window, text="/", height=4, width=8, command=lambda: bt_click("/")).grid(row=5, column=3)

window.mainloop()
