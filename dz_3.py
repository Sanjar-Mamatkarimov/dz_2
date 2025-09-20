import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


def main():
    app = QApplication(sys.argv)

   
    window = QWidget()
    window.setWindowTitle("Моё окно с кнопкой")

    layout = QVBoxLayout()
    button = QPushButton("Нажми меня")

    button.clicked.connect(lambda: print("Кнопка нажата!"))

    layout.addWidget(button)
    window.setLayout(layout)


    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()