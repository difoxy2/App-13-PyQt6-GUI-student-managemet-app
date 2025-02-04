from PyQt6.QtWidgets import QDialog,QVBoxLayout,QPushButton,QLineEdit
from PyQt6.QtCore import Qt

class SearchDialog(QDialog):
    def __init__(self, mainwindow):
        super().__init__()
        self.setWindowTitle('Search Student')
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        self.mainwindow = mainwindow
        
        layout = QVBoxLayout()

        self.lineedit_name = QLineEdit()
        self.lineedit_name.setPlaceholderText('Name')
        layout.addWidget(self.lineedit_name)

        btn_search = QPushButton('Search')
        btn_search.clicked.connect(self.search)

        self.setLayout(layout)
        layout.addWidget(btn_search)
    

    def search(self):
        self.mainwindow.table.setCurrentItem(None)
        search_str = self.lineedit_name.text()
        if not search_str:
            return
        matching_items = self.mainwindow.table.findItems(search_str,Qt.MatchFlag.MatchContains)
        if matching_items:
            for i in matching_items:
                i.setSelected(True)