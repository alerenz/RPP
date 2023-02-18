import random
import numpy as np

def write_file(arr, summ,n,m): #запись результатов в файл
    file = open("output.txt", 'w')
    try:
        file.write(f"Размер по строкам: {(str(n))}\n"
                   f"Размер по столбцам: {(str(m))}\n"
                   f"Сумма элементов: {(str(summ))}\n"
                   f"Массив после обработки: \n")
        np.savetxt(file, arr, fmt='%.2f')
    finally:
        file.close()


def array_create(n, m): #создание массива с рандомными элементами
    return np.random.randint(1, 10, size=(n, m))


def summ_str(arr, summ, n, m): #сумма строк и запись в последний стобец относительных сумм
    last_col = [0] * n
    for i in range(n):
        for j in range(m):
            last_col[i] += arr[i][j]
            if j + 1 == m:
                last_col[i] /= summ

    arr = np.column_stack((arr, last_col))
    return arr


def main():
    n = random.randint(5, 10)
    m = random.randint(5, 10)
    arr = array_create(n, m)
    summ = arr.sum()
    arr = summ_str(arr, summ, n, m)
    write_file(arr, summ,n,m)


if __name__ == '__main__':
    main()
