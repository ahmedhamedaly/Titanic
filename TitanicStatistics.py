import pandas as pd
import matplotlib.pyplot as plt


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
          f"The average age is {format(survivedMaleAge / survivedMale, '.2f')}, "
          f"The average fare is £{format(survivedMaleFare / survivedMale, '.2f')}")

    activities = ['Male Survived', 'Female Survived', 'Died']
    deaths = 891 - (survivedMale + survivedFemale)
    slices = [survivedMale, survivedFemale, deaths]
    colors = ['r', 'g', 'b']
    plt.pie(slices, labels=activities, colors=colors,
            startangle=90, shadow=True, explode=(0.1, 0.1, 0.1),
            radius=1.2, autopct='%1.1f%%')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
