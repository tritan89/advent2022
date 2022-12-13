import math


m0 = [98, 89, 52]
m1 = [57, 95, 80, 92, 57, 78]
m2 = [82, 74, 97, 75, 51, 92, 83]
m3 = [97, 88, 51, 68, 76]
m4 = [63]
m5 = [94, 91, 51, 63]
m6 = [61, 54, 94, 71, 74, 68, 98, 83]
m7 = [90, 56]

monkey_business = [0, 0, 0, 0, 0, 0, 0, 0]
divs = [5, 2, 19, 7, 17, 13, 3, 11]


def monkey0():

    monkey_business[0] += len(m0)
    for item in m0:

        item = (item * 2)
        item = item % 9699690
        if item % 5 == 0:

            m6.append(item)
        else:
            m1.append(item)
    m0.clear()

def monkey1():
    monkey_business[1] += len(m1)
    for item in m1:

        item = (item * 13)
        item = item % 9699690
        if item % 2 == 0:

            m2.append(item)
        else:
            m6.append(item)
    m1.clear()

def monkey2():
    monkey_business[2] += len(m2)
    for item in m2:

        item = (item + 5)
        item = item % 9699690
        if item % 19 == 0:

            m7.append(item)
        else:
            m5.append(item)
    m2.clear()

def monkey3():
    monkey_business[3] += len(m3)
    for item in m3:

        item = (item +6)
        item = item % 9699690
        if item % 7 == 0:

            m0.append(item)
        else:
            m4.append(item)
    m3.clear()

def monkey4():
    monkey_business[4] += len(m4)
    for item in m4:

        item = (item + 1)
        item = item % 9699690
        if item % 17 == 0:
            m0.append(item)
        else:
            m1.append(item)
    m4.clear()

def monkey5():
    monkey_business[5] += len(m5)
    for item in m5:

        item = (item + 4)
        item = item % 9699690
        if item % 13 == 0:
            m4.append(item)
        else:
            m3.append(item)
    m5.clear()

def monkey6():
    monkey_business[6] += len(m6)
    for item in m6:

        item = (item +2)
        item = item % 9699690
        if item % 3 == 0:
            m2.append(item)
        else:
            m7.append(item)
    m6.clear()
def monkey7():
    monkey_business[7] += len(m7)
    for item in m7:

        item = (item**2)
        item = item % 9699690
        if item % 11 == 0:
            m3.append(item)
        else:
            m5.append(item)
    m7.clear()


def main():
    for i in range(10000):
        if m0:
            monkey0()
        if m1:
            monkey1()
        if m2:
            monkey2()
        if m3:
            monkey3()
        if m4:
            monkey4()
        if m5:
            monkey5()
        if m6:
            monkey6()
        if m7:
            monkey7()
        print(i,monkey_business)
    monkey_business.sort()
    print(monkey_business[-1]*monkey_business[-2])


main()
