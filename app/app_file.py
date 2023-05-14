from gui.uis.windows.main_window.ui_main import UI_MainWindow
from qt_core import QFileDialog, QMessageBox, Qt

file_name = None
original_content = ""


# Files
# ////////////////////////////////////////////
class Files:
    def __init__(self):
        super.__init__()

        # IMPORTS WIDGETS
        self.ui = UI_MainWindow()
        self.ui.setup_ui()

    # ASK SAVE CHANGES DIALOG
    # ////////////////////////////////////////////
    def ask_save_changes_dialog(self):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Question)
        dialog.setWindowTitle("Save Changes")
        dialog.setText("You have unsaved changes. Do you want to save them?")
        dialog.setStandardButtons(
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        dialog.setDefaultButton(QMessageBox.Save)
        dialog.setWindowFlag(Qt.WindowTitleHint)
        response = dialog.exec_()

        if response == QMessageBox.Save:
            return QMessageBox.Save
        elif response == QMessageBox.Discard:
            return QMessageBox.Discard
        else:
            return QMessageBox.Cancel

    # NEW FILE
    # ////////////////////////////////////////////
    def new(self):
        global file_name, original_content
        print(original_content)
        print(self.ui.load_pages.text_edit.toPlainText())
        if original_content != self.ui.load_pages.text_edit.toPlainText():
            response = Files.ask_save_changes_dialog(self)
            if response == QMessageBox.Save:
                Files.save(self)
            elif response == QMessageBox.Cancel:
                return

        # reset Fields
        self.ui.load_pages.text_edit.setPlainText("")
        self.ui.title_bar.set_title("Untitled")
        file_name = None
        original_content = ""

    # OPEN FILE
    # ////////////////////////////////////////////
    def open(self):
        global file_name, original_content
        print(original_content)
        print(self.ui.load_pages.text_edit.toPlainText())
        if original_content != self.ui.load_pages.text_edit.toPlainText():
            response = Files.ask_save_changes_dialog(self)
            if response == QMessageBox.Save:
                Files.save(self)
            elif response == QMessageBox.Cancel:
                return

        # OPEN FILE DIALOG
        dlg_file = QFileDialog.getOpenFileName(
            parent=self,
            caption=self.tr("select a Robobt file"),
            filter=self.tr("Robot files (*.robot)"),
        )

        # READ FILE
        if dlg_file:
            file = open(dlg_file[0], encoding="utf-8")  # open file
            text = file.read()
            file.close()
            self.ui.load_pages.text_edit.setPlainText(text)
            original_content = text
            file_name = dlg_file[0]
            self.ui.title_bar.set_title(file_name)

    # SAVE FILE
    # ////////////////////////////////////////////
    def save(self):
        global file_name

        def write_text(self, file):
            global original_content
            print("Saved in folder: " + file)
            file = open(file, "w")
            text = self.ui.load_pages.text_edit.toPlainText()
            file.write(text)
            original_content = text
            file.close()

        # READ FILE
        if file_name:
            write_text(self, file_name)
            # Change Title
            self.ui.title_bar.set_title(file_name)
        else:
            # FILE DIALOG
            dlg_file = QFileDialog.getSaveFileName(
                parent=self,
                caption=self.tr("Select Robobt file"),
                filter=self.tr("Robot files (*.robot)"),
            )

            if dlg_file:
                file_name = dlg_file[0]
                write_text(self, file_name)
                # Change Title
                self.ui.title_bar.set_title(file_name)
