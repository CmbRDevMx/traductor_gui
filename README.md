# Traductor Multilínea Profesional

## ¿Qué es este proyecto?

Este proyecto es una aplicación de escritorio que permite traducir textos de varios idiomas usando una interfaz gráfica sencilla y cómoda. Está pensada para usuarios que desean traducir párrafos o textos largos de manera rápida, sin complicaciones y sin depender del navegador web.

## Características principales
- Traducción automática entre múltiples idiomas usando Google Translate (a través de `deep_translator`).
- Interfaz gráfica intuitiva y amigable (con PyQt5).
- Permite copiar y pegar textos fácilmente.
- Selección de idioma de origen y destino.
- Botones para traducir, limpiar campos y cerrar la aplicación.
- Traducción multilínea.

## ¿Cómo usar la aplicación?

1. **Abrir la aplicación**: Al ejecutar el programa, verás una ventana con instrucciones.
2. **Ingresar texto**: Escribe o pega el texto que deseas traducir en el área de entrada.
3. **Seleccionar idiomas**: Elige el idioma de origen (o "Auto detectar") y el idioma de destino.
4. **Traducir**: Haz clic en el botón "Traducir" para ver la traducción en el área de salida.
5. **Limpiar**: Usa el botón "Limpiar" para borrar los campos y empezar una nueva traducción.
6. **Cerrar**: Pulsa "Cerrar" para salir de la aplicación.

## Requisitos y dependencias

Antes de compilar o ejecutar, asegúrate de tener instalado Python 3.7 o superior.

Las dependencias necesarias están listadas en `requirements.txt`:
- PyQt5
- colorama
- deep_translator

Puedes instalarlas ejecutando:

```bash
pip install -r requirements.txt
```

## Archivos principales
- `traductor_gui.py`: Código principal de la interfaz gráfica.
- `traducir_google.py`: Lógica de traducción usando Google Translate.
- `icono.ico`: Icono de la aplicación.
- `requirements.txt`: Lista de dependencias.

## Compilar el ejecutable (.exe)

Para generar el archivo ejecutable para Windows, se utiliza **PyInstaller**. Debes tenerlo instalado:

```bash
pip install pyinstaller
```

Luego, ejecuta el siguiente comando en la carpeta del proyecto:

```bash
pyinstaller --onefile --windowed --icon=icono.ico traductor_gui.py
```

### ¿Qué hace cada opción?
- `--onefile`: Crea un solo archivo ejecutable.
- `--windowed`: No muestra consola al abrir la app (modo ventana).
- `--icon=icono.ico`: Usa el icono personalizado para el ejecutable.
- `traductor_gui.py`: Archivo principal del programa.

El ejecutable se generará en la carpeta `dist/`.

## Notas adicionales
- Si agregas nuevos módulos, recuerda actualizar `requirements.txt`.
- Si tienes problemas con la traducción, asegúrate de tener conexión a internet.
- El traductor usa la API pública de Google Translate a través de `deep_translator`.

---

**¡Listo! Ahora puedes disfrutar de tu traductor multilínea profesional en Windows.**
