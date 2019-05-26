from __future__ import print_function


def main():
    conn = open('simple.txt')
    curr = conn.readline()
    while curr:
        print(curr,end='')
        curr = conn.readline()
    conn.close()
if __name__ == "__main__":
    main()