import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import io

from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog

win_color = 'light gray'
light_win_color = "white"

class OptionTabs(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Variables for the gauge

        #Variables for displaying
        self.config(border=2, bg = "Black", relief=tk.FLAT)
        self.place(x = 2, y = 2, width = 1195, height = 895)

        noteStyler = ttk.Style()
        noteStyler.configure("TNotebook", borderwidth=0, background="White")
        tab_parent = ttk.Notebook(self, style = 'TNotebook')
               
        #Populating the tabs with their own frame classses
        avantes_in_gas = AvantesInGaAS(tab_parent)
        acton_pixis = ActonPixisTab(tab_parent)
        
        
        tab_parent.pack(expand=1, fill='both')

    def browse_directory(window_on_top):
        directory_location = filedialog.askdirectory(parent = window_on_top, initialdir = "/")
        print(directory_location)

#Create Classes to fill the tabs
class ActonPixisTab(tk.Frame):
    def __init__(self, Parent):
        super().__init__(Parent)

        Parent.add(self, text="High T: Acton-PIXIS 400")
        self.config(bg="White")

        # Populating the spectra files
        label_logo = tk.Label(self, text="High T: Acton-PIXIS 400", bg=light_win_color, font=("Arial", 25)).place(x = 5, y = 5, width = 380)

        frames_around_fileshandling = tk.Frame(self, highlightbackground="black", highlightthickness=1, background=light_win_color).place(x=5, y = 50, width = 380, height = 220)
        
        # Select Avantes Spectra Folder widgets
        folder_select_label = tk.Label(self, text="Select Avantes Spectra Folder", bg=light_win_color, font=("Arial", 15)).place(x = 15, y = 60)
        folder_select_text = tk.Text(self, bg=win_color).place(x=15, y = 90, height=30,width=250)
        folder_select_button = tk.Button(self, text="SELECT", font=("Arial", 15)).place(x=270,y = 90, height=30,width=100)

        # Select Folder to save T-Fit widgets
        t_fit_save_label = tk.Label(self, text="Select Folder to save T-Fit", bg=light_win_color, font=("Arial", 15)).place(x = 10, y = 130)
        t_fit_save_text = tk.Text(self, bg=win_color).place(x=15,y = 160, height=30,width=250)
        t_fit_save_button = tk.Button(self, text="SELECT", font=("Arial", 15)).place(x=270,y = 160, height=30,width=100)

        # Filename output widgets
        output_filename_label = tk.Label(self, text="Enter output filename", bg=light_win_color, font=("Arial", 15)).place(x = 15, y = 200)
        output_filename_text = tk.Text(self, bg=win_color).place(x=15,y = 230, height=30,width=250)
        output_filename_button = tk.Button(self, text="SAVE", font=("Arial", 15)).place(x=270,y = 230, height=30,width=100) 


        #Frame around the Calibration Temperature
        frames_around_fileshandling = tk.Frame(self, highlightbackground="black", highlightthickness=1, background=light_win_color).place(x=5, y = 300, width = 380, height = 400)
    
class AvantesInGaAS(tk.Frame):
    def __init__(self, Parent):
        super().__init__(Parent)

        Parent.add(self, text="Low T: Avantes-InGaAS")
        self.config(bg=light_win_color)

        # Populating the spectra files
        self.label_logo = tk.Label(self, text="Low T: Avantes-InGaAS", bg=light_win_color, font=("Arial", 25)).place(x = 5, y = 5, width = 380)

        self.frames_around_fileshandling = tk.Frame(self, highlightbackground="black", highlightthickness=1, background=light_win_color).place(x=5, y = 50, width = 380, height = 220)
        
        # Select Avantes Spectra Folder widgets
        self.folder_select_label = tk.Label(self, text="Select Avantes Spectra Folder", bg=light_win_color, font=("Arial", 15)).place(x = 15, y = 60)
        self.folder_select_text = tk.Text(self, bg=win_color).place(x=15, y = 90, height=30,width=250)
        self.folder_select_button = tk.Button(self, text="SELECT", font=("Arial", 15), command= lambda: OptionTabs.browse_directory(self)).place(x=270,y = 90, height=30,width=100)

        # Select Folder to save T-Fit widgets
        self.t_fit_save_label = tk.Label(self, text="Select Folder to save T-Fit", bg=light_win_color, font=("Arial", 15)).place(x = 10, y = 130)
        self.t_fit_save_text = tk.Text(self, bg=win_color).place(x=15,y = 160, height=30,width=250)
        self.t_fit_save_button = tk.Button(self, text="SELECT", font=("Arial", 15)).place(x=270,y = 160, height=30,width=100)

        # Filename output widgets
        self.output_filename_label = tk.Label(self, text="Enter output filename", bg=light_win_color, font=("Arial", 15)).place(x = 15, y = 200)
        self.output_filename_text = tk.Text(self, bg=win_color).place(x=15,y = 230, height=30,width=250)
        self.output_filename_button = tk.Button(self, text="SAVE", font=("Arial", 15)).place(x=270,y = 230, height=30,width=100)       

        #Frame around the Calibration Temperature
        self.frames_around_fileshandling = tk.Frame(self, highlightbackground="black", highlightthickness=1, background=light_win_color).place(x=5, y = 300, width = 380, height = 450)

        image_test = ImageTk.PhotoImage(generate_graph_image())
        self.test_label = tk.Label(self, image=image_test)
        self.test_label.image = image_test
        self.test_label.place(x = 425, y = 5)

def generate_graph_image():
    xpoints = np.arange(0, 5, 0.1)
    ypoints = np.sin(xpoints)
    
    fig = plt.figure(figsize=(7, 5))
    plt.subplot(2, 2, 1)
    plt.xlabel("Wavelength", fontsize = 10)
    plt.ylabel("Count")
    plt.title('LEFT SIDE RAW')
    # plt.grid(True)    
    plt.scatter(xpoints, ypoints)
    
    plt.subplot(2, 2, 2)
    plt.xlabel("Wavelength", fontsize = 10)
    plt.ylabel("Count")
    plt.title('RIGHT SIDE RAW')
    plt.scatter(xpoints, ypoints)

    plt.subplot(2, 2, 3)
    plt.xlabel("Wavelength", fontsize = 10)
    plt.ylabel("Count")
    plt.title('LEFT SIDE FIT')
    plt.plot(xpoints, ypoints)

    plt.subplot(2, 2, 4)
    plt.xlabel("Wavelength", fontsize = 10)
    plt.ylabel("Count")
    plt.title('RIGHT SIDE FIT')
    plt.plot(xpoints, ypoints)
    
    plt.tight_layout()
    # plt.show()

    """Convert a Matplotlib figure to a PIL Image and return it"""
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img          

    win_color = 'light gray'
    light_win_color = "white"

if __name__ == "__main__":

    # Creating the main window
    window = tk.Tk()
    window.title('Laser Heating Controls')
    window.geometry('1200x900')
    window.configure(bg=win_color)

    spectrometer_data_window = OptionTabs(window)    

    window.mainloop()
