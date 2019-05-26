from __future__ import print_function

def getCapitalize(inputPertama):
    hasil = inputPertama.capitalize()
    return hasil

def getCenter(inputString):
    hasil = inputString.center(20,"-")
    return hasil
def main():
    inputVariable = input('input : ')
    hasil = getCenter(inputVariable)
    print(hasil)
if __name__ == "__main__":
    main()