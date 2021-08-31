# 진행상태를 알려주는 progress bar
from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

p_var2 = DoubleVar()  # percentage는 정수값으로 올라가지 않기 때문에 실수를 반영
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btn_command():
    for i in range(101):
        time.sleep(0.01)  # 0.01초 대기

        p_var2.set(i)  # 0~100까지 올라가는 것을 볼 수 있다.
        # UI의 시각적인 변화를 알기 위해서 udpate()를 사용한다.
        progressbar2.update()# 없으면, 실행 시, 순식간에 progressbar가 찬다.
        print(p_var2.get())  # 현재 값을 가져온다.(지금 percentage가 얼마인지)


btn = Button(root, text="시작", command=btn_command)
btn.pack()

root.mainloop()
