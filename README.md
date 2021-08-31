# GUI Programming Python(Tkinter)

Exercise for GUI programming with Python's Tkinter

**youtube의 강의를 따라하여 파이썬의 Tkinter로 GUI 프로그래밍에 대해서 배운다.**

[파이썬 코딩 무료 강의(활용편2)-GUI 프로그래밍을 배우고 '여러 이미지 합치기' 프로그램을 함께 만들어요.[나도코딩]](https://www.youtube.com/watch?v=bKPIcoou9N8)


## python 파일 설명
  * **1_create-frame** : 기본적인 창(프레임)을 생성한다.
  * **2_button** : 다양한 형태/색상의 버튼을 생성한다.
    * **btn_image** : 버튼을 생성할 때 해당 이미지로 생성할 수 있다.
  * **3_label** : 레이블 (이미지나 텍스트)를 표시하는 기능 + ```.config```를 통해서 해당 레이블을 변경할 수 있다.
    * **btn_image2** : btn_image를 레이블로 설정하고, 해당 이미지 변경시킬 수 있다.
  * **3_label_ttk** : 원래의 파일에 ttk 모듈을 ```import```시켜서 조금 변형시켜봤다.  ```compound```, ```image=''```, label에 대해서 width조정, label 배열 정렬 타입 설정, 글씨체 설정, 라벨과 배경색 설정도 가능하다. (참고: [네이버 블로그 gaussian37](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=infoefficien&logNo=221057243324))
  * **4_text_empty** : txt와 entry 상자를 만들어서 글자를 입력 받고, delete를 통해서 지울 수도 있는 기능을 만든다.
  * **5_listbox** : listbox를 생성한다. 
  * **6_checkbox** : checkbox를 생성한다.
  * **6_checkbox_응용** : checkbox 원본을 살짝 변형시켜보았다.
  * **7_radiobutton** : 여러 버튼 중에서 한 개씩 선택하는 radiobutton을 생성 / 서로 다른 구릅의 라디오 버튼을 생성
  * **8_combobox_1** : combobox 생성 (combobox 내에 문자 입력 가능하다)
  * **8_combobox_2** : combobox 생성 (combobox 내에 문자 입력 불가능 처리)
  * **9_progressbar_1** : progress bar(점점 차오르는 막대)를 생성 ("중지" 버튼으로 종료되도록 처리)
  * **9_progressbar_2** : progress bar는 "시작"버튼으로 시작되고, 퍼센티를 출력
  * **10_menu** : 메뉴창 생성
  * **11_msgbox** : 팝업을 뜨는 다양한 메시지 박스 생성
  * **12_frame** : 프레임 생성
  * **13_scrollbar** : 스크롤바 생성. ```yscrollcommand=scrollbar.set```과 ```scrollbar.config(command.listbox.yview)``` 둘 다 반드시 있어야 제대로 작동
  * **14_grid_1_calculator** : ```14_grid_keyboard.JPG```의 형태로 생성 - 1 __ 버튼과 그리드를 생성한다.
  * **14_grid_1_calculator** : ```14_grid_keyboard.JPG```의 형태로 생성 - 2 __ 버튼 크기 일정하게, 그리드 여유 크기 생성, ```sticky```로 행/열로 몇 줄 
