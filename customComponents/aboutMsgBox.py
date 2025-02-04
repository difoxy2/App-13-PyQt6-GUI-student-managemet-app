from PyQt6.QtWidgets import QMessageBox


class AboutMsgBox(QMessageBox):
    def __init__(self):
        print('hi')
        super().__init__()  
        self.information(
            self,
            'About',
            f"""
This app is a simple student management CRUD app implemented with python

Features are Create, Read, Update, Delete, Search student records from sqlite3 database

Library used: PyQt6, sqlite3

Author: Helen Lai ( bigdk0900ft@gmail.com )
            """,
        )