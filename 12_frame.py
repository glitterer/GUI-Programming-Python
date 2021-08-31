# 프레임을 만들어서 각각 위젯을 프레임에 집어넣기
# pack() 내의 옵션을 통해서 위치/펼치는 옵션 등 다루기

from tkinter import *

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

Label(root, text="메뉴를 선택해주세요").pack(side="top")  #위쪽에 배치한 레이블

Button(root, text="주문하기").pack(side = "bottom")

#burger frame
frame_burger = Frame(root, relief="solid", bd=1)  # relief: 테두리 모양
frame_burger.pack(side="left", fill="both", expand=True)  #side: 위치 배열, fill:꽉 채우는 것

Button(frame_burger, text = "햄버거").pack()
Button(frame_burger, text = "치즈버거").pack()
Button(frame_burger, text = "치킨버거").pack()

#drink frame
frame_drink = LabelFrame(root, text="음료") # 제목이 있는 frame
frame_drink.pack(side = "right", fill="both", expand=True)
Button(frame_drink, text = "콜라").pack()
Button(frame_drink, text = "사이다").pack()

root.mainloop()
