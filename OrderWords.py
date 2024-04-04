import threading
import re

class OrderWords :
    def __init__(self, files, match) :
        self.files = files
        self.match = match
        self.dict= {}
        self.temp = open("./saidaTemp.txt", "a") # Arquivo temporário
        self.contagem = open("./textoFinal.txt", "a") # Contagem final
        self.matchText = open("./matchText.txt", "a") # Arquivo com linhas encontradas com match
        self.count = 0

        for t in range(len(self.files)):
            file = open(f"./{self.files[t]}", "r")
            thread = threading.Thread(target=self.map, args=(self.files[t], file.readlines()))
            lock = threading.Lock()
            lock.acquire()
            thread.start()
            thread.join()
            lock.release()

        self.makeDict()
        for key in self.dict:
            for line in self.dict[key]:
                self.reduce(key, line)

        self.contagem.close()
        self.contagem = open("./textoFinal.txt", "r") # Contagem final

        for index, line in enumerate(self.contagem.readlines()):
            find = re.search(self.match, line)
            if find:
                self.count += 1
                print(f"Line {index+1}: {line}")
                self.matchText.write(f"Line {index+1}: {line}")
        
        print("Total de linhas com match: ", self.count)
                

    # Função map
    def map(self, name, content):
        for line in content:
            self.emitIntermediate(name, line.strip())

    # Função reduce
    def reduce(self, file, words):
        self.emit(file, words)

    def read(self):
        self.contagem.readline()

    # Função auxiliar para fazer dict
    def makeDict(self):
        self.temp.close()
        temp = open("./saidaTemp.txt", "r").readlines()

        for item in temp:
            item = item.strip()
            name = item.split(" ")[0]
            words = item.split(" ")[1:]
            string = ""
            for word in words:
                string += f"{word} "
            string = string.strip()
            if self.dict.get(name):
                self.dict[name].append(string)
            else:
                self.dict[name] = [string]

        x = open("./dict.txt", "a")
        for k in self.dict:
            x.write(f"{k} {self.dict[k]}\n")
        
    # Função para escrever arquivo final
    def emit(self, word, result):
        self.contagem.write(f'{word} {result}\n')

    # Função para escrever arquivo temporário
    def emitIntermediate(self, word, num):
        self.temp.write(f'{word} {num}\n')

# Texto comum
# count = OrderWords(["input0", "input1", "input2", "input3"], "ehecc")
# Usando regex
count = OrderWords(["input0", "input1", "input2", "input3"], r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')