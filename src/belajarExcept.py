from __future__ import print_function
def main():
    try:
        fileName = 'sample.txt'
        conn = open(fileName)
        for i in conn:
            print(i,end=' ')

    except IOError as e:
        print(e)

if __name__ == "__main__":
    main()