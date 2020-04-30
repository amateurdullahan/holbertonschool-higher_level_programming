#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = 1
    sum = 0
    if (len(sys.argv) == 1):
        sum = sys.argv[arg]
        print("{:d}".format(sum))
    elif (len(sys.argv) > 1):
        for argc in range(arg, len(sys.argv)):
            sum += int(sys.argv[arg])
            arg += 1
    print("{:d}".format(sum))
