from customComponents import *
from PyQt6.QtWidgets import QMainWindow,QToolBar,QStatusBar,QPushButton,QApplication
from PyQt6.QtGui import QAction,QIcon
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management App')
        self.setMinimumSize(800,600)

        

        # Menu item & sub item (=Actions)
        # Menu item: File
        menu_item_file = self.menuBar().addMenu('&File')
        action_insert_student = QAction(QIcon('icons/add.png'),'Add Student',self)
        action_insert_student.triggered.connect(lambda a :InsertDialog(self).exec())
        menu_item_file.addAction(action_insert_student)

        # Menu item: Help
        menu_item_help = self.menuBar().addMenu('&Help')
        action_about = QAction('About',self)
        action_about.triggered.connect(lambda a :AboutMsgBox())
        menu_item_help.addAction(action_about)

        # Menu item: Edit
        menu_item_edit = self.menuBar().addMenu('&Edit')
        action_search_record = QAction(QIcon('icons/search.png'),'search',self)
        action_search_record.triggered.connect(lambda a : SearchDialog(self).exec())
        menu_item_edit.addAction(action_search_record)

        # Toolbar
        toolbar = QToolBar('My main toolbar')
        toolbar.addAction(action_insert_student)
        toolbar.addAction(action_search_record)
        self.addToolBar(toolbar)

        # Table widget
        self.table = MyTableWidget(self)
        self.table.loaddata()
        self.setCentralWidget(self.table)

        # Status bar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
    

    def show_statusbar_btns(self):
        self.rmv_statusbar_btns()
        btn_edit = QPushButton('Edit Record')
        btn_edit.clicked.connect(lambda a :EditRecordDialog(self).exec())
        self.statusbar.addWidget(btn_edit)
        btn_del = QPushButton('Delete Record')
        btn_del.clicked.connect(lambda a :DeleteRecordMsgBox(self))
        self.statusbar.addWidget(btn_del)


    def rmv_statusbar_btns(self):
        children = self.statusbar.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)


app = QApplication(sys.argv)
window0 = MainWindow()
window0.show()
sys.exit(app.exec())