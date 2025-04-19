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
        self.setWindowTitle('Traductor Open Source')
        self.setGeometry(200, 200, 700, 600)
        self.modo_oscuro = False
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
            '- Pulsa "Cerrar" para salir de la aplicación.\n'
            '- Pulsa "Modo Oscuro" para cambiar el tema visual.'
        )
        instrucciones.setWordWrap(True)
        instrucciones.setAlignment(Qt.AlignLeft)

        # Entrada de texto
        entrada_group = QGroupBox('Texto a traducir')
        self.texto_entrada = QTextEdit()
        self.texto_entrada.setPlaceholderText('Ingrese aquí el texto (puede ser multilínea)...')
        entrada_layout = QVBoxLayout()
        entrada_layout.setContentsMargins(15, 15, 15, 15)  # Margen interno
        entrada_layout.addWidget(self.texto_entrada)
        entrada_group.setLayout(entrada_layout)
        entrada_group.setObjectName('entrada_group')

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
        self.btn_modo_oscuro = QPushButton('Modo Oscuro')
        self.btn_modo_oscuro.setCheckable(True)
        self.btn_modo_oscuro.clicked.connect(self.toggle_modo_oscuro)
        botones_layout.addWidget(self.btn_traducir)
        botones_layout.addWidget(self.btn_limpiar)
        botones_layout.addWidget(self.btn_cerrar)
        botones_layout.addWidget(self.btn_modo_oscuro)

        # Salida de texto
        salida_group = QGroupBox('Traducción')
        self.texto_salida = QTextEdit()
        self.texto_salida.setReadOnly(True)
        salida_layout = QVBoxLayout()
        salida_layout.setContentsMargins(15, 15, 15, 15)  # Margen interno
        salida_layout.addWidget(self.texto_salida)
        salida_group.setLayout(salida_layout)
        salida_group.setObjectName('salida_group')

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(instrucciones)
        layout.addWidget(entrada_group)
        layout.addLayout(idioma_layout)
        layout.addLayout(botones_layout)
        layout.addWidget(salida_group)

        # Usuarios en la parte inferior derecha
        creditos = QLabel('<span style="font-size:11px;">GitHub: <a href="https://github.com/cmbrdevmx" style="color:#50fa7b;">cmbrdevmx</a> &nbsp;|&nbsp; YouTube: <a href="https://youtube.com/@retired64" style="color:#8be9fd;">retired64</a></span>')
        creditos.setOpenExternalLinks(True)
        creditos.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        creditos.setObjectName('creditos_label')
        layout.addWidget(creditos)
        self.setLayout(layout)

        self.aplicar_tema()

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

    def toggle_modo_oscuro(self):
        self.modo_oscuro = not self.modo_oscuro
        self.aplicar_tema()
        self.btn_modo_oscuro.setChecked(self.modo_oscuro)
        self.btn_modo_oscuro.setText('Modo Claro' if self.modo_oscuro else 'Modo Oscuro')

    def aplicar_tema(self):
        if self.modo_oscuro:
            # Modo oscuro
            self.setStyleSheet('''
                QWidget {
                    background-color: #23272e;
                    color: #f8f8f2;
                }
                QGroupBox {
                    border: 1.5px solid #444;
                    border-radius: 12px;
                    margin-top: 10px;
                    margin-bottom: 10px;
                    color: #f8f8f2;
                    background-color: rgba(40, 42, 54, 0.92);
                    font-weight: bold;
                    padding: 8px 8px 8px 8px;
                }
                QGroupBox:title {
                    subcontrol-origin: margin;
                    left: 12px;
                    top: 4px;
                    padding: 0 5px 0 5px;
                }
                QLabel {
                    color: #f8f8f2;
                }
                QTextEdit {
                    background-color: #282a36;
                    color: #f8f8f2;
                    border: 1px solid #444;
                    border-radius: 6px;
                    padding: 8px;
                }
                QComboBox {
                    background-color: #282a36;
                    color: #f8f8f2;
                    border: 1px solid #444;
                    border-radius: 6px;
                    padding: 4px;
                }
                QPushButton {
                    background-color: #44475a;
                    color: #f8f8f2;
                    border: 1px solid #444;
                    border-radius: 6px;
                    padding: 5px;
                }
                QPushButton:checked {
                    background-color: #6272a4;
                }
                #creditos_label {
                    color: #888;
                    font-size: 11px;
                }
                #creditos_label a {
                    color: #50fa7b;
                    text-decoration: none;
                }
                #creditos_label a:hover {
                    color: #ffb86c;
                    text-decoration: underline;
                }
            ''')
            self.texto_salida.setStyleSheet('background-color: #282a36; color: #f8f8f2;')
        else:
            # Modo claro
            self.setStyleSheet('''
                QGroupBox {
                    border: 1.5px solid #bbb;
                    border-radius: 12px;
                    margin-top: 10px;
                    margin-bottom: 10px;
                    color: #222;
                    background-color: rgba(255,255,255,0.97);
                    font-weight: bold;
                    padding: 8px 8px 8px 8px;
                }
                QGroupBox:title {
                    subcontrol-origin: margin;
                    left: 12px;
                    top: 4px;
                    padding: 0 5px 0 5px;
                }
                #creditos_label {
                    color: #888;
                    font-size: 11px;
                }
                #creditos_label a {
                    color: #0077cc;
                    text-decoration: none;
                }
                #creditos_label a:hover {
                    color: #e67e22;
                    text-decoration: underline;
                }
            ''')
            self.texto_salida.setStyleSheet('background-color: #f4f4f4; color: #222;')
        self.btn_modo_oscuro.setText('Modo Claro' if self.modo_oscuro else 'Modo Oscuro')

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, 'Error', mensaje)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = TraductorGUI()
    ventana.show()
    sys.exit(app.exec_())