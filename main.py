import turtle

try:                        
    import tkinter as tk    
except:
    import tkinter as tk
from PIL import Image, ImageTk


if __name__ == '__main__':
    root = tk.Tk()

    label = tk.Label(root)
    img = Image.open(r"background.jpg")
    label.img = ImageTk.PhotoImage(img)
    label['image'] = label.img

    label.pack()
    root.mainloop()