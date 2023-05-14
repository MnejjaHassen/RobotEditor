# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
from app.app_file import *
import sys
import os
import ctypes

myappid = "mycompany.myproduct.subproduct.version"  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'


# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.active_btn_left_menu = None

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////

        # OPEN EDITOR PAGE
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # OPEN EDITOR PAGE
        if btn.objectName() == "btn_editor":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # NEW FILE
        if btn.objectName() == "btn_new_file":
            # New File
            Files.new(self)

            # Return to Editor Page
            self.ui.left_menu.select_only_one("btn_editor")
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # OPEN FILE
        if btn.objectName() == "btn_open_file":
            # Open File
            Files.open(self)

            # Return to Editor Page
            self.ui.left_menu.select_only_one("btn_editor")
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # SAVE FILE
        if btn.objectName() == "btn_save_file":
            # Return to Editor Page
            self.ui.left_menu.select_only_one("btn_editor")
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

            # Save File
            Files.save(self)

        # OPEN SETTINGS
        if (
            btn.objectName() == "btn_settings"
            or btn.objectName() == "btn_close_left_column"
        ):
            # Check if left column is visible
            if not MainFunctions.left_column_is_visible(self):
                # Show/Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                self.active_btn_left_menu = btn
            else:
                if (
                    btn.objectName() == "btn_close_left_column"
                ):  # This BTN is default btn of left column on top
                    # Deselect all tabs selected
                    self.ui.left_menu.deselect_all_tab()

                    # Show/Hide
                    MainFunctions.toggle_left_column(self)

                if self.active_btn_left_menu == btn:
                    self.ui.left_menu.deselect_all_tab()
                    MainFunctions.toggle_left_column(self)
                    return
                # Slect Tab
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                self.active_btn_left_menu = btn

            # Change Left Page
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings Tab",
                    icon_path=Functions.set_svg_icon("icon_settings.svg"),
                )

                # Get Title Menu Btn
                btn_top_settings = MainFunctions.get_title_bar_btn(
                    self, "btn_top_settings"
                )
                btn_top_settings.set_active(False)

        # OPEN INFO
        if (
            btn.objectName() == "btn_info"
            or btn.objectName() == "btn_close_left_column"
        ):
            # Check if left column is visible
            if not MainFunctions.left_column_is_visible(self):
                # Show/Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                self.active_btn_left_menu = btn
            else:
                if (
                    btn.objectName() == "btn_close_left_column"
                ):  # This BTN is default btn of left column on top
                    # Deselect all tabs selected
                    self.ui.left_menu.deselect_all_tab()

                    # Show/Hide
                    MainFunctions.toggle_left_column(self)

                if self.active_btn_left_menu == btn:
                    self.ui.left_menu.deselect_all_tab()
                    MainFunctions.toggle_left_column(self)
                    return
                # Slect Tab
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                self.active_btn_left_menu = btn
            # Change Left Page
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2,
                    title="Info Tab",
                    icon_path=Functions.set_svg_icon("icon_info.svg"),
                )

                # Get Title Menu Btn
                btn_top_settings = MainFunctions.get_title_bar_btn(
                    self, "btn_top_settings"
                )
                btn_top_settings.set_active(False)

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////

        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn
            btn_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            btn_settings.set_active_tab(False)

            # Get Left Menu Btn
            btn_info = MainFunctions.get_left_menu_btn(self, "btn_info")
            btn_info.set_active_tab(False)

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())
