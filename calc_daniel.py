# -*- coding: utf-8 -*-
"""
Created on Tue May 11 18:02:28 2021

@source: inspired and expanded from https://stackoverflow.com/questions/44357846/python-gui-tkinter-scientific-calculator
"""

from tkinter import ttk
from math import*

class Calculator:
    c_state = "Input1"   # other options: Input2    Result    Error 
    c_operation = "None" # other options + - x / ^
    c_input1 = 0.0
    c_input2 = 0.0


    def button_press(self, value):
        if value == "AC" or self.c_state == 'Result' or self.c_state == 'Error':
            self.entry_value.set('0')
            self.c_state = 'Input1'
            self.prev_value.set('')
            self.c_operation = 'None'
        if value == "AC":
            return

        entry_val = self.number_entry.get()
        if entry_val == '0' and value != '.':   # we don't want a 0 prefix, unless it is a decimal
            entry_val = value
        else:
            if entry_val == '' and value == '.':
                value = '0.'
            entry_val += value
        self.entry_value.set(entry_val)


    def isfloat(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:           
            return False


    def operation_button_press(self, value):
        if self.isfloat(str(self.number_entry.get())):
            self.c_operation = 'None'
            self.c_input1 = float(self.entry_value.get())    # error handling missing
            if value == "/":
                self.c_operation = "/"
            elif value == "*":
                self.c_operation = '*'
            elif value == "+":
                self.c_operation = '+'
            elif value == "-":
                self.c_operation = '-'
            else:
                print("Unknown command")
            self.entry_value.set("")      # clear display
            self.prev_value.set(str(self.c_input1)+' '+str(self.c_operation))
            self.c_state = 'Input2'
        else:
            print("Non-numeric first entry")


    def equal_button_press(self):  
        if self.c_operation != 'None':
            e_value = self.entry_value.get()
            if e_value != "" and self.isfloat(e_value):
                self.c_input2 = float(self.entry_value.get())
                if self.c_operation == '+':
                    solution = self.c_input1 + self.c_input2
                elif self.c_operation == '-':
                    solution = self.c_input1 - self.c_input2
                elif self.c_operation == '*':
                    solution = self.c_input1 * self.c_input2
                elif self.c_operation == '/':
                    solution = self.c_input1 / self.c_input2
                else:
                    print('Unknown operation')

                print(self.c_input1, " ", self.c_operation, ' ' , float(self.entry_value.get()), " ", solution)
                
                self.entry_value.set(solution)
                self.c_state = 'Result'
                self.prev_value.set(str(self.c_input1)+' '+self.c_operation+' '+str(self.c_input2)+' =')
            else:
                self.entry_value.set('ERR')
                self.c_state = 'Error'
                self.prev_value.set('')
        self.c_operation = 'None'

    # class constructor
    def __init__(self, root):
        self.entry_value = StringVar(root, value='0')    # new string object to interact with entry box
        self.prev_value = StringVar(root, value='')      # displays input1 and operation when in c_state Input2
        root.title("Calculator")
        root.geometry("860x440")
        root.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton", font="Serif 15", padding=15)
        style.configure("TEntry", font="Serif 24", padding=10)

        # ----- Top rows -----
        self.prev_input = ttk.Label(root, textvariable=self.prev_value).grid(row=0, column=3)
        
        self.button_clear = ttk.Button(root, text="AC", command=lambda: self.button_press('AC')).grid(row=1, column=0)

        self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=60, justify = tk.RIGHT)
        self.number_entry.grid(row=1, column = 1, columnspan=3)

        # ----- 1st Row -----
        self.button7 = ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=2, column=0)
        self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=2, column=1)
        self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=2, column=2)
        self.button_div = ttk.Button(root, text="/", command=lambda: self.operation_button_press('/')).grid(row=2, column=3)

        # ----- 2nd Row -----
        self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=3, column=0)
        self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=3, column=1)
        self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=3, column=2)
        self.button_mult = ttk.Button(root, text="*", command=lambda: self.operation_button_press('*')).grid(row=3, column=3)

        # ----- 3rd Row -----
        self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=4, column=0)
        self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=4, column=1)
        self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=4, column=2)
        self.button_add = ttk.Button(root, text="+", command=lambda: self.operation_button_press('+')).grid(row=4, column=3)

        # ----- 4th Row -----
        self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=5, column=0)
        self.button_decimal = ttk.Button(root, text=".", command=lambda: self.button_press('.')).grid(row=5, column=1)
        self.button_equal = ttk.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=5, column=2)
        self.button_sub = ttk.Button(root, text="-", command=lambda: self.operation_button_press('-')).grid(row=5, column=3)

# main code
root = Tk()

calc = Calculator(root)  # create instance of calculator object
root.mainloop()

# end of program