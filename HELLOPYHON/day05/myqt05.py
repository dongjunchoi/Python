import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
from qtconsole.mainwindow import background
 
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt05.ui")[0]
 
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pb_click) 
    def pb_click(self):
#         b = self.le2.text()
        
        com=""
        rnd = random.randrange(1,3)
        if rnd == 1:
            com = "짝"
        elif rnd == 2:
            com ="홀"
        
        user = self.le1.text()
        res =""
        if user==com:
            res = "이겼습니다"
            self.le3.setStyleSheet("background-color : green")
        elif user > com:
            res = "졌습니다"
            self.le3.setStyleSheet("background-color : red")
            
        self.le2.setText(com)
        self.le3.setText(res)
        
    
       
#         self.pb.clicked.connect(self.pb_click)
#     def pb_click(self) :

#         print("pb_Click")
#         self.lbl.setText("good Evening");
 
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
 
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 
 
    #프로그램 화면을 보여주는 코드
    myWindow.show()
 
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()