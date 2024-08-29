from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

def save_to_file():
    content = title_entry.get()
    if content:
        with open("secret notes.txt", "w") as file:
            file.write(content)
        messagebox.showinfo("Success", "Content saved to secret notes.txt")
    else:
        messagebox.showwarning("Warning", "Entry field is empty")

root = Tk()

root.title("Secret Notes")
root.configure(background="white")
root.minsize(200, 200)
root.maxsize(500,900)
root.geometry("500x800")

image = PhotoImage(file="Untitled.png")
image_label = Label(root, image=image)
image_label.pack()
image_label.place(x=150, y=15)

text = Label(root, text="You can give me a secret!", font='Impact 12')
text.pack()
text.place(x=140, y=180)

title_label = Label(root, text="Enter Your Secret's Title!")
title_label.pack()
title_label.place(x=160, y=220)

title_entry = Entry(root)
title_entry.pack()
title_entry.place(x=160, y=250)

save_button = Button(root, text="Save", command=save_to_file)
save_button.pack()
save_button.place(x=200, y=700)

root.mainloop()