from tkinter import *

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

txt = Text(root, width=30, height=5)  # textbox(텍스트 위젯)이 찾 내에 생겨서 텍스트 입력이 가능하다.
txt.pack()

txt.insert(END, "글자를 입력하세요")  # textbox에 텍스트를 입력한다. (미리 글자가 들어가있다.)

e =Entry(root, width=30)  #entrybox가 textbox 밑에 생성된다. --> entry는 한 줄로만 받을 수 있다 (eg.id/pw받을 때)
e.pack()
e.insert(0, "insert only in one line")  # 0 대신 END 입력 가능하다.==>현재는 값이 비어있으므로

def btn_command():
    print(txt.get("1.0", END))  #처음부터 끝까지의 모든 텍스트 내용을 가져온다(1번 줄부터 column기준으로 0번째 index에서부터 가져와라)
    print(e.get())  # Entry에 있는 값도 가져온다.

    txt.delete("1.0", END)  # 모든 내용 삭제(txt에 대해서)
    e.delete(0, END)  # 모든 내용 삭제(ENTRY에 대해서)
btn = Button(root, text="클릭", command=btn_command)
btn.pack()

root.mainloop()
