class Company:
    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Person(Company):
    def __init__(self, company_bank, company_name, first_name, last_name, salary):
        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salary(self):
        if self.company_bank < self.salary:
            print("у компании недостаточно средств")
        else:
            self.company_bank -= self.salary
            print(f'Остаток капитала компании {self.company_bank}')

    def get_info(self):
        print(f'Информация о сотруднике: {self.first_name} {self.last_name}\n зарплата:{self.salary}\n')


bank = Person(90000, 'Etiket', 'Jon', 'Haison', 40000)
bank.get_salary()
bank.get_info()
