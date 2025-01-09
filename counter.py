'''
lyw
25-1-09
'''
from tkinter import *

FONT = "Arial {}"
W = 3
H = 2


class Operator:
    def __init__(self, input_label: Label, result_label: Label):
        self.input_label = input_label
        self.result_label = result_label

    def set_input(self, text: str):
        self.input_label.config(text=text)

    def get_input(self):
        return self.input_label.cget('text')

    def is_empty(self):
        return self.get_input() == ""

    def add_text(self, obj):
        text = self.get_input()
        self.set_input(text + str(obj))

    def del_text(self):
        if not self.is_empty():
            self.set_input(self.get_input()[:-1])

    def set_result(self, text: str):
        self.result_label.config(text=text)

    def clear(self):
        self.set_input("")
        self.set_result("")

    def back(self, index=1):
        if len(self.get_input()) - index < 0:
            return ""
        return self.get_input()[-index]

    def is_num(self):
        return self.back().isdigit()

    def is_operator(self):
        return self.back() in ('+', '-', '*', '/', '**')

    def is_bracket(self, option=None):
        t = self.back()
        if option:
            return t == option
        return t in ('(', ')')

    def can_add_num(self):
        return self.back() != '0' or self.back(2).isdigit()

    def can_add_operator(self):
        return self.is_num() or self.is_bracket(')')

    def can_add_open_bracket(self):
        return self.is_empty() or self.is_operator() or self.is_bracket('(')

    def can_add_close_bracket(self):
        text = self.get_input()
        count = text.count('(') - text.count(')')
        return self.can_add_operator() and count > 0

    def can_add_dot(self):
        text = self.get_input()
        if not self.is_num():
            return False
        last_number = text.split(' ')[-1].split('.')
        return len(last_number) == 1

    def calculation(self):
        try:
            text = self.get_input()
            result = eval(text.replace('x', '*').replace('÷', '/'))
            self.clear()
            self.set_result(f"{text} = {result}")
        except Exception:
            self.set_result("Error")


def add_number(text):
    if oper.can_add_num():
        oper.add_text(text)


def add_operator(text):
    if oper.can_add_operator():
        oper.add_text(text)


def add_open_bracket():
    if oper.can_add_open_bracket():
        oper.add_text('(')


def add_close_bracket():
    if oper.can_add_close_bracket():
        oper.add_text(')')


def add_dot():
    if oper.can_add_dot():
        oper.add_text('.')


def handle_keypress(event):
    key = event.char
    if key.isdigit():
        add_number(key)
    elif key in '+-*/':
        add_operator(key)
    elif key == '(':
        add_open_bracket()
    elif key == ')':
        add_close_bracket()
    elif key == '.':
        add_dot()
    elif key == '\r':
        oper.calculation()
    elif key == '\x08':  # Backspace
        oper.del_text()


app = Tk()
app.title('계산기')
app.minsize(width=400, height=500)

input_label = Label(app, text="", font=FONT.format(20),
                    background='#FFFFFF', height=2)
input_label.pack(fill=BOTH)

result_label = Label(app, text="", font=FONT.format(
    15), background='#FFFFFF', height=2, borderwidth=1, relief='solid')
result_label.pack(fill=BOTH)

oper = Operator(input_label, result_label)

frame = Frame(app)
frame.pack()

for row in range(3):
    for col in range(3):
        cnt = row*3+col+1
        btn = Button(frame, text=cnt, width=W, height=H, font=FONT.format(
            20), command=lambda cnt=cnt: add_number(cnt))
        btn.grid(row=row, column=col)
btn0 = Button(frame, text="0", width=W, height=H,
              font=FONT.format(20), command=lambda: add_number(0))
btn0.grid(row=3, column=1)

dot_btn = Button(frame, text='.', width=W, height=H,
                  font=FONT.format(20), command=add_dot)
dot_btn.grid(row=3, column=4)

add_btn = Button(frame, text='+', width=W, height=H,
                 font=FONT.format(20), command=lambda: add_operator('+'))
add_btn.grid(row=0, column=3)
sub_btn = Button(frame, text='-', width=W, height=H,
                 font=FONT.format(20), command=lambda: add_operator('-'))
sub_btn.grid(row=1, column=3)
mul_btn = Button(frame, text='x', width=W, height=H,
                 font=FONT.format(20), command=lambda: add_operator('*'))
mul_btn.grid(row=2, column=3)
div_btn = Button(frame, text='÷', width=W, height=H,
                 font=FONT.format(20), command=lambda: add_operator('/'))
div_btn.grid(row=3, column=3)

pow_btn = Button(frame, text='^', width=W, height=H,
                 font=FONT.format(20), command=lambda: add_operator('**'))
pow_btn.grid(row=4, column=0)

open_btn = Button(frame, text='(', width=W, height=H,
                  font=FONT.format(20), command=add_open_bracket)
open_btn.grid(row=1, column=4)
close_btn = Button(frame, text=')', width=W, height=H,
                   font=FONT.format(20), command=add_close_bracket)
close_btn.grid(row=2, column=4)

clr_btn = Button(frame, text='c', width=W, height=H,
                 font=FONT.format(20), command=oper.clear)
clr_btn.grid(row=0, column=4)
res_btn = Button(frame, text='=', width=W, height=H,
                 font=FONT.format(20), command=oper.calculation)
res_btn.grid(row=3, column=0)
del_btn = Button(frame, text='<', width=W, height=H,
                 font=FONT.format(20), command=oper.del_text)
del_btn.grid(row=3, column=2)

app.bind('<Key>', handle_keypress)

app.mainloop()

