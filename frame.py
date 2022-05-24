from re import I
import tkinter
import customtkinter

class TKFrame:
    def __init__(self, app_width, app_height, backg, title):
        self.window = tkinter.Tk()
        self.window.geometry(f'{app_width}x{app_height}')
        self.window.config(bg=backg)
        self.window.title(title)

    def start(self):
        pass

class CTKFrame:
    def __init__(self, app_width, app_height, backg, title, text):
        customtkinter.set_appearance_mode(backg)
        customtkinter.set_default_color_theme('blue')

        self.window = customtkinter.CTk()
        self.window.geometry(f'{app_width}x{app_height}')
        self.window.title(title)

    def start(self):
        pass

class SuccessWindow:
    def __init__(self, app_width, app_height, backg, title, line):
        self.window = tkinter.Tk()
        self.window.geometry(f'{app_width}x{app_height}')
        self.window.config(bg=backg)
        self.window.title(title)

        self.image = tkinter.PhotoImage(file=)

        self.success_label = tkinter.Label(
            self.window,
            text=line,
            bg='black',
            font=('Courier', 12, 'bold')
            fg='green',
            image=self.image
        )

        self.success_label.place(anchor=tkinter.CENTER)
        self.window.mainloop()

class ErrorWindow:
    def __init__(self, app_width, app_height, bgcol, title, line):
        self.window = tkinter.Tk()
        self.window.geometry(f'{app_width}x{app_height}')
        self.window.config(bg=bgcol)
        self.window.title(title)

        self.image = tkinter.PhotoImage(file=)

        self.success_label = tkinter.Label(
            self.window,
            text=line,
            bg='black',
            font=('Courier', 12, 'bold')
            fg='red',
            image=self.image
        )

        self.success_label.place(anchor=tkinter.CENTER)
        self.window.mainloop()