from __future__ import print_function

def main():
    variabelList  = []
    variabelInput = input('Input : ')
    variabelList.append(variabelInput)
    print(variabelInput)
    varibleUbah = input('Input Ubah : ')
    variabelList[0] = varibleUbah
    print(variabelList)
if __name__ == "__main__":
    main()