from tkinter import *

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표


#리스트 박스
#selectmode = single / extended (한개 선택 / 여러 개 선택 가능)
#height: 0이면 list가 포함하는 만큼 다 볼 수 있다 VS 1 이상은 보이고자 하는 list 갯수 -->scrollbar는 다른 방법으로 생성 가능
listbox = Listbox(root, selectmode = "extended", height = 0)
listbox.insert(0, "사과")  #0번째에 "사과"가 입력
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")  # END=가장 마지막에 입력
listbox.insert(END, "포도")
listbox.pack()

def btn_command():
    # listbox.delete(END)  #맨 뒤의 항목을 삭제한다.
    # listbox.delete(0)  #맨 앞의 항목을 삭제한다.

    #갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    #항목 확인(시작index, 끝index)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    #선택된 항목 확인(위치로 반환)
    print("선택된 항목 : ", listbox.curselection())  # 선택된 항목이 index값으로 출력해준다.

btn = Button(root, text="클릭", command=btn_command)
btn.pack()

root.mainloop()
