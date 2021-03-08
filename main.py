import sys
from redimensionar_imagem import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap


class Redimensionar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, nova_img=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setFixedSize(1300, 700)
        self.nova_img = nova_img

        self.btnArquivo.clicked.connect(self.abrir_imagem)

        self.btnRedimensionar.clicked.connect(self.redimensionar)

        self.btnSalvar.clicked.connect(self.salvar)
    
    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem',
            "C:/Users/Thiago/Desktop/Thiago/Galeria",
            filter='Images (*.png *.jpg *.jpeg *.gif *.jfif)'
        )
        self.inputArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))
    
    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_img = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_img)
        self.inputAltura.setText(str(self.nova_img.height()))

    def salvar(self):
        if self.nova_img:
            imagem, _ = QFileDialog.getSaveFileName(
                self.centralwidget,
                'Salvar Imagem',
                "C:/Users/Thiago/Desktop/imagem.png",
                filter='png'
            )

        try:
            self.nova_img.save(imagem, 'PNG')
        except:
            pass



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    red = Redimensionar()
    red.show()
    qt.exec_()