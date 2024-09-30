import tkinter as tk
from tkinter import filedialog

class LogoDisplay(tk.Frame):
    def __init__(self, x_position, y_position):
        tk.Frame.__init__(self)

        #Frame visual configuration
        self.configure(width=1260,height=40,background="White", highlightbackground="black", highlightthickness=1)

        #Frame position information
        self.x_position = x_position
        self.y_position = y_position
        self.place(x = self.x_position, y = self.y_position)

        #Set logo
        self.logotext = tk.Label(self, text="High T : Acton-PIXIS 400", font=('Helvetica', 20), background="White")
        self.logotext.place(x = 5, y = 0, width=1250, height=35)


class FileSelection(tk.Frame):
    def __init__(self, x_position, y_position):
        tk.Frame.__init__(self)
        
        #Frame visual configuration
        self.configure(width=320,height=290,background="White", highlightbackground="black", highlightthickness=1)
        
        #Frame position information
        self.x_position = x_position
        self.y_position = y_position
        self.place(x = self.x_position, y = self.y_position)

        #Frame buttons and labels
        self.select_lightfield_spectra = tk.Button(self, text="Select Lightfield Spectra", font=('Helvetica', 10), command=lambda: self.file_open_dialog(1))
        self.select_lightfield_spectra.place(x = 10, y = 10, width=300, height = 30)
        self.selected_lightfield_spectra = tk.Text(self, font=('Helvetica', 10), highlightbackground="black", highlightthickness=0, background="Light Gray")
        self.selected_lightfield_spectra.place(x = 10, y = 50, width=300, height = 50)

        self.select_folder_to_save_tfit = tk.Button(self, text="Select Folder for T-fit", font=('Helvetica', 10), command=lambda: self.file_open_dialog(2))
        self.select_folder_to_save_tfit.place(x = 10, y = 110, width=300, height = 30)
        self.selected_folder_to_save_tfit = tk.Text(self, font=('Helvetica', 10), highlightbackground="black", highlightthickness=0, background="Light Gray")
        self.selected_folder_to_save_tfit.place(x = 10, y = 150, width=300, height = 50)

        self.enter_output_filename = tk.Label(self, text="Enter output filename", font=('Helvetica', 10))
        self.enter_output_filename.place(x = 10, y = 210, width=300, height = 30)
        self.entered_output_filename = tk.Text(self, font=('Helvetica', 10), highlightbackground="black", highlightthickness=0, background="Light Gray")
        self.entered_output_filename.place(x = 10, y = 240, width=300, height = 30)

    def file_open_dialog(self, file_location_number):
        #Differentiates between the light field spectra and the t-rax folder
        if file_location_number == 1:
            self.open_file_path = filedialog.askopenfilename()
            #print(open_file_name)
            self.selected_lightfield_spectra.delete("1.0",tk.END)
            self.selected_lightfield_spectra.insert(tk.END, self.open_file_path)
        elif file_location_number == 2:
            self.open_folder_path = filedialog.askdirectory()
            #print(open_file_name)
            self.selected_folder_to_save_tfit.delete("1.0",tk.END)
            self.selected_folder_to_save_tfit.insert(tk.END, self.open_folder_path)
            
        
class CalibrationFileSelection(tk.Frame):
    def __init__(self, x_position, y_position):
        tk.Frame.__init__(self)

        #Frame visual configuration
        self.configure(width=320,height=600,background="White", highlightbackground="black", highlightthickness=1)
        
        #Frame position information
        self.x_position = x_position
        self.y_position = y_position
        self.place(x = self.x_position, y = self.y_position)
    
class TransmissionFilterSelection(tk.Frame):
    def __init__(self, x_position, y_position):
        tk.Frame.__init__(self)

        #Frame visual configuration
        self.configure(width=930,height=900,background="White", highlightbackground="black", highlightthickness=1)
        
        #Frame position information
        self.x_position = x_position
        self.y_position = y_position
        self.place(x = self.x_position, y = self.y_position)

        self.select_one_transmission_filter_logo = tk.Label(self, text = "Select One Transmission Filter", font=('Helvetica', 15), background="White")
        self.select_one_transmission_filter_logo.place(x=5,y=5, width=920, height=30)

        self.select_one_transmission_filter_logo = tk.Label(self, text = "Select Iris Status", font=('Helvetica', 15), background="White")
        self.select_one_transmission_filter_logo.place(x=5,y=135, width=920, height=30)
        
        # Filter Determination Raio Buttons for the Left Side
        
        self.filter_variable_left = tk.IntVar()
        self.iris_variable_left = tk.IntVar()

        self.left_no_filter_selection = tk.Radiobutton(self,text="NO FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 1000, selectcolor="Light Blue", background="Light Blue")
        self.left_no_filter_selection.place(x=30, y = 50, width=90, height=30)
        self.left_no_filter_selection.select()

        self.left_700_filter_selection = tk.Radiobutton(self,text="70% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 700, selectcolor="Light Blue", background="Light Blue")
        self.left_700_filter_selection.place(x=130, y = 50, width=90, height=30)

        self.left_500_filter_selection = tk.Radiobutton(self,text="50% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 500, selectcolor="Light Blue", background="Light Blue")
        self.left_500_filter_selection.place(x=230, y = 50, width=90, height=30)

        self.left_350_filter_selection = tk.Radiobutton(self,text="35% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 350, selectcolor="Light Blue", background="Light Blue")
        self.left_350_filter_selection.place(x=330, y = 50, width=90, height=30)
        
        self.left_100_filter_selection = tk.Radiobutton(self,text="10% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 100, selectcolor="Light Blue", background="Light Blue")
        self.left_100_filter_selection.place(x=30, y = 90, width=90, height=30)

        self.left_070_filter_selection = tk.Radiobutton(self,text="7% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 70, selectcolor="Light Blue", background="Light Blue")
        self.left_070_filter_selection.place(x=130, y = 90, width=90, height=30)

        self.left_050_filter_selection = tk.Radiobutton(self,text="5% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 50, selectcolor="Light Blue", background="Light Blue")
        self.left_050_filter_selection.place(x=230, y = 90, width=90, height=30)

        self.left_035_filter_selection = tk.Radiobutton(self,text="3.5% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_left, value = 35, selectcolor="Light Blue", background="Light Blue")
        self.left_035_filter_selection.place(x=330, y = 90, width=90, height=30)

        self.left_iris_selection = tk.Radiobutton(self, text = "Iris Out", font=('Helvetica', 12), indicatoron=0, variable=self.iris_variable_left, value = 1, selectcolor="Light Blue", background="Light Blue")
        self.left_iris_selection.place(x = 130, y = 160, width=90, height=50)
        
        self.left_iris_selection = tk.Radiobutton(self, text = "Iris In", font=('Helvetica', 12), indicatoron=0, variable=self.iris_variable_left, value = 0, selectcolor="Light Blue", background="Light Blue")
        self.left_iris_selection.place(x = 230, y = 160, width=90, height=50)

        # Filter Determination Raio Buttons for the Right Side
        
        self.filter_variable_right = tk.IntVar()
        self.iris_variable_right = tk.IntVar()

        self.right_no_filter_selection = tk.Radiobutton(self,text="NO FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 1000, selectcolor="Pink", background="Pink")
        self.right_no_filter_selection.place(x=930-90-330, y = 50, width=90, height=30)
        self.right_no_filter_selection.select()

        self.right_700_filter_selection = tk.Radiobutton(self,text="70% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 700, selectcolor="Pink", background="Pink")
        self.right_700_filter_selection.place(x=930-90-230, y = 50, width=90, height=30)

        self.right_500_filter_selection = tk.Radiobutton(self,text="50% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 500, selectcolor="Pink", background="Pink")
        self.right_500_filter_selection.place(x=930-90-130, y = 50, width=90, height=30)

        self.right_350_filter_selection = tk.Radiobutton(self,text="35% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 350, selectcolor="Pink", background="Pink")
        self.right_350_filter_selection.place(x=930-90-30, y = 50, width=90, height=30)
        
        self.right_100_filter_selection = tk.Radiobutton(self,text="10% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 100, selectcolor="Pink", background="Pink")
        self.right_100_filter_selection.place(x=930-90-330, y = 90, width=90, height=30)

        self.right_070_filter_selection = tk.Radiobutton(self,text="7% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 70, selectcolor="Pink", background="Pink")
        self.right_070_filter_selection.place(x=930-90-230, y = 90, width=90, height=30)

        self.right_050_filter_selection = tk.Radiobutton(self,text="5% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 50, selectcolor="Pink", background="Pink")
        self.right_050_filter_selection.place(x=930-90-130, y = 90, width=90, height=30)

        self.right_035_filter_selection = tk.Radiobutton(self,text="3.5% FILTER", font=('Helvetica', 10), indicatoron = 0, variable = self.filter_variable_right, value = 35, selectcolor="Pink", background="Pink")
        self.right_035_filter_selection.place(x=930-90-30, y = 90, width=90, height=30)

        self.right_iris_selection = tk.Radiobutton(self, text = "Iris Out", font=('Helvetica', 12), indicatoron=0, variable=self.iris_variable_right, value = 1, selectcolor="Pink", background="Pink")
        self.right_iris_selection.place(x = 930-90-230, y = 160, width=90, height=50)
        
        self.right_iris_selection = tk.Radiobutton(self, text = "Iris In", font=('Helvetica', 12), indicatoron=0, variable=self.iris_variable_right, value = 0, selectcolor="Pink", background="Pink")
        self.right_iris_selection.place(x = 930-90-130, y = 160, width=90, height=50)



if __name__ == "__main__":
    mainwindow = tk.Tk()
    mainwindow.geometry('1280x1000')
    mainwindow.title("High T: Acton-PIXIS 400")

    Logo = LogoDisplay(10,10)
    OpenFile = FileSelection(10, 60)
    CalibrationFile = CalibrationFileSelection(10, 360)
    TransmissionFilter = TransmissionFilterSelection (340, 60)


    mainwindow.mainloop()