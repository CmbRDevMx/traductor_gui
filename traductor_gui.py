import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QMessageBox, QGroupBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from traducir_google import traducir, validar_idioma

IDIOMAS = {
    'Auto detectar': 'auto',
    'Español': 'es',
    'Inglés': 'en',
    'Francés': 'fr',
    'Alemán': 'de',
    'Italiano': 'it',
    'Portugués': 'pt',
    'Ruso': 'ru',
    'Chino': 'zh-CN',
    'Japonés': 'ja',
    'Coreano': 'ko',
    'Árabe': 'ar',
    'Hindi': 'hi',
    'Turco': 'tr',
}

class TraductorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Traductor Multilínea Profesional')
        self.setGeometry(200, 200, 700, 600)
        self.init_ui()

    def init_ui(self):
        fuente = QFont('Arial', 11)
        self.setFont(fuente)

        instrucciones = QLabel(
            'INSTRUCCIONES:\n'
            '- Escribe o pega el texto a traducir en el área de entrada.\n'
            '- Selecciona el idioma de origen y destino.\n'
            '- Pulsa "Traducir" para ver el resultado.\n'
            '- Pulsa "Limpiar" para borrar los campos.\n'
            '- Pulsa "Cerrar" para salir de la aplicación.'
        )
        instrucciones.setWordWrap(True)
        instrucciones.setStyleSheet('color: #333;')
        instrucciones.setAlignment(Qt.AlignLeft)

        # Entrada de texto
        entrada_group = QGroupBox('Texto a traducir')
        self.texto_entrada = QTextEdit()
        self.texto_entrada.setPlaceholderText('Ingrese aquí el texto (puede ser multilínea)...')
        entrada_layout = QVBoxLayout()
        entrada_layout.addWidget(self.texto_entrada)
        entrada_group.setLayout(entrada_layout)

        # Selección de idiomas
        idioma_layout = QHBoxLayout()
        self.combo_origen = QComboBox()
        self.combo_origen.addItems(IDIOMAS.keys())
        self.combo_origen.setCurrentText('Auto detectar')
        self.combo_destino = QComboBox()
        self.combo_destino.addItems(IDIOMAS.keys())
        self.combo_destino.setCurrentText('Español')
        idioma_layout.addWidget(QLabel('Idioma origen:'))
        idioma_layout.addWidget(self.combo_origen)
        idioma_layout.addSpacing(20)
        idioma_layout.addWidget(QLabel('Idioma destino:'))
        idioma_layout.addWidget(self.combo_destino)

        # Botones
        botones_layout = QHBoxLayout()
        self.btn_traducir = QPushButton('Traducir')
        self.btn_traducir.clicked.connect(self.traducir_texto)
        self.btn_limpiar = QPushButton('Limpiar')
        self.btn_limpiar.clicked.connect(self.limpiar_campos)
        self.btn_cerrar = QPushButton('Cerrar')
        self.btn_cerrar.clicked.connect(self.close)
        botones_layout.addWidget(self.btn_traducir)
        botones_layout.addWidget(self.btn_limpiar)
        botones_layout.addWidget(self.btn_cerrar)

        # Salida de texto
        salida_group = QGroupBox('Traducción')
        self.texto_salida = QTextEdit()
        self.texto_salida.setReadOnly(True)
        self.texto_salida.setStyleSheet('background-color: #f4f4f4;')
        salida_layout = QVBoxLayout()
        salida_layout.addWidget(self.texto_salida)
        salida_group.setLayout(salida_layout)

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(instrucciones)
        layout.addWidget(entrada_group)
        layout.addLayout(idioma_layout)
        layout.addLayout(botones_layout)
        layout.addWidget(salida_group)
        self.setLayout(layout)

    def traducir_texto(self):
        texto = self.texto_entrada.toPlainText().strip()
        if not texto:
            self.mostrar_error('Debe ingresar texto para traducir.')
            return
        origen = IDIOMAS[self.combo_origen.currentText()]
        destino = IDIOMAS[self.combo_destino.currentText()]
        if not validar_idioma(origen):
            self.mostrar_error('El código del idioma origen no es válido.')
            return
        if not validar_idioma(destino):
            self.mostrar_error('El código del idioma destino no es válido.')
            return
        resultado = traducir(texto, origen, destino)
        if resultado:
            self.texto_salida.setPlainText(resultado)
        else:
            self.mostrar_error('No se pudo traducir el texto.')

    def limpiar_campos(self):
        self.texto_entrada.clear()
        self.texto_salida.clear()
        self.combo_origen.setCurrentText('Auto detectar')
        self.combo_destino.setCurrentText('Español')

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, 'Error', mensaje)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = TraductorGUI()
    ventana.show()
    sys.exit(app.exec_())