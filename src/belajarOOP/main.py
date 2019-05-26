from __future__ import print_function
from abc import ABCMeta,abstractclassmethod

class kerangkaManusia(metaclass= ABCMeta):
    def bicara(self):
        pass
class Manusia(kerangkaManusia):
    def __init__(self,inputKata = None):
        self.__kata = inputKata
    def setKata(self,inputKata):
        self.__kata = inputKata
    def getKata(self):
        return self.__kata
    def bicara(self):
        print(self.__kata)

def main():
    myManusia = Manusia()
    inputKata = input('Kata : ')
    myManusia.setKata(inputKata)
    myManusia.bicara()
if __name__ == "__main__":
    main()
