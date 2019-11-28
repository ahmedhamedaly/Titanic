import pandas as pd

df = pd.read_csv("dataset.csv")


def main():
    print(f"Categories: {str(df.columns.tolist()).strip('[]')}")

    while True:
        category = input("Select Category: ")
        if category.casefold() in str(df.columns.tolist()).casefold():
            print("Do something")
        elif category.casefold() == "quit":
            print("Quiting the program")
            break
        else:
            print("Invalid input! Please try again.")


if __name__ == '__main__':
    main()
