from tkinter import *

root = Tk()
root.title("first GUI from python")  # 창의 이름
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

label1 = Label(root, text="This is the experiment of the label")  # 창에서 는 레이블
label1.pack()

photo = PhotoImage(file="btn_image.png")  # 이미지를 받아온다.
label2 = Label(root, image=photo)  # 레이블로 이미지를 사용한다.
label2.pack()


def change():  # button에 대한 command
    label1.config(text="Change the label by the change function")  # label1을 변경하기 위해서 .config를 사용한다.

    global photo2
    photo2 = PhotoImage(file="btn_image2.png")  #  get photo image as photo2 variable
    label2.config(image=photo2)  # configure label2 to image which is photo2

btn = Button(root, text="Click to change label and image", command=change)  # 버튼을 생성하고, change함수를 처리한다.
btn.pack()

root.mainloop()
