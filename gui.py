from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, IntVar, Checkbutton
from pathlib import Path
from functions import generate_and_show, copy_to_clipboard, password_mask
import authentication

def login_success(username):
    print("Welcome, " + username + "!")

def register_or_login():
    while True:
        user_choice = input("Do you want to (r)egister or (l)ogin? ")
        if user_choice.lower() == 'r':
            authentication.register_user()
        elif user_choice.lower() == 'l':
            username = authentication.login_user()
            if username:
                login_success(username)
                break
        else:
            print("Invalid input. Please enter 'r' for register or 'l' for login.")

register_or_login()

# define functions
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# define constants
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\MARCO\Desktop\build\assets\frame0")

# set up the main window
window = Tk()
window.title("PassGen")
window.iconbitmap("C:/Users/MARCO/Desktop/build/18_icon-icons.com_73792.ico")
window.geometry("477x300")
window.configure(bg = "#FFFFFF")
window.resizable(False, False)

# create canvas
canvas = Canvas(
    window, bg = "#FFFFFF", 
    height = 300, width = 477, 
    bd = 0, highlightthickness = 0, 
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

# draw on canvas
canvas.create_rectangle(
    0.0, 
    0.0, 
    140.0, 
    300.0, 
    fill="#990011", 
    outline="")

canvas.create_rectangle(
    274.0, 
    62.0, 
    374.0, 
    162.0, 
    fill="#D9D9D9", 
    outline="")

canvas.create_rectangle(
    140.0, 
    0.0, 
    477.0, 
    300.0, 
    fill="#990011", 
    outline="")

canvas.create_rectangle(
    147.0, 
    8.0, 
    470.0, 
    293.0, 
    fill="#FCF6F5", 
    outline="")

# add texts on canvas
canvas.create_text(
    16.0, 
    8.0, 
    anchor="nw", 
    text="PassGen", 
    fill="#FCF6F5", 
    font=("GenosRoman Regular", 30 * -1)
)

canvas.create_text(
    164.0, 
    10.0, 
    anchor="nw", 
    text="Generator", 
    fill="#990011", 
    font=("GenosRoman Regular", 28 * -1)
)

canvas.create_text(
    169.0, 
    73.0, 
    anchor="nw", 
    text="Password Length:", 
    fill="#990011", 
    font=("GenosRoman Regular", 20 * -1)
)

canvas.create_text(
    169.0, 
    169.0, 
    anchor="nw", 
    text="Generated Password:", 
    fill="#990011", 
    font=("GenosRoman Regular", 20 * -1)
)

canvas.create_text(
    169.0, 
    220.0, 
    anchor="nw", 
    text="Strength:", 
    fill="#990011", 
    font=("GenosRoman Regular", 16 * -1)
)

# password strength label
strength_label = Label(window, text = "", bg = "#FCF6F5", fg = "#990011", font = ("GenosRoman Regular", 8))
strength_label.place(x = 240.0, y = 220.0)

# password length entry
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(305.5, 111.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#DEDEDE", fg="#000716", highlightthickness=0)
entry_2.place(x=174.0, y=99.0, width=263.0, height=22.0)

# generated password entry
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(304.5, 207.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#DEDEDE", fg="#000716", highlightthickness=0)
entry_1.place(x=173.0, y=195.0, width=263.0, height=22.0)

# generate button
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, relief="flat")
button_1.place(x=366.0, y=130.0, width=77.0, height=27.0)
button_1.configure(command=lambda: generate_and_show(entry_2, entry_1, strength_label, symbols_var.get(), digits_var.get()))

# copy to clipboard button
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, relief="flat")
button_2.place(x=366.0, y=225.0, width=77.0, height=27.0)
button_2.configure(command=lambda: copy_to_clipboard(entry_1))

# checkboxes
mask_var = IntVar()
symbols_var = IntVar()
digits_var = IntVar()
mask_checkbox = Checkbutton(window, text='Mask password', variable=mask_var, command=lambda: password_mask(entry_1, mask_var), bg="#FCF6F5", fg="#990011")
mask_checkbox.place(x=165, y=240)
symbols_checkbox = Checkbutton(window, text='!-)', variable=symbols_var, bg="#FCF6F5", fg="#990011")
symbols_checkbox.place(x=165, y=130)
digits_checkbox = Checkbutton(window, text='0-9', variable=digits_var, bg="#FCF6F5", fg="#990011")
digits_checkbox.place(x=215, y=130)

# start the application
window.mainloop()
