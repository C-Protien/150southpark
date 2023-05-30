from  tkinter import *
import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import cv2
import threading
import csv



root = tk.Tk()
root.geometry("700x700")
root.title("Method Study (Analyser ver 1.0)")



heading_label = tk.Label(root, text="Method Study Analysis Tool", font=('arial',30) , width=30 ,background='#E3BFBF')
heading_label.pack()

heading_label = tk.Label(root, text="Version 1.0", font=('arial',15) , background ='#DFE5B2')
heading_label.pack(pady= 20)

company_name_label = tk.Label(root, text="Company Name:", font=20)
company_name_label.pack()
company_name_entry = tk.Entry(root)
company_name_entry.pack(pady=5)

unit_name_label = tk.Label(root, text="Unit Name:", font=20)
unit_name_label.pack()
unit_name_entry = tk.Entry(root)
unit_name_entry.pack(pady=5)

operation_name_label = tk.Label(root, text="Operation Name:", font=20)
operation_name_label.pack()
operation_name_entry = tk.Entry(root)
operation_name_entry.pack(pady=5)

Machine_name_label = tk.Label(root, text="Machine:", font=20)
Machine_name_label.pack()
Machine_name_entry = tk.Entry(root)
Machine_name_entry.pack(pady=5)

video_path_label = tk.Label(root, text="Video Path:", font=20)
video_path_label.pack()
video_path_entry = tk.Entry(root)
video_path_entry.pack(pady=5)

# def analysis_complete_window():
#     complete_window = tk.Toplevel(root)
#     complete_window.geometry("300x100")
#     complete_window.title("Analysis Complete")
#     complete_label = tk.Label(complete_window, text="Analysis is Complete!")
#     complete_label.pack()
#     complete_window.mainloop()



def run_app():
    video_path = video_path_entry.get()
    # video_path = r"{}".format(video_path)
    os.environ['VIDEO_PATH'] = video_path

    cmd1 = [r"C:\Users\91999\AppData\Local\Programs\Python\Python37\python.exe", "app.py"]
    cmd2 = [r"C:\Users\91999\AppData\Local\Programs\Python\Python37\python.exe", r"C:\Users\91999\Documents\RP\Model test\Model 1\Application\Top - MTM - Right\hand-gesture-recognition-mediapipe-main\app.py" ]

    # r"C:\Users\91999\Documents\RP\Model test\Model 1\Application\Top - MTM - Right\hand-gesture-recognition-mediapipe-main\app.py"
    subprocess.call(cmd1)
    subprocess.call(cmd2)
    cmd3 = [r"C:\Users\91999\AppData\Local\Programs\Python\Python37\python.exe", "speed_extractor.py"]
    subprocess.call(cmd3)
     # speed_extractor_right
    cmd4 = [r"C:\Users\91999\AppData\Local\Programs\Python\Python37\python.exe", r"C:\Users\91999\Documents\RP\Model test\Model 1\Application\Top - MTM - Right\hand-gesture-recognition-mediapipe-main\speed_extractor.py"]
    subprocess.run(cmd4)
    # root.after(0, analysis_complete_window)









def browse_file():
    file_path = filedialog.askopenfilename()
    video_path_entry.delete(0, tk.END)
    video_path_entry.insert(0, file_path)


browse_button = tk.Button(root, text="Browse", command=browse_file ,  background='grey', width= 10 ,height=2, font=20)
browse_button.pack(pady=10)


pid = None
def submit():
    global pid

    company_name = company_name_entry.get()
    unit_name = unit_name_entry.get()
    operation_name = operation_name_entry.get()
    video_path = video_path_entry.get()
    machine_name = Machine_name_entry.get()

    if company_name and unit_name and operation_name and video_path:
        with open("Operation_details.csv",'w' ,newline='') as csv_file :
            writer = csv.writer(csv_file)
            writer.writerow(['Company_Name', 'Unit', 'Operation', 'Machine'])
            writer.writerow([str(company_name), str(unit_name), str(operation_name), str(machine_name)])
            start_label = tk.Label(root, text="Writing Details to file...", fg='green', font=20)
            start_label.pack()





        # video_length = get_video_length(video_path)
        # print(video_length)

        # start the script
        # cmd = [r"C:\Users\91999\AppData\Local\Programs\Python\Python37\python.exe", "app.py"]

        start_label = tk.Label(root, text="Starting Analysis...", fg='green' , font=20)
        start_label.pack(pady=20)
        start_label = tk.Label(root, text="Pressing 'Esc' on analysis windows will end process", fg='red', font=20)
        start_label.pack()

        # destroy the window after 2 seconds
        root.after(2000, root.destroy)


        app_thread = threading.Thread(target=run_app)
        app_thread.start()





    else:
        error_message = "Please fill in all four input fields."
        error_label = tk.Label(root, text=error_message, fg="red", font=20)
        error_label.pack()



def get_video_length(video_path):
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return length



# def quit_program():
#     global pid
#     os.kill(pid, signal.SIGTERM)
#     root.destroy()



submit_button = tk.Button(root, text="Start Analysis", command=submit,background='#DCEEAE' , width= 20 ,height=2, font=20)
submit_button.pack(pady=20)

# exit_button = tk.Button(root, text="Exit", command=quit_program)
# exit_button.pack()

root.mainloop()

# root2.mainloop()
