
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# from PyQt5.QtCore import *
# from matplotlib import artist

import requests     #파이썬으로 웹페이지 연결
from bs4 import BeautifulSoup as bs  #분석을 용이하게
import pandas as pd      #데이터 분석 관련 모듈

from selenium import webdriver   #사이트에 직접 요청하는것이 아닌 로컬에 이미 저장된 소스를 가지고옴


form_class = uic.loadUiType("musicchart.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #버튼 클릭 인식해서 btn_clicked 매서드를 호출
        self.pushButton.clicked.connect(self.btn_clicked)  #벅스 조회 단추
        self.pushButton_2.clicked.connect(self.btn_clicked_2)  #멜론 조회 단추
        self.pushButton_3.clicked.connect(self.btn_clicked_3)  #지니 조회 단추

    def btn_clicked(self): #벅스 조회 매소드
        # print("버튼 클릭")
        # chart_list=[]
        rank = 1

        html = requests.get('https://music.bugs.co.kr/chart')  #페이지 소스 읽어오기 (site에다가 직접 소스요청)
        soup = bs(html.text)  #소스에서 텍스트만 추출

        titles = soup.select('p.title > a')   #노래제목 100곡 
        singers = soup.select('p.artist > a')  #가수 100명

        for each in range(len(soup.select('p.title > a'))):   #100곡 반복

            self.tableWidget.resizeColumnsToContents()

            title = titles[each].text.strip()
            singer = singers[each].text.strip()

            # self.tableWidget.setItem(행,열,값) #문법
            self.tableWidget.setItem(each, 0, QTableWidgetItem("벅스"))
            self.tableWidget.setItem(each, 1, QTableWidgetItem(str(rank)))
            self.tableWidget.setItem(each, 2, QTableWidgetItem(title))
            self.tableWidget.setItem(each, 3, QTableWidgetItem(singer))
            
            rank += 1

        # self.lineEdit.setText(soup.select('strong.current')[0].text.strip()[5:])

    def btn_clicked_2(self): #멜론 조회 매소드
        # print("버튼 클릭")
        # song_data = []
        rank = 1

        driver = webdriver.Chrome('chromedriver.exe')    #크롬 브라우저 띄우기
        driver.get('https://www.melon.com/chart/')  #사이트 연결
        html = driver.page_source  

        soup = bs(html)

        songs = soup.select('tbody > tr')  #100개 곡 가지고 옴
        # singers = soup.select('td.point')  #영화 평점 44개

        for song in songs:  #100번 반복
            self.tableWidget.resizeColumnsToContents()

            title = song.select('div.ellipsis.rank01 > span > a')[0].text
            singer = song.select('div.ellipsis.rank02 > span > a')[0].text
            self.tableWidget.setItem(rank - 1, 0, QTableWidgetItem("멜론"))
            self.tableWidget.setItem(rank - 1, 1, QTableWidgetItem(str(rank)))
            self.tableWidget.setItem(rank - 1, 2, QTableWidgetItem(title))
            self.tableWidget.setItem(rank - 1, 3, QTableWidgetItem(singer))

            
            rank += 1



    def btn_clicked_3(self): #지니 조회 매소드
        # print("버튼 클릭")

        # song_data = []
        rank = 1

        driver = webdriver.Chrome('chromedriver.exe')    #크롬 브라우저 띄우기
        driver.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220516&hh=20&rtm=Y&pg=1')  #사이트 연결(1~50)
        html = driver.page_source   #소스 읽어오기
        soup = bs(html)

        songs = soup.select('tr.list')

        for song in songs:
            self.tableWidget.resizeColumnsToContents()

            title = song.select('a.title.ellipsis')[0].text.strip()
            singer = song.select('a.artist.ellipsis')[0].text.strip()
            self.tableWidget.setItem(rank - 1, 0, QTableWidgetItem("지니"))
            self.tableWidget.setItem(rank - 1, 1, QTableWidgetItem(str(rank)))
            self.tableWidget.setItem(rank - 1, 2, QTableWidgetItem(title))
            self.tableWidget.setItem(rank - 1, 3, QTableWidgetItem(singer))        
            rank += 1


        driver.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220516&hh=20&rtm=Y&pg=2')  #사이트 연결(1~50)
        html = driver.page_source   #소스 읽어오기
        soup = bs(html)
        songs = soup.select('tr.list')

        for song in songs:
            self.tableWidget.resizeColumnsToContents()

            title = song.select('a.title.ellipsis')[0].text.strip()
            singer = song.select('a.artist.ellipsis')[0].text.strip()
            self.tableWidget.setItem(rank - 1, 0, QTableWidgetItem("지니"))
            self.tableWidget.setItem(rank - 1, 1, QTableWidgetItem(str(rank)))
            self.tableWidget.setItem(rank - 1, 2, QTableWidgetItem(title))
            self.tableWidget.setItem(rank - 1, 3, QTableWidgetItem(singer))        
            rank += 1



app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()