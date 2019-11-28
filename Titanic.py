import csv


def allPassInfo(column):
    with open('dataset.csv') as file:
        data = csv.reader(file, delimiter=',')
        for row in data:
            print(f"{row[column]}")


def specificPassInfo(row, column):
    with open('dataset.csv') as file:
        data = csv.reader(file, delimiter=',')
        ro = 0
        for r in data:
            ro += 1
            if ro == row:
                print(r[column])


def main():
    allPassInfo(2)
    specificPassInfo(3, 3)


if __name__ == '__main__':
    main()
