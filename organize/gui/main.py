import sys
from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel


class Backend(QObject):

    @Slot(int, int, result=int)
    def select_folder_path(self, ):
        return 


app = QApplication(sys.argv)

view = QWebEngineView()

channel = QWebChannel()
backend = Backend()
channel.registerObject("backend", backend)

view.page().setWebChannel(channel)
view.load("file://" + sys.path[0] + "/index.html")

view.resize(600, 400)
view.show()

sys.exit(app.exec())