__author__ = 'robby'

from Tkinter import *

import mancala

class MancalaBoard(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.pack(expand=YES, fill=BOTH)
        self.master.title('Mancala')
        self.master.iconname("mancala")


        square_entry_frame = Frame(self).pack(side=TOP, expand=YES, fill=BOTH)

        Label(square_entry_frame, text="Number of Squares", fg='black', font=("arial", 10, "bold"), width=20, bg='gray40').pack(
            side=LEFT, expand=YES, fill=BOTH)

        number_of_squares_display = StringVar()
        Entry(square_entry_frame, relief=SUNKEN, textvariable=number_of_squares_display).pack(side=RIGHT, expand=YES,
                                                                                                fill=BOTH)

        player_frame = Frame(self).pack(side=BOTTOM, expand=YES, fill=BOTH)
        Label(player_frame, text="Player 1", fg='black', font=("arial", 10, "bold"), width=20, bg='gray40').pack(
            side=LEFT, expand=YES, fill=BOTH)
        Label(player_frame, text="Player 2", fg='black', font=("arial", 10, "bold"), width=20, bg='gray40').pack(
            side=LEFT, expand=YES, fill=BOTH)

        # number_of_squares_display = StringVar()
        # square_entry_frame.pack(side=TOP)
        # start_button = button(self, BOTTOM, "Start Game")



        # Entry(self, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)
        # frame = frame(root, CENTER)


    def create_board(self, board_size=4):
        self.board = mancala.Mancala(board_size=board_size)

def start(self):
    self.root.mainloop()

def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Simple Calculator')
        self.master.iconname("calc1")
        display = StringVar()
        Entry(self, relief=SUNKEN,
        textvariable=display).pack(side=TOP, expand=YES,
        fill=BOTH)

        for key in ("123", "456", "789", "-0."):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, LEFT, char, lambda w=display, s=' %s '%char: w.set(w.get()+s))

        opsF = frame(self, TOP)
        for char in "+-*/=":
            if char == '=':
                btn = button(opsF, LEFT, char)
                btn.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
            else:
                btn = button(opsF, LEFT, char, lambda w=display, c=char: w.set(w.get()+' '+c+' '))

        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, 'Clr', lambda w=display: w.set(''))

    def calc(self, display):
        try:
            display.set(`eval(display.get())`)
        except ValueError:
            display.set("ERROR")


if __name__ == '__main__':
    MancalaBoard().mainloop()
