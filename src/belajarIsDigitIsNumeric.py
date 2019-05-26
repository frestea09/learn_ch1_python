from __future__ import print_function

def main():
    try:
        inputNumber = input('Variabel Number : ')
        inputDigit = input('Variable Digit : ')
        hasilDigit = inputDigit.isdigit()
        hasilNumber = inputNumber.isnumeric()
        print('Vairbale Input : %s'%inputNumber)
        print('Variabel Digit : %s'%inputDigit)
        print('Hasil Digit :  %s'%hasilDigit)
        print('Hasil Number : %s '%hasilNumber)
    except:
        print('Error input ')

if __name__ == "__main__":
    main()