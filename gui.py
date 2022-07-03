from tkinter import *

class SuccessWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('400x400')
        self.window.config(bg='black')
        self.window.title('Success!')

        self.image = PhotoImage(file='Success.png')

        self.success_img = Label(
            self.window,
            image=self.image,
            bg='black'
        )

        self.success_lbl = Label(
            self.window,
            text='Success!',
            bg='black',
            font=('Times', 20, 'bold'),
            fg='green',
        )

        self.success_img.place(x=80, y=35)
        self.success_lbl.place(x=155, y=300)
        self.window.mainloop()

class ErrorWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry(f'400x400')
        self.window.config(bg='black')
        self.window.title('Error!')

        self.image = PhotoImage(file='Error.png')

        self.error = Label(
            self.window,
            bg='black',
            image=self.image
        )

        self.error_lbl = Label(
            self.window,
            text='Error!',
            font=('Times', 20, 'bold'),
            bg='black',
            fg='red'
        )

        self.error.place(x=80, y=35)
        self.error_lbl.place(x=160, y=300)
        self.window.mainloop()