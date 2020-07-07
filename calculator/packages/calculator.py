from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        self.string = ''
        self.fontConfig = ('Verdana', 14)


        self.entryText(0, 0)

        self.button('7',1,0)
        self.button('8',1,1)
        self.button('9',1,2)

        self.button('4',2,0)
        self.button('5',2,1)
        self.button('6',2,2)

        self.button('3',3,0)
        self.button('2',3,1)
        self.button('1',3,2)

        self.button('0',4,0)

        self.button('+', 1, 3)
        self.button('-', 1, 4)
        self.button('*', 2, 3)
        self.button('/', 2, 4)

        self.button('(', 3, 3)
        self.button(')', 3, 4)

        self.buttonClear('C', 4, 1)
        self.buttonRemove('<', 4,2)
        self.buttonEqual('=', 4, 3)



    def button(self, _char,_x,_y):
        self.b =Button(
            self.master, text=_char, width=4, height=1,
            font=self.fontConfig, command=lambda: self.buttonClick(_char))
        
        self.b.grid(row=_x,column=_y)
   
    def entryText(self,_x,_y):
        self.entry = Text(
            self.master, font=self.fontConfig,
            width=20, height=2, state=DISABLED
        )
        
        self.entry.grid(row=_x,column=_y,columnspan=5, sticky='we')

    def buttonEqual(self,_char,_x,_y):
        self.b = Button(
            self.master, text = _char, width=4, height=1, 
            font=self.fontConfig, command=self.buttonEqualClick
        )        
        self.b.grid(row=_x, column=_y,sticky='we', columnspan=2)
    
    def buttonRemove(self, _char, _x, _y):
        self.b = Button(
            self.master, text=_char, width=4, height= 1,
            font = self.fontConfig, command =self.buttonRemoverClick 
        )
        self.b.grid(row=_x, column=_y)
    
    def buttonClear(self, _char, _x, _y ):
        self.b = Button(
            self.master, text=_char, width=4, height= 1,
            font = self.fontConfig, command =self.buttonClearClick 
        )
        self.b.grid(row=_x, column=_y)
    
    def display(self, _text):
        self.entry.config(state=NORMAL)
        self.entry.delete('1.0',END)
        self.entry.insert('1.0', _text)
        self.entry.config(state=DISABLED)

    def buttonClick(self, _text):
        self.string = '' + self.string + _text
        self.display(self.string)
    
    def buttonEqualClick(self):
        self.display(eval(self.string))
        self.string=''
    
    def buttonRemoverClick(self):
        self.string=''+self.string[0:-1]
        self.display(self.string)
    
    def buttonClearClick(self):
        self.display('')
        self.string = ''


