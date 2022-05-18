import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


import requests     #파이썬으로 웹페이지 연결
from bs4 import BeautifulSoup as bs  #분석을 용이하게
import pandas as pd      #데이터 분석 관련 모듈
from datetime import datetime, timedelta, timezone
from selenium import webdriver   #사이트에 직접 요청하는것이 아닌 로컬에 이미 저장된 소스를 가지고옴

form_class = uic.loadUiType("ppvs.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #버튼 클릭 인식해서 btn_clicked 매서드를 호출
        self.pushButton.clicked.connect(self.btn_clicked)  #onejav 조회 단추
        # self.pushButton_2.clicked.connect(self.btn_clicked_2)  #141ppv 조회 단추

    def btn_clicked(self):
        rank = 1

        # datetime_utc = datetime.utcnow()

        # timezone_kst = timezone(timedelta(hours=9))
        # datetime_kst = datetime_utc.astimezone(timezone_kst).strftime("%Y-%m-%d %H:%M:%S")

        # print(datetime_kst)


        html = requests.get('https://onejav.com/search/PPV?page=1')
        soup = bs(html.text)

        ppvs = soup.select('div.card.mb-3')

        for ppv in ppvs:
            self.tableWidget.resizeColumnsToContents()
            title = ppv.select('h5.is-spaced > a')[0].text.strip()
            date = ppv.select('p.is-6 > a')[0].text.strip()
            self.tableWidget.setItem(ppv - 1, 0, QTableWidgetItem("onejav"))

            self.tableWidget.setItem(ppv - 1, 1, QTableWidgetItem(title))
            self.tableWidget.setItem(ppv - 1, 2, QTableWidgetItem(date))
            rank += 1

        html = requests.get('https://onejav.com/search/PPV?page=2')
        soup = bs(html.text)
        ppvs = soup.select('div.card.mb-3')

        for ppv in ppvs:
            self.tableWidget.resizeColumnsToContents()
            title = ppv.select('h5.is-spaced > a')[0].text.strip()
            date = ppv.select('p.is-6 > a')[0].text.strip()
            self.tableWidget.setItem(ppv - 1, 0, QTableWidgetItem("onejav"))
            self.tableWidget.setItem(ppv - 1, 1, QTableWidgetItem(str(rank)))
            self.tableWidget.setItem(ppv - 1, 2, QTableWidgetItem(title))
            self.tableWidget.setItem(ppv - 1, 3, QTableWidgetItem(date))
            rank += 1

        html = requests.get('https://onejav.com/search/PPV?page=3')
        soup = bs(html.text)
        ppvs = soup.select('div.card.mb-3')

        for ppv in ppvs:
            self.tableWidget.resizeColumnsToContents()
            title = ppv.select('h5.is-spaced > a')[0].text.strip()
            date = ppv.select('p.is-6 > a')[0].text.strip()
            self.tableWidget.setItem(ppv - 1, 0, QTableWidgetItem("onejav"))
            self.tableWidget.setItem(ppv - 1, 1, QTableWidgetItem(str(rank)))
            self.tableWidget.setItem(ppv - 1, 2, QTableWidgetItem(title))
            self.tableWidget.setItem(ppv - 1, 3, QTableWidgetItem(date))
            rank += 1














app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()






