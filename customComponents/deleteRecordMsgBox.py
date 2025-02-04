from settings import DB_CONNECT
from PyQt6.QtWidgets import QMessageBox


class DeleteRecordMsgBox(QMessageBox):
    def __init__(self,mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        self.setMinimumSize(500,500)

        # Retrive table row data
        selected_row = self.mainwindow.table.currentRow()
        if selected_row == -1:
            return
        record_id = self.mainwindow.table.item(selected_row,0).text()
        record_name = self.mainwindow.table.item(selected_row,1).text()
        record_course = self.mainwindow.table.item(selected_row,2).text()
        record_tel = self.mainwindow.table.item(selected_row,3).text()

        confirm=self.question(
            self,
            'Delete Student Record',
            f"""
Delete this record?

Name : {record_name} 
Subject : {record_course}
Mobile : {record_tel}
            """,
            buttons=self.StandardButton.Yes|self.StandardButton.No,
            defaultButton=self.StandardButton.No
        )

        if confirm == self.StandardButton.Yes:
            connection_obj = DB_CONNECT()
            cursor_obj = connection_obj.cursor()
            sql = """
            DELETE FROM students WHERE id = ?;
            """
            cursor_obj.execute(sql,(record_id,))
            connection_obj.commit()
            cursor_obj.close()
            connection_obj.close()
            self.mainwindow.table.loaddata()

