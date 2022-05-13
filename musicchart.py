
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import requests     #파이썬으로 웹페이지 연결
from bs4 import BeautifulSoup as bs  #분석을 용이하게
import pandas as pd      #데이터 분석 관련 모듈



form_class = uic.loadUiType("musicchart.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #버튼 클릭 인식해서 btn_clicked 매서드를 호출
        self.pushButton.clicked.connect(self.btn_clicked)  #벅스 조회 단추

    def btn_clicked(self): #벅스 조회 매소드
        # print("버튼 클릭")
        chart_list=[]
        rank = 1

        html = requests.get('https://music.bugs.co.kr/chart')  #페이지 소스 읽어오기 (site에다가 직접 소스요청)
        soup = bs(html.text)  #소스에서 텍스트만 추출

        titles = soup.select('p.title > a')   #노래제목 100곡 
        singers = soup.select('p.artist > a')  #가수 100명

        for each in range(len(soup.select('p.title > a'))):   #100곡 반복
            title = titles[each].text.strip()
            singer = singers[each].text.strip()
            chart_list.append(['Bugs',rank,title,singer])
            rank += 1


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()