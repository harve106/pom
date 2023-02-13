import argparse
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simple Pomodoro Timer")
    parser.add_argument('-w', action="store", dest="work")
    parser.add_argument('-r', action="store", dest="rest")
    parser.add_argument('-a', action="store", dest="alarm")

    args = parser.parse_args()

    work = 25
    rest = 5
    alarm = 2

    if args.work:
        work = int(args.work)
    if args.rest:
        rest = int(args.rest)
    if args.alarm:
        alarm = int(args.alarm)

    print ("Starting timer\n", "Time:\t", work, "\nRest:\t", rest, "\nAlarm:\t", alarm, "\n")

    while True:
        print ("WORK")
        time.sleep(work * 60)
        
        print ("REST")
        for i in range(alarm):
            print("\a", end='')

        time.sleep(rest * 60)

        for i in range(alarm):
            print("\a", end='')


