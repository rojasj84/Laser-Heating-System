import socket
import tkinter as tk

def laser_send_command(laser_ip, command_string):
    # TCP_IP = '192.168.1.100'
    TCP_PORT = '10001'
    buffer_size = 1024

    message = command_string + "/r"

    laser_ip_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    laser_ip_connection.connect(laser_ip, TCP_PORT)
    laser_ip_connection.send(message.encode())
    laser_dataread = laser_ip_connection.recv(1024).decode()
    laser_ip_connection.close()

    return laser_dataread

if __name__ == "__main__":
    
    mainwindow = tk.Tk()
    mainwindow.title("Laser Troubleshooting")
    mainwindow.config(width=475, height=250)

    emmission_on_button = tk.Button(mainwindow, text="Disable HW Emission Control", command=lambda: laser_send_command(laser_ip_textbox.get("1.0","end-1c"),"DLE")) 
    emmission_on_button.place(x=20, y=20, width=200, height=25)   

    emmission_on_button = tk.Button(mainwindow, text="Emission ON") 
    emmission_on_button.place(x=20, y=50, width=200, height=25)   

    emmission_off_button = tk.Button(mainwindow, text="Emission OFF") 
    emmission_off_button.place(x=20, y=80, width=200, height=25)

    laser_power_button = tk.Button(mainwindow, text="Set Laser Power") 
    laser_power_button.place(x=20, y=110, width=200, height=25)

    enable_external_control_button = tk.Button(mainwindow, text="Enable External Control") 
    enable_external_control_button.place(x=20, y=140, width=200, height=25)

    disable_external_control_button = tk.Button(mainwindow, text="Disable External Control") 
    disable_external_control_button.place(x=20, y=170, width=200, height=25)

    send_command_button = tk.Button(mainwindow, text="Send Command") 
    send_command_button.place(x=20, y=200, width=200, height=25)    

    laser_power_label = tk.Label(mainwindow, text="Laser Power")   
    laser_power_label.place(x=250, y = 10, width=200, height=20)

    laser_power_textbox = tk.Text(mainwindow)   
    laser_power_textbox.place(x=250, y=30, width=200, height=20)

    laser_ip_label = tk.Label(mainwindow, text="Laser IP")   
    laser_ip_label.place(x=250, y = 50, width=200, height=20)
    
    laser_ip_textbox = tk.Text(mainwindow)   
    laser_ip_textbox.place(x=250, y=70, width=200, height=20)

    text_command_label = tk.Label(mainwindow, text="Text Command")   
    text_command_label.place(x=250, y = 90, width=200, height=20)
    
    text_command_textbox = tk.Text(mainwindow)   
    text_command_textbox.place(x=250, y=110, width=200, height=20)
    
    laser_output_label = tk.Label(mainwindow, text="Laser Output")   
    laser_output_label.place(x=250, y = 130, width=200, height=20)

    laser_output_label_display = tk.Label(mainwindow, text="", bd = 1, relief=tk.SUNKEN)   
    laser_output_label_display.place(x=250, y = 150, width=200, height=20)

    mainwindow.mainloop()
