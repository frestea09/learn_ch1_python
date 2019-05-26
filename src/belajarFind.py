from __future__ import print_function

def main():
    variableInput = input('input : ')
    variabelCari = input('cari : ')
    indexCari = variableInput.find(variabelCari)
    print('Variable Input : %s '%variableInput)
    print('Varibale Cari : %s'%variabelCari)
    print('Index Variable Cari : %d'%indexCari)
if __name__ == "__main__":
    main()