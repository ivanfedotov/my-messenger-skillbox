import requests
from datetime import datetime
from PyQt6 import QtWidgets, QtCore
import clientui

class Ui_MainWindow(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Событие нажатия кнопки
        self.pushButton_2.pressed.connect(self.send_message)

        # Таймер (1 раз в секунду)
        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def show_messages(self, messages):
        for message in messages:
            dt = datetime.fromtimestamp(message['time'])
            dt = dt.strftime('%H:%M')
            self.textBrowser.append(dt + ' ' + message['name'])
            self.textBrowser.append(message['text'])
            self.textBrowser.append('')

    def get_messages(self):
        try:
            response = requests.get(
                'http://127.0.0.1:5000/messages',
                params={'after': self.after}
            )
        except:
            return

        messages = response.json()['messages']
        if len(messages) > 0:
            self.show_messages(messages)
            self.after = messages[-1]['time']

    def send_message(self):
        name = self.lineEdit_2.text()
        text = self.textEdit.toPlainText()

        try:
            response = requests.post(
                'http://127.0.0.1:5000/send',
                json={'name': name, 'text': text}
            )
        except:
            self.textBrowser.append('Сервет недоступен')
            self.textBrowser.append('')
            return

        if response.status_code != 200:
            self.textBrowser.append('Сообщение не отправлено')
            self.textBrowser.append('Проверьте имя и текст')
            self.textBrowser.append('')
            return

        self.textEdit.clear()

app = QtWidgets.QApplication([])
window = Ui_MainWindow()
window.show()
app.exec()