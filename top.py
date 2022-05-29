from tkinter import *
import tkinter as tk
import videoTester




def btn_clicked():

    print("Button Clicked ")
    # new_window= tk.TopLevel(window)
    # app = videoTester(new_window)

def btn_clicked_scan_image():
        print("Button Clicked scan Image")
        videoTester.scan_image()

def btn_clicked_add_member():
    print("button clicked add member")

top = Tk()
top.title("Home Security Main")
top.iconbitmap("D:\GitHub\FaceRecognition_Neha/home.ico")

top.geometry("1518x1080")
top.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1080,
    width = 1518,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    759.0, 540.0,
    image=background_img)

#Scan face Button
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat",
    command = btn_clicked_scan_image)

b0.place(
    x = 845, y = 741,
    width = 551,
    height = 81)

#Train Model
# img1 = PhotoImage(file = f"img1.png")
# b1 = Button(
#     image = img1,
#     borderwidth = 0,
#     highlightthickness = 0,
#     command = btn_clicked,
#     relief = "flat")
#
# b1.place(
#     x = 845, y = 606,
#     width = 551,
#     height = 81)

#Add Member
img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked_add_member,
    relief = "flat")

b2.place(
    x = 845, y = 461,
    width = 551,
    height = 81)

top.resizable(True, True)
window.mainloop()
