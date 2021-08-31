# 진행상태를 알려주는 progress bar
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

# indeterminate<->determinate
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")

progressbar.start(10)  # 10ms 마다 움직임 / progressbar가 시작한다.
progressbar.pack()


def btn_command():
    progressbar.stop()  # 작동 중지


btn = Button(root, text="중지", command=btn_command)
btn.pack()

root.mainloop()
