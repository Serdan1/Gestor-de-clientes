import sys
import menu
import ui

if __name__ == "__main__":
    if "-t" in sys.argv:
        menu.iniciar()
    else:
        app = ui.MainWindow()
        app.mainloop()