from tkinter import *

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)  # listbox나 scrollbar모두 똑같은 frame에 들어간다
# scrollbar.pack(side="right")  # fill이 없으면 스크롤바가 이상하게 생성된다.
scrollbar.pack(side="right", fill="y")

# yscrollcommand: 스크롤이 위아래로 움직인다.
# scrollbar.set에서 set이 없다면 스크롤이 다시 위로 올라간다.
# 대신 config를 통해서 list와 mapping이 필요하다.
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):  # 1~31일
    listbox.insert(END, str(i) + "일")  # 1일, 2일 ...
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)  # 상하 움직임에 대해서 매칭이 된다.

root.mainloop()
