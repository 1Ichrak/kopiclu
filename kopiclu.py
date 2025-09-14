import pyperclip, time
import tkinter as tk
import keyboard

def show_flash(message):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.geometry("200x100+800+400")  # position (x=800, y=400)
    label = tk.Label(root, text=message, font=("Arial", 16), fg="white", bg="black")
    label.pack(expand=True, fill="both")
    root.after(700, root.destroy)  # disappears after 0.7s
    root.mainloop()

last_clipboard = ""  # store previous clipboard content

while True:
    try:
        # --- COPY detection ---
        current_clipboard = pyperclip.paste()
        if current_clipboard != last_clipboard and current_clipboard.strip() != "":
            show_flash("Copied!")
            last_clipboard = current_clipboard

        # --- PASTE detection ---
        if keyboard.is_pressed("ctrl+v"):
            if pyperclip.paste().strip() != "":
                show_flash("Pasted!")
                time.sleep(0.5)  # avoid double trigger

        time.sleep(0.2)  # check 5 times per second

    except Exception:
        time.sleep(0.5)