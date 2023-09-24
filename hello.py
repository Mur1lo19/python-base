#!/usr/bin/env python3
"""
Hello word mult linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:
Tenha váriavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Murilo Ferreira"
__license__ = "unlicense"

import os

current_language = os.getenv("LANG", "pt_BR")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)

