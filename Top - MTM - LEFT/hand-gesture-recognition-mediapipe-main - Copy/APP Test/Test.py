import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import time
import pyautogui
import cv2


root = tk.Tk()
root.geometry("400x400")
root.title("Video Processor")

company_name_label = tk.Label(root, text="Company Name:")
company_name_label.pack()
company_name_entry = tk.Entry(root)
company_name_entry.pack()

unit_name_label = tk.Label(root, text="Unit Name:")
unit_name_label.pack()
unit_name_entry = tk.Entry(root)
unit_name_entry.pack()

operation_name_label = tk.Label(root, text="Operation Name:")
operation_name_label.pack()
operation_name_entry = tk.Entry(root)
operation_name_entry.pack()

video_path_label = tk.Label(root, text="Video Path:")
video_path_label.pack()
video_path_entry = tk.Entry(root)
video_path_entry.pack()


def browse_file():
    file_path = filedialog.askopenfilename()
    video_path_entry.delete(0, tk.END)
    video_path_entry.insert(0, file_path)


browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()


def submit():
    global process
    company_name = company_name_entry.get()
    unit_name = unit_name_entry.get()
    operation_name = operation_name_entry.get()
    video_path = video_path_entry.get()

    if company_name and unit_name and operation_name and video_path:
        video_length = get_video_length(video_path)
        print(video_length)

        # start the script
        cmd = ["python", "app.py", company_name, unit_name, operation_name, video_path]
        process = subprocess.Popen(cmd)

        # wait for the length of the video file
        root.after(int(video_length * 1000), pyautogui.press, 'esc')

        # send "ESC" key press event
        pyautogui.press('esc')

        # terminate the script
        process.terminate()
    else:
        error_message = "Please fill in all four input fields."
        error_label = tk.Label(root, text=error_message, fg="red")
        error_label.pack()



def get_video_length(video_path):
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length



def quit_program():

    subprocess.Popen.terminate(process)
    root.destroy()



submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

exit_button = tk.Button(root, text="Exit", command=quit_program)
exit_button.pack()

root.mainloop()
