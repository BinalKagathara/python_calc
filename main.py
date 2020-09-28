import sys
from PyQt5.QtWidgets import QApplication
from view import GUI
from  model import evaluateExpression


# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = GUI()
    view.show()
    sys.exit(pycalc.exec_())


    model = evaluateExpression

if __name__ == "__main__":
    main()