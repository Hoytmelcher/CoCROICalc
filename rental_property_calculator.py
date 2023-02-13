class Inputs():
    def __init__(self):
        self.incomes = []
        self.expenses = []
        self.investment = []
        self.total_month_income = []
        self.total_month_expense = []
        self.total_invest = []

    def add_input(self):
        type = input("Which are you adding: none, income, expense, or investment? ").lower()
        if type == "income":
            ammount = int(input("How much? "))
            if ammount == int(ammount):
                self.incomes.append(int(ammount))
            else:
                print("Please input digits")
        elif type == "expense":
            ammount = int(input("How much? "))
            if ammount == int(ammount):
                self.expenses.append(int(ammount))
            else:
                print("Please input digits")
        elif type == "investment":
            ammount = int(input("How much? "))
            if ammount == int(ammount):
                self.investment.append(int(ammount))
            else:
                print("Please input digits")
        elif type == "none":
            return
        else:
            print("Input invalid, please try again")


    def monthly_income(self):
        income = sum(self.incomes)
        self.total_month_income = income
        print(f'Total monthly income est: ${self.total_month_income}')

    def monthly_expenses(self):
        expense = sum(self.expenses)
        self.total_month_expense = expense
        print(f'Total monthly expenses est: ${self.total_month_expense}')

    def investments(self):
        invest = sum(self.investment)
        self.total_invest = invest
        print(f'Total investment est: ${self.total_invest}')

    def cash_flow(self):
        total_monthly_cashflow = self.total_month_income - self.total_month_expense
        print(f'Total monthly cashflow est: ${total_monthly_cashflow}')
        total_annual_cashflow = total_monthly_cashflow * 12
        print(f'Total annual cashflow est: ${total_annual_cashflow}')
        coc = total_annual_cashflow / self.total_invest
        total_return = coc *100
        print(f'Estimated Cash on Cash Return: %{total_return}')
        return total_return


class Calc():
    def __init__(self):
        self.calc = Inputs()
        
    def calculate_return(self):
        while True:
            option = input("Choose an option: add, display, or run? ").lower()

            if option == 'add':
                self.calc.add_input()
            elif option == 'display':
                print(self.calc.incomes)
                print(self.calc.expenses)
                print(self.calc.investment)
            elif option == 'run':
                self.calc.monthly_income()
                self.calc.monthly_expenses()
                self.calc.investments()
                self.calc.cash_flow()
                
            else:
                break

            

house = Calc()

house.calculate_return()









