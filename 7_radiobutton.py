# 라디오 버튼: 여러 버튼 중에서 한 개씩 선택하는 것.
# 서로 다른 그룹의 라디오 버튼을 생성할 수도 있다.
from tkinter import *

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

# 버거
label1 = Label(root, text="메뉴를 선택하세요").pack()
burger_var = IntVar()  # 여기에 int혀응로 값을 저장
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()  # 기본적으로 선택되어이 있는 상태로 지정
btn_burger2 = Radiobutton(root, text="치즈햄버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨햄버거", value=3, variable=burger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

# 음료
label1 = Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()  # 기본값으로 선택
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btn_command():
    print(burger_var.get())  # 햄버거 중 선택된 라디오 항목의 값(value)를 출력
    print(drink_var.get())  # 음료 중 선택된 라디오 항목의 값(value)를 출력


btn = Button(root, text="주문하기", command=btn_command)
btn.pack()

root.mainloop()
