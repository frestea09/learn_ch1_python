from __future__ import print_function

def main():
    variabelDictionary = {}
    variableInput = input("variabel Apa : ")
    variableKey = input("Variable Key : ")
    variabelDictionary[variableKey] = variableInput
    print(variabelDictionary)
    variabelUbah = input("Key Ubah : ")
    variableInput = input("Value Ubah : ")
    variabelDictionary[variabelUbah] = variableInput
    print(variabelDictionary)
if __name__ == "__main__":
    main()