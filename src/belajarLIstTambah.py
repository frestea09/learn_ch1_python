from __future__ import print_function

def main():
    variableList = []
    # print('list Now : ')
    # print(variableList)
    # print('Use Append')
    # inputAppend = input('input')
    # variableList.append(inputAppend)
    # print('List Setelah Append')
    # print(variableList)
    inputKeyInsert = int(input('Key : '))
    inputValueAppend = input('Value : ')
    variableList.insert(inputKeyInsert,inputValueAppend)
    print(variableList)
    variableList.extend([4,5])
    print(variableList)
if __name__ == "__main__":
    main()