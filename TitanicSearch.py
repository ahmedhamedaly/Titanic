import pandas as pd

df = pd.read_csv("dataset.csv")


def getCat(category):
    if category.casefold() == "quit":
        return "quit"

    for cat in df.columns.tolist():
        if category.casefold() == cat.casefold():
            return cat
    return ""


def getSea(category):
    if category == df.columns.tolist()[0]:
        se = int(input("Unique ID of the passenger: "))
        if 0 < se < 982:
            print(df.iloc[se - 1])
        else:
            print("Input a valid PassengerId")
    elif category == df.columns.tolist()[1]:
        su = input("Survived (1) or died (0): ")
        for index, row in df.iterrows():
            if row['Survived'] == int(su):
                print(df.iloc[index])
    elif category == df.columns.tolist()[2]:
        pc = input("Passenger's class (1, 2 or 3): ")
        for index, row in df.iterrows():
            if row['Pclass'] == int(pc):
                print(df.iloc[index])
    elif category == df.columns.tolist()[3]:
        na = input("Passengers name: ")
        for index, name in df.iterrows():
            if str(na).casefold() in str(name['Name']).casefold():
                print(df.iloc[index])
    elif category == df.columns.tolist()[4]:
        ge = input("Passengers sex ")
        count = 0
        if ge.casefold() == "male":
            for index, sex in df.iterrows():
                if sex['Sex'] == ge.casefold():
                    count += 1
                    print(df.iloc[index])
            print(f"Printed {count} {ge}s")
        elif ge.casefold() == "female":
            for index, sex in df.iterrows():
                if sex['Sex'] == ge.casefold():
                    count += 1
                    print(df.iloc[index])
            print(f"Printed {count} {ge}s")
        else:
            print("Enter a valid sex!")
    elif category == df.columns.tolist()[5]:
        ag = input("Passengers age: ")
        for index, row in df.iterrows():
            if float(row['Age']) == float(ag):
                print(df.iloc[index])
    elif category == df.columns.tolist()[6]:
        si = input("Enter the Number of siblings/spouses the Passenger has aboard the Titanic: ")
        for index, row in df.iterrows():
            if row['SibSp'] == int(si):
                print(df.iloc[index])
    elif category == df.columns.tolist()[7]:
        pa = input("Number of parents/children the Passenger has aboard the Titanic: ")
        for index, row in df.iterrows():
            if row['Parch'] == int(pa):
                print(df.iloc[index])
    elif category == df.columns.tolist()[8]:
        ti = input("Ticket number: ")
        for index, row in df.iterrows():
            if row['Ticket'] == ti:
                print(df.iloc[index])
    elif category == df.columns.tolist()[9]:
        fa = input("Fare paid for ticket: ")
        for index, row in df.iterrows():
            if row['Fare'] == fa:
                print(df.iloc[index])
    elif category == df.columns.tolist()[10]:
        ca = input("Cabin number: ")
        for index, row in df.iterrows():
            if row['Cabin'] == ca:
                print(df.iloc[index])
    elif category == df.columns.tolist()[11]:
        em = input("Where the passenger got on the ship (C - Cherbourg, S - Southampton, Q = Queenstown): ")
        for index, row in df.iterrows():
            if row['Embarked'] == em:
                print(df.iloc[index])


def main():
    print(f"Categories: {str(df.columns.tolist()).strip('[]')}")

    while True:
        category = getCat(input("Select Category: "))
        if category in df.columns.tolist():
            getSea(category)
        elif category == "quit":
            print("Quiting the program")
            break
        else:
            print("Invalid input! Please try again.")


if __name__ == '__main__':
    main()
