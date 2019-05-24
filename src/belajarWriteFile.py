from __future__ import print_function

def main():
    conn = open('sample.txt','w')
    variableInput = input('Input : ')
    conn.write(variableInput)
    conn.close()
if __name__ == "__main__":
    main()