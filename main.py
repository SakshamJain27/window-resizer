from tkinter import *
root = Tk()
root.title("My Window")

def change():
    root.geometry(f"{width.get()}x{height.get()}")

height = StringVar()
width = StringVar()

Label(root, text="Window resizer").grid(column=2)

Label(root, text="Height:").grid(row=1, column=1)
Entry(root, textvariable=height).grid(row=1, columnspan=2, column=2)

Label(root, text="Width:").grid(row=2, column=1)
Entry(root, textvariable=width).grid(row=2, columnspan=2, column=2)

Button(root, text="Resize", command=change).grid(row=3, column=2)
root.mainloop()
