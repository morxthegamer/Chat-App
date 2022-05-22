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
    def __init__(self, app_width, app_height, backg, title):
        customtkinter.set_appearance_mode(backg)
        customtkinter.set_default_color_theme('blue')

        self.window = customtkinter.CTk()
        self.window.geometry(f'{app_width}x{app_height}')
        self.window.title(title)

    def start(self):
        pass