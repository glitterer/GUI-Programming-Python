#  ttk.Label을 이용한 GUI 라벨 지정하기
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=infoefficien&logNo=221057243324을 기초로 응용
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("first GUI from python")  # 창의 이름
# root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

label1 = ttk.Label(
    root, text="This is the experiment of the label")  # 창에서 는 레이블
label1.pack()

photo1 = PhotoImage(file="btn_image.png")  # 이미지를 받아온다.
label2 = ttk.Label(root, image=photo1)  # 레이블로 이미지를 사용한다.
label2.pack()


def change():  # button에 대한 command
    # label1을 변경하기 위해서 .config를 사용한다.
    label1.config(text="Change the label by the change function.\nGUI programming\nYAY!")
    label1.config(wraplength=1000)   # wraplength로 width가 조정이 된다.
    label1.config(justify=CENTER)  # .config(justify = LEFT/CENTER/RIGHT) ==> label 배열 정렬 타입
    label1.config(font = ('Arial', 18, 'bold'))  # config(font = ('글씨체', 폰트 사이즈, 옵션)) ==> 글씨체 수정
    label1.config(foreground = 'red', background = 'yellow')  #  foreground:라벨색,  background:배경색

    global photo2
    # get photo image as photo2 variable
    photo2 = PhotoImage(file="btn_image2.png")
    label1.img = PhotoImage(file = "btn_image2.png")
    # configure label2 to image which is photo2
    # compound = 'top'/'bottom'/'right'/'left' ==> 이미지가 text의 어느 곳에 배치할지 정한다.
    label1.config(image=photo2, compound = "right")
    label2.config(image = '')  #label2로 넣었던 이미지를 삭제한다.


# 버튼을 생성하고, change함수를 처리한다.
btn = Button(root, text="Click to change label and image", command=change)
btn.pack()

root.mainloop()
