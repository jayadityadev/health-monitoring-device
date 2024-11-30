import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSizePolicy, QSpacerItem
from PyQt5.QtCore import QTimer, Qt, QSize
from PyQt5.QtGui import QImage, QPixmap
import cv2


class CameraWidget(QWidget):
    def __init__(self, parent=None):
        super(CameraWidget, self).__init__(parent)
        self.initUI()
        self.capture = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.current_resolution = (640, 480)

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.input_layout = QVBoxLayout()
        self.layout.addLayout(self.input_layout, 0)

        self.ip_input = QLineEdit(self)
        self.ip_input.setPlaceholderText(
            "IP address")
        self.input_layout.addWidget(self.ip_input, 0, Qt.AlignCenter)

        self.start_button = QPushButton("Start Stream", self)
        self.start_button.clicked.connect(self.on_start_button_clicked)
        self.input_layout.addWidget(self.start_button, 0, Qt.AlignCenter)

        self.error_label = QLabel(self)
        self.layout.addWidget(self.error_label, 0, Qt.AlignCenter)

        self.label = QLabel(self)
        self.layout.addWidget(self.label, 0, Qt.AlignCenter)

    def on_start_button_clicked(self):
        ip_address = self.ip_input.text().strip()
        if ip_address:
            url = f"http://{ip_address}:81/stream"
            if self.start_camera(url):
                self.error_label.setText("")
                self.ip_input.hide()
                self.start_button.hide()
                self.timer.start(30)
            else:
                self.error_label.setText(
                    "Invalid IP address or unable to connect to the stream.")
        else:
            self.error_label.setText("Please enter a valid IP address.")

    def start_camera(self, ip_address):
        self.capture = cv2.VideoCapture(ip_address)
        return self.capture.isOpened()

    def set_resolution(self, resolution):
        self.current_resolution = resolution
        if self.capture and self.capture.isOpened():
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

    def update_frame(self):
        if self.capture and self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                frame = cv2.resize(frame, self.current_resolution)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = QImage(
                    frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(image)
                self.label.setPixmap(pixmap)

    def closeEvent(self, event):
        if self.capture and self.capture.isOpened():
            self.capture.release()
        super(CameraWidget, self).closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraWidget()
    window.setWindowTitle("Camera Stream")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
