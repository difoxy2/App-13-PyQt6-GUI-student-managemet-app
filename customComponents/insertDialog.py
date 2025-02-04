from settings import DB_CONNECT
from PyQt6.QtWidgets import QDialog,QVBoxLayout,QLineEdit,QComboBox,QPushButton

class InsertDialog(QDialog):
    def __init__(self,mainwindow):
        super().__init__()
        self.setWindowTitle('Insert Student Data')
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        self.mainwindow = mainwindow
        
        layout = QVBoxLayout()

        self.lineedit_name = QLineEdit()
        self.lineedit_name.setPlaceholderText('Name')
        layout.addWidget(self.lineedit_name)

        self.combobox_subject = QComboBox()
        self.combobox_subject.addItems(['Biology','Math','Astronomy','Physics'])
        layout.addWidget(self.combobox_subject)

        self.lineedit_mobile = QLineEdit()
        self.lineedit_mobile.setPlaceholderText('Mobile')
        layout.addWidget(self.lineedit_mobile)

        btn_register = QPushButton('Register')
        btn_register.clicked.connect(self.add_student)
        layout.addWidget(btn_register)

        self.setLayout(layout)


    def add_student(self):
        name = self.lineedit_name.text()
        course = self.combobox_subject.currentText()
        mobile = self.lineedit_mobile.text()
        
        connection_obj = DB_CONNECT()
        cursor_obj = connection_obj.cursor()
        sql = """INSERT INTO students(name,course,mobile)
                    VALUES(?,?,?)
        """
        cursor_obj.execute(sql,(name,course,mobile))
        connection_obj.commit()
        cursor_obj.close()
        connection_obj.close()
        self.mainwindow.table.loaddata()