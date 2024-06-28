import tkinter

from LeleEasyTkinter.easy_check_button import EasyCheckButton


def on_button_click():
    fruit_check_button.set(["苹果(默认)", "橙子(默认)"])


root = tkinter.Tk()
root.title("示例")

fruit_check_button = EasyCheckButton(root,
                                     text=["苹果(默认)", "香蕉(默认)", "橙子(默认)", "葡萄", "梨子(默认)", "榴莲",
                                           "荔枝", "草莓", "柚子", "樱桃", "杏子", "菠萝", "西瓜"],
                                     set_=["苹果(默认)", "梨子(默认)", "橙子(默认)", "香蕉(默认)"],
                                     expand=tkinter.YES)

button = tkinter.Button(root, text="改变选中值", command=on_button_click)
button.pack()

root.mainloop()
