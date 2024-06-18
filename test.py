import tkinter as tk


def on_command_comma(event):
    print("Command+comma pressed")


root = tk.Tk()

root.bind('<Command-comma>', on_command_comma)

root.mainloop()
