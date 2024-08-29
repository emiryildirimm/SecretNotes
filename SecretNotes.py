from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

def save_to_file():
    title = title_entry.get()
    content = secret_text.get("1.0", 'end-1c')
    if title and content :
        with open("secret notes.txt", "a") as file:
            file.write(title+ "\n" + content + "\n")
        messagebox.showinfo("Success", "Content saved to secret notes.txt")
    else:
        messagebox.showwarning("Warning", "Entry field is empty")

def encrypt_secret():
    print("Hello World")

def save_and_encrypt():
    save_to_file()
    encrypt_secret()

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

secret_text = Text(root, height=10, width=20)
secret_text.pack()
secret_text.place(x=160, y=300)

encrypt_and_save_button = Button(root, text="Encrypt&Save", command=save_and_encrypt)
encrypt_and_save_button.pack()
encrypt_and_save_button.place(x=180, y=660)

decrypt_button = Button(root, text="Decrypt")
decrypt_button.pack()
decrypt_button.place(x=200, y=700)

root.mainloop()