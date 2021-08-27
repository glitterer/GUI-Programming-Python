from tkinter import *

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

root.resizable(False, False)  # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가 시키기)

root.mainloop()
