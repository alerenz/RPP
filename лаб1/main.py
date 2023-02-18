import random


def check(a, b, start, end): # проверяет, что элемент из списка А, не встречается в списке В,
    flag = False            # и если встречается, то возвращает false

    for j in a[start:end]:
        if j not in b and j % 2 != 0:
            flag = True
        else:
            return False
    return flag


def del_el(a, start, end): #функция удаления из списка А элементов, подходящие условию
    m = end - 1
    while m >= start:
        if a[m] % 2 != 0:
            a.pop(m)
        m -= 1
    return a


def action(a, b): #основная функция, содержая методы проверки и удаления
    start = -1
    end = 0
    i = 0
    while i < len(a):
        if a[i] % 2 != 0 and start == -1:
            start = i
        else:
            i += 1
        if i + 1 < len(a) and a[i + 1] % 2 == 0 and start != -1:
            end = i + 1
            if check(a, b, start, end):
                a = del_el(a, start, end)
                i = 0
            else:
                i += 1
            start = -1
            end = 0
        if i + 1 == len(a):
            if a[i] % 2 != 0:
                if start == -1:
                    start = i
                end = i + 1
                if check(a, b, start, end):
                    del_el(a, start, end)
            i += 1
    return a


def input_arr(itype): #метод выбора ввода
    a = []
    b = []
    if itype == 1:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

    if itype == 2:
        n = random.randint(10, 20)
        for i in range(n):
            a.append(random.randint(0, 10))
        n = random.randint(5, 10)
        for i in range(n):
            b.append(random.randint(0, 10))
    if itype == 0:
        exit(1)
    return a, b


def main():
    while True:
        print("1 - ввод вручную\n"
              "2 - автоматический ввод\n"
              "0 - закончить программу")
        itype = int(input())
        a, b = input_arr(itype)
        print(f"Список А: {a}")
        print(f"Список B: {b}")
        a = action(a,b)
        print(f"Конечный результат: {a}")


if __name__ == "__main__":
    main()
