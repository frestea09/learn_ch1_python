from __future__ import print_function

def main():
    variableInput = input('Input : ')
    variableCari = input('Huruf yang dicari : ')
    print("Variable : %s"%variableInput)
    print("Search Variable : %s"%variableCari)
    print("Vairalble : ",variableInput.count(variableCari))
if __name__ == "__main__":
    main()