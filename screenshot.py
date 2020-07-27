import tkinter as tk, pyautogui

def takeShot():
    sc = pyautogui.screenshot()
    sc.save(r"c:\Users\Naser\Pictures\screenshot.png") #location of the scr shot

#create the canvas (window)#
root = tk.Tk()
canvas1 = tk.Canvas(root, width = 50, height = 50)
canvas1.pack()
###

#create the button#
button = tk.Button(text= "Snap!", command = takeShot, bg = 'black', fg = 'red', font=10)
canvas1.create_window(25,15,window = button)
####

root.mainloop()