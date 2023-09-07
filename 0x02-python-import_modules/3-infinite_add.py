#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    all = 0
    for number in range(len(sys.argv) - 1):
        all += int(sys.argv[number + 1])
    print("{}".format(all))
