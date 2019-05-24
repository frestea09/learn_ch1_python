from __future__ import print_function

def main():
    i = 0
    while i<=10:
        j = 0
        while j<=i:
            print(j,end='')
            j+=1
        print()
        i+=1
if __name__ == "__main__":
    main()