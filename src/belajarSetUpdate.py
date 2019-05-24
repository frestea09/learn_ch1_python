from __future__ import print_function

def main():
    variableSet = set([])
    print("Set Sekarang : ")
    print(variableSet)
    variableInput = int(input("Belajar : "))
    variableSet.add(variableInput)
    print("Setelah Ditambah : ")
    print(variableSet)
    variableUpdate = [11,12]
    variableSet.update(variableUpdate)
    print(variableSet)
if __name__ == "__main__":
    main()