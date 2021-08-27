from tkinter import *

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

btn1 = Button(root, text="버틴1")  # 버튼 생성하기
btn1.pack()  # 실제로 버튼을 window에 포함을 시킨다.

btn2 = Button(root, padx=5, pady=10, text = "버튼2222222")  # 제목에 따라서 버튼의 크기가 달라질 수 있다. / 버튼의 여백설정
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text = "버튼3")
btn3.pack()

btn4 = Button(root, width = 10, height=3, text = "버튼4")  # 버튼의 크기가 정해져있다.
btn4.pack()

btn5 = Button(root, fg = "red", bg="yellow", text = "버튼5")  # 버튼의 크기가 정해져있다.
btn5.pack()

photo = PhotoImage(file = "btn_image.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():  #버튼이 클릭되었을 때 실행이 되는 함수
    print("버튼이 클릭되었습니다.")
btn7 = Button(root, text="active button", command=btncmd)  # 버튼을 클릭하면 무언가 실행이 되도록 한다.
btn7.pack()

root.mainloop()
