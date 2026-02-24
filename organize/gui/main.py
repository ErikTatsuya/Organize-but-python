import sys
from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import QFileDialog
from organize.core import organize, CATEGORIES
from PySide6.QtCore import QUrl
from pathlib import Path


class Backend(QObject):

    @Slot(result=str)
    def select_dir_path(self):
        dir_path = QFileDialog.getExistingDirectory(
            None,
            "Selecionar pasta"
        )
        return dir_path or ""
    
    @Slot(str)
    def organize_files(self, dir_path):
        if dir_path:
            organize(dir_path, CATEGORIES)


app = QApplication(sys.argv)

view = QWebEngineView()

channel = QWebChannel()
backend = Backend()
channel.registerObject("backend", backend)
view.page().setWebChannel(channel)

html_path = Path(__file__).parent / "index.html"
view.setUrl(QUrl.fromLocalFile(str(html_path)))

view.resize(600, 400)
view.show()

sys.exit(app.exec())