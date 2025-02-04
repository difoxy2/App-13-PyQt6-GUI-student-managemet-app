from settings import DB_CONNECT
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton

class EditRecordDialog(QDialog):
    def __init__(self,mainwindow):
        super().__init__()
        self.setWindowTitle('Edit Student Record')
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        self.mainwindow = mainwindow

        layout = QVBoxLayout()

        # Retrive table row data
        selected_row = self.mainwindow.table.currentRow()
        self.record_id = self.mainwindow.table.item(selected_row,0).text()
        record_name = self.mainwindow.table.item(selected_row,1).text()
        record_course = self.mainwindow.table.item(selected_row,2).text()
        record_tel = self.mainwindow.table.item(selected_row,3).text()

        # Widget with current row data
        self.lineedit_name = QLineEdit(record_name)
        layout.addWidget(self.lineedit_name)
        self.combobox_subject = QComboBox()
        self.combobox_subject.addItems(['Biology','Math','Astronomy','Physics'])
        self.combobox_subject.setCurrentText(record_course)
        layout.addWidget(self.combobox_subject)
        self.lineedit_tel = QLineEdit(record_tel)
        layout.addWidget(self.lineedit_tel)

        # Submit button and reload table data
        btn_submit = QPushButton('Edit Record')
        btn_submit.clicked.connect(self.btn_submit_clicked)
        layout.addWidget(btn_submit)

        self.setLayout(layout)

    def btn_submit_clicked(self):
        connection_obj = DB_CONNECT()
        cursor_obj = connection_obj.cursor()
        sql = """
        UPDATE students
        SET name = ?, course = ?, mobile = ?
        where id = ?
        """
        cursor_obj.execute(sql, (self.lineedit_name.text(),self.combobox_subject.currentText(),self.lineedit_tel.text(),self.record_id) )
        connection_obj.commit()
        cursor_obj.close()
        connection_obj.close()
        self.mainwindow.table.loaddata()
