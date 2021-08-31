from tkinter import *
from tkinter import ttk

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

values_1 = [str(i) + "일" for i in range(1, 32)]  #1~31까지의 숫자를 반환
combobox = ttk.Combobox(root, height=5, values = values_1)  # height로 목록에 보이는 갯수를 지정
combobox.pack()
combobox.set("카드 결제일")  #최초 목록 제목 설정 + 버튼 클릭을 통한 값 설정도 가능

#state를 추가한 combobox
readonly_combobox = ttk.Combobox(root, height=10, values = values_1, state="readonly")  # 사용자가 직접 입력은 불가능
readonly_combobox.current(0)  #0번째 인덱스 값 선택
readonly_combobox.pack()


def btn_command():
    print(combobox.get())  #선택된 값 표기
    print(readonly_combobox.get())

btn = Button(root, text="선택하기", command=btn_command)
btn.pack()

root.mainloop()
