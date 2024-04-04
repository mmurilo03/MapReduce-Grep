import os

if (os.path.exists("./dict.txt")):
    os.remove("./dict.txt")
if (os.path.exists("./saidaTemp.txt")):
    os.remove("./saidaTemp.txt")
if (os.path.exists("./textoFinal.txt")):
    os.remove("./textoFinal.txt")
if (os.path.exists("./matchText.txt")):
    os.remove("./matchText.txt")