import tkinter

class SuccessWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry('400x400')
        self.window.config(bg='black')
        self.window.title('Success!')

        self.image = tkinter.PhotoImage(file='Success.png')

        self.success_img = tkinter.Label(
            self.window,
            image=self.image,
            bg='black'
        )

        self.success_lbl = tkinter.Label(
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
        self.window = tkinter.Tk()
        self.window.geometry(f'400x400')
        self.window.config(bg='black')
        self.window.title('Error!')

        self.image = tkinter.PhotoImage(file='Error.png')

        self.error = tkinter.Label(
            self.window,
            bg='black',
            image=self.image
        )

        self.error_lbl = tkinter.Label(
            self.window,
            text='Error!',
            font=('Times', 20, 'bold'),
            bg='black',
            fg='red'
        )

        self.error.place(x=80, y=35)
        self.error_lbl.place(x=160, y=300)
        self.window.mainloop()

wind1 = SuccessWindow()
wind2 = ErrorWindow()