import argparse
import logging
from deep_translator import GoogleTranslator
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def traducir(texto: str, origen: str = 'auto', destino: str = 'es') -> str | None:
    """Traduce un texto usando GoogleTranslator."""
    try:
        return GoogleTranslator(source=origen, target=destino).translate(texto)
    except Exception as error:
        logging.error(Fore.RED + f"Fallo la traducción: {error}")
        return None


def leer_texto_multilinea() -> str:
    """Lee texto multilínea desde entrada estándar hasta que se escriba 'FIN'."""
    logging.info(Fore.CYAN + "Modo interactivo: ingrese el texto. Escriba 'FIN' para terminar.")
    lineas = []

    try:
        while True:
            linea = input()
            if linea.strip().upper() == "FIN":
                break
            lineas.append(linea)
    except KeyboardInterrupt:
        logging.warning(Fore.YELLOW + "Entrada cancelada por el usuario.")
        return ""

    return "\n".join(lineas).strip()


def validar_idioma(codigo: str) -> bool:
    """Valida que el código de idioma tenga 2 o 3 letras o sea 'auto'."""
    return codigo == "auto" or (codigo.isalpha() and len(codigo) in (2, 3))


def main():
    parser = argparse.ArgumentParser(
        description="Traductor multilínea usando Google Translate API"
    )
    parser.add_argument(
        "-t", "--texto",
        help="Texto a traducir. Si se omite, se habilita el modo interactivo.",
        type=str
    )
    parser.add_argument(
        "-d", "--destino",
        help="Código del idioma destino (ej: es, en, fr).",
        default="es",
        type=str
    )
    parser.add_argument(
        "-o", "--origen",
        help="Código del idioma origen (ej: en, auto).",
        default="auto",
        type=str
    )

    args = parser.parse_args()

    if not validar_idioma(args.destino):
        logging.error(Fore.RED + "El idioma destino debe tener 2 o 3 letras.")
        return

    if not validar_idioma(args.origen):
        logging.error(Fore.RED + "El idioma origen debe tener 2 o 3 letras.")
        return

    texto = args.texto or leer_texto_multilinea()
    if not texto:
        logging.warning(Fore.YELLOW + "No se ingresó ningún texto.")
        return

    resultado = traducir(texto, origen=args.origen, destino=args.destino)
    if resultado:
        print(Fore.GREEN + Style.BRIGHT + "\n✅ Traducción exitosa:\n")
        print(Fore.WHITE + resultado)
    else:
        logging.error(Fore.RED + "No se pudo traducir el texto.")


if __name__ == "__main__":
    main()
