from settings import DB_CONNECT
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem
from customComponents import *

class MyTableWidget(QTableWidget):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow


    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        if self.itemAt(e.pos()) is None:
            self.mainwindow.rmv_statusbar_btns()
        else:
            self.mainwindow.show_statusbar_btns()


    def loaddata(self):
        connection_obj = DB_CONNECT()
        cursor_obj = connection_obj.cursor()
        sql = """select * from students"""
        cursor_obj.execute(sql)
        
        # get column names from cursor object, set col names to table widget
        col_names = [i[0] for i in cursor_obj.description]
        self.setColumnCount(len(col_names))
        self.setHorizontalHeaderLabels(col_names)
        self.verticalHeader().setVisible(False)

        # populate db data to table widget
        self.setRowCount(0)
        for row_index, row_data in enumerate(cursor_obj.fetchall()):
            self.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.setItem(row_index,col_index,QTableWidgetItem(str(col_data)))

        # close connections
        cursor_obj.close()
        connection_obj.close()