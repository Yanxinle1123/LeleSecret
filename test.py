import tkinter as tk


def on_button_click():
    # 取消选中所有选项
    print(vars)
    for var in vars.values():
        var.set(0)
    # 选中"选项2"
    vars["选项2"].set(1)


root = tk.Tk()
root.title("示例")

options = ["选项1", "选项2", "选项3"]
vars = {option: tk.IntVar() for option in options}
check_buttons = [tk.Checkbutton(root, text=option, variable=vars[option]) for option in options]
for check_button in check_buttons:
    check_button.pack()

button = tk.Button(root, text="改变选中值", command=on_button_click)
button.pack()

root.mainloop()
