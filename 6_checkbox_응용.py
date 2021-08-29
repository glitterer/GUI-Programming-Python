from tkinter import *

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

chkvar = IntVar()  # chkvar에 int형으로 값을 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select()  # 기본으로 check가 선택되어있는 상태로 바뀐다.
# chkbox.deselect()  # 선택 해제 처리한다.
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "일주일동안 보지 않기", variable = chkvar2)
chkbox2.pack()

def btn_command():
    if chkvar.get() == 1: # 체크 박스의 상태를 출력... 0: 체크 해제, 1: 체크
        print("오늘 하루 동안 보지 않기로 체크 되어있습니다.")
    else:
        print("오늘 하루 동안 보지 않기가 체크되어있지 않습니다. 따라서 오늘 하루동안 봅니다.")

    if chkvar2.get() == 1:
        print("일주일동안 보지 않기로 체크되어있습니다.")
    else:
        print("일주일동안 보지 않기가 체크되어있지 않습니다. 따라서 일주일동안 봅니다.")
    print()
btn = Button(root, text="클릭", command=btn_command)
btn.pack()

root.mainloop()
