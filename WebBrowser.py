from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QVBoxLayout,QHBoxLayout,QPushButton,QStyle,QTabWidget
from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class Window_browser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.setWindowTitle("iWeb - Browse the World")
        self.setStyleSheet("background-color:rgb(53, 54, 58); color:Black;")
        self.setGeometry(100,50,1200,630)
        horizontalBox = QHBoxLayout()
        self.tabcontoller = QTabWidget()
        horizontalBox.addWidget(self.tabcontoller)
        self.tab_maker()
        self.tab_maker()
        self.setLayout(horizontalBox)
        self.show()
    
    def tab_maker(self):
        self.tabcontoller.addTab(Browser(),"New Tab")

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        # Create a search url widget
        self.search_url = QLineEdit()
        self.search_url.setStyleSheet("background-color:black; color:white; border-radius:14px; margin:0px,10px,0px,10px; border:2px solid grey; padding: 2px 10px 2px 10px; font-weight:bold;")
        self.search_url.setFont(QtGui.QFont("sans-serif",11))
        self.search_url.setPlaceholderText("Search in Google or Type a URL")
        self.search_url.setMinimumWidth(500)
        self.search_url.returnPressed.connect(self.webb)
        self.search_url.setEnabled(True)
        self.search_url.setAlignment(Qt.AlignCenter)

        # Create a vbox
        vbox = QVBoxLayout()
        
        # Back Button
        self.back_button = QPushButton()
        self.back_button.setIcon(self.style().standardIcon(QStyle.SP_ArrowBack))
        self.back_button.setEnabled(False)
        self.back_button.clicked.connect(self.go_back)

        # forword Button
        self.forword_button = QPushButton()
        self.forword_button.setIcon(self.style().standardIcon(QStyle.SP_ArrowForward))
        self.forword_button.clicked.connect(self.go_fast)

        # Reload Button
        self.reload_button = QPushButton()
        self.reload_button.setIcon(self.style().standardIcon(QStyle.SP_BrowserReload))
        self.reload_button.clicked.connect(self.go_reload_buton)

        # Reload Button
        self.stop_button = QPushButton()
        self.stop_button.setIcon(self.style().standardIcon(QStyle.SP_BrowserStop))
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.go_stop_button)


        # Create a Hbox
        hbox = QHBoxLayout()
        hbox.addWidget(self.back_button)
        hbox.addWidget(self.forword_button)
        hbox.addWidget(self.reload_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.search_url)

        self.web = QWebEngineView()
        self.web.load(QUrl(f"https://google.com/"))
        self.web.show()
        vbox.addLayout(hbox)
        vbox.addWidget(self.web)
        self.setLayout(vbox)
        self.show()
    
    def webb(self):
        self.stop_button.setEnabled(True)
        self.back_button.setEnabled(True)
        if 'http://' or 'https://' not in self.search_url:
            self.web.load(QUrl(f"https://{self.search_url.text()}/"))
            self.web.show()

        else:
            self.web.load(QUrl(self.search_url.text()))
            self.web.show()
        

    def go_back(self):
        self.web.back()

    def go_fast(self):
        self.web.forward()
    
    def go_reload_buton(self):
        self.web.reload()

    def go_stop_button(self):
        self.web.stop()
        

if __name__ == "__main__":
    App = QApplication(sys.argv)
    browser = Window_browser()
    sys.exit(App.exec())