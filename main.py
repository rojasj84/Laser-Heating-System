# Importing libraries
import tkinter as tk
from tkinter import ttk

# Importing local .py files
from spectrometerdatadisplay import *
# Defining functions for use in the program

#Create Classes    

class PiezoControl(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        # configure the root window
        self.title('Optical Stage Controls')
        self.geometry('600x900')
        self.configure(bg=win_color)

        x = 0

class SpectrometerDataDisplay(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        # configure the root window
        self.title('Spectrometer Data Display')
        self.geometry('1200x900')
        self.configure(bg=win_color)


        # call from Classes from spectrometerdatadisplay.py
        spectrometer_tabs = OptionTabs(self)

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Laser Heating Controls')
        self.geometry('400x600')
        self.configure(bg=win_color)
        
        menubar = tk.Menu(self, relief=tk.RAISED, bg = light_win_color)
        filemenu = tk.Menu(menubar, tearoff=0,relief=tk.RAISED,bg=light_win_color)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.config(menu=menubar)

        spectrometer_data_button = tk.Button(self, text = "Data Display", command=self.call_spectrometer_window).place(x = 20,y = 200, width=200)
        motor_control_button = tk.Button(self, text="Motor Control Button", command=self.call_motor_control_window).place(x = 20, y = 250, width=200)

        # spectrometer_tabs_window = SpectrometerDataDisplay(self)

    def call_spectrometer_window(self):
        spectrometer_data_window = SpectrometerDataDisplay(self)

    def call_motor_control_window(self):
        motor_control_window = PiezoControl(self)

if __name__ == "__main__":
    win_color = 'light gray'
    light_win_color = "white"

    # Creating the main window
    window = MainWindow()    

    window.mainloop()
