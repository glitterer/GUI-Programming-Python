from tkinter import *

root = Tk()
root.title("first GUI from python")
root.geometry("640x480+500+100")  # 가로크기 * 세로크기 + x좌표 + y좌표

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)
#File menu
menu_file = Menu(menu, tearoff=0)  #file menu 생성
menu_file.add_command(label="New File", command=create_new_file) #동작 시, 함수 호출 
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")  #비활성화 시키기
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)  #root.quit로 프로그램 종료가 가능하다.
menu.add_cascade(label="File", menu=menu_file)  #큰 file이라는 메뉴에 위의 내용들이 정의된다.

# Edit menu_file
menu.add_cascade(label = "Edit")

#language menu 추가(radio button을 통해서 택 1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label = "Python")
menu_lang.add_radiobutton(label = "Java")
menu_lang.add_radiobutton(label = "C++")
menu.add_cascade(label = "Language", menu=menu_lang)

#View 메뉴/checkbutton(여러 개 체크 가능)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="Show All")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)
root.mainloop()
