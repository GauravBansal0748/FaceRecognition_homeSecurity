from tkinter import *
import tkinter as tk
import videoTester
import pyttsx3
import videotoimg
import config


# get_key function to check whether the given key exist or not
def get_key(val):
    for key, value in config.name.items():
        if val == value:
            return True


# function activated when ADD MEMBER is pressed
def btn_clicked_add_member():
    print("button clicked add member")
    videotoimg.subject = entry0.get()  # Saves the entered name into the subject variable
    videotoimg.add_member()
    videotoimg.train_model()


# function activated when SCAN IMAGE is pressed
def btn_clicked_scan_image():
    print("Button Clicked scan Image")
    videoTester.scan_image()


# function to extract name from the Tkinter Textbox
def name_get():
    return entry0.get()


# Below Function called when SUBMIT button is pressed
def open():
    global canvas, background_img, background, img0, b0, img1, b1, img2, b2
    print("Name Entered:" + entry0.get())
    videotoimg.subject = entry0.get()
    # Tkinter Second Window with Scan Face and Add Member Button
    top = Toplevel()
    top.title("Home Security Main")
    top.iconbitmap("D:\GitHub\FaceRecognition_homeSecurity/home_icon.ico")
    top.geometry("1518x1080")
    top.configure(bg="#ffffff")

    # Sets Canvas in UI
    canvas = Canvas(
        top,
        bg="#ffffff",
        height=1080,
        width=1518,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    # Background in UI
    background_img = PhotoImage(file=f"background.png")
    background = canvas.create_image(
        759.0, 540.0,
        image=background_img)

    # Scan face Button
    img0 = PhotoImage(file=f"img0.png")
    b0 = Button(top,
                image=img0,
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                command=btn_clicked_scan_image)
    b0.place(
        x=845, y=606,
        width=551,
        height=81)

    # Add Member
    img2 = PhotoImage(file=f"img2.png")
    b2 = Button(top,
                image=img2,
                borderwidth=0,
                highlightthickness=0,
                command=btn_clicked_add_member,
                relief="flat")
    b2.place(
        x=845, y=461,
        width=551,
        height=81)

    top.resizable(True, True)


# Tkinter First Window with Name Textbox and Submit Button
window = Tk()

window.title("Home Security")
window.iconbitmap("D:\GitHub\FaceRecognition_homeSecurity/home_icon.ico")
window.geometry("500x446")
window.configure(bg="#e2e1e2")
# Tkinter Canvas
canvas = Canvas(
    window,
    bg="#e2e1e2",
    height=446,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

# NAME TextBox
entry0_img = PhotoImage(file=f"img_textBox01.png")
entry0_bg = canvas.create_image(
    245.0, 305.0,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)
entry0.place(
    x=65.0, y=278,
    width=360.0,
    height=52)

# SUBMIT Button
img0 = PhotoImage(file=f"img01.png")
b0 = Button(window,
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=open,
            relief="flat")
b0.place(
    x=159, y=370,
    width=192,
    height=57)

# Tkinter First Window Background
background_img = PhotoImage(file=f"background01.png")
background = canvas.create_image(
    250.0, 153.5,
    image=background_img)

window.resizable(True, True)
window.mainloop()
