import pandas as pd


def main():
    df = pd.read_csv("dataset.csv")
    survivedCount = 0

    survivedMale = 0
    survivedMaleAge = 0
    survivedMaleFare = 0

    survivedFemale = 0

    for index, row in df.iterrows():
        if row['Survived'] == 1:
            survivedCount += 1
            if row['Sex'] == "male":
                survivedMale += 1
                if row['Age'] >= 0:
                    survivedMaleAge += row['Age']
                if row['Fare'] > 0:
                    survivedMaleFare += row['Fare']
            else:
                survivedFemale += 1

    print(f"There's a total of {survivedCount} people who survived the Titanic.")
    print(f"Of which, {survivedMale} are male and {survivedFemale} are female")
    print(f"Of the {survivedMale} males that survived, "
          f"The average age is {format(survivedMaleAge/survivedMale, '.2f')}, "
          f"The average fare is {format(survivedMaleFare/survivedMale, '.2f')}")


if __name__ == '__main__':
    main()
