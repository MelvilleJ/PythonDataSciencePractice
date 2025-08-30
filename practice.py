import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('personal_finance_dataset.csv')
df['Date'] = pd.to_datetime(df['Date']) 

choice = 0
choice2 = 0
while True:
    choice = 0
    print('------------------------- \n')
    print('Please enter the type of transaction you would like to see: \n')
    print('1. Income')
    print('2. Expense')
    print('4. Quit')
    choice = int(input('Enter your choice: '))
    
    match choice:
        case 1:  # INCOME MENU
            df_income = df[df['Type'] == 'Income'].copy()
            df_income = df_income.drop_duplicates().dropna()

            while True:
                print('---------------------------------\n')
                print('What would you like to see?\n')
                print('---------------------------------\n')
                print('1. Rolling Average')
                print('2. Total')
                print('3. Total by Month')
                print('4. NumPy Stats (Mean, Median, Std, Min, Max)')
                print('5. Detect Outliers')
                print('6. Back')
                choice2 = int(input('Enter your choice: '))

                match choice2:
                    case 1:  # Rolling Average
                        daily_income = df_income.groupby('Date')['Amount'].sum()
                        rolling_avg = daily_income.rolling(window=7).mean()  # 7-day
                        plt.figure(figsize=(10, 6))
                        plt.plot(daily_income, label='Daily Income', alpha=0.6)
                        plt.plot(rolling_avg, label='7-Day Rolling Average', color='red')
                        plt.title('Rolling Average Income')
                        plt.xlabel('Date')
                        plt.ylabel('Amount ($)')
                        plt.legend()
                        plt.grid(True)
                        plt.show()

                    case 2:  # Total
                        total_income = np.round(df_income['Amount'].to_numpy().sum(), 2)
                        print(f'Total Income = ${total_income}')

                    case 3:  # Total by Month
                        monthly_income = df_income.groupby(df_income['Date'].dt.to_period('M'))['Amount'].sum()
                        monthly_income.plot(kind='bar', figsize=(10, 6))
                        plt.title("Total Monthly Income")
                        plt.ylabel("Amount ($)")
                        plt.show()
                        print(monthly_income)

                    case 4:  # NumPy Stats
                        amounts = df_income['Amount'].to_numpy()
                        print("Income Stats:")
                        print(f"Mean: ${np.mean(amounts):.2f}")
                        print(f"Median: ${np.median(amounts):.2f}")
                        print(f"Std Dev: ${np.std(amounts):.2f}")
                        print(f"Max: ${np.max(amounts):.2f}")
                        print(f"Min: ${np.min(amounts):.2f}")

                    case 5:  # Outlier Detection
                        amounts = df_income['Amount'].to_numpy()
                        mean, std = np.mean(amounts), np.std(amounts)
                        outliers = amounts > (mean + 2 * std)
                        df_income['Outlier'] = np.where(outliers, "Yes", "No")
                        print("Income Outliers:")
                        print(df_income[df_income['Outlier'] == "Yes"][['Date', 'Category', 'Amount']])

                    case 6:  # Back
                        break
