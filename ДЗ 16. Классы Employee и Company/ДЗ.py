# Создать классы Employee (сотрудник) и Company (компания).
# Классы должны содержать:
# минимум два поля экземпляров и одно поле класса
# минимум два метода экземпляра
# минимум один метод класса
# минимум один статический метод
# К методам добавить строки документации.
# Методы должные быть НЕ get/set поле, а что-то оригинальнее:) (но если надо их, тоже можно добавить)
# Написать код который создает несколько экземпляров и взаимодействует с объектами
# Задание в том числе и на фантазию



class Client:
    def __init__(self, code, name, dep_opening_date, dep_amount, dep_interest):
        self.code = code
        self.name = name
        self.dep_opening_date = dep_opening_date
        self.dep_amount = dep_amount
        self.dep_interest = dep_interest

    def __str__(self):
        return f'клиент {self.code}, {self.name}, дата открытия вклада: {self.dep_opening_date}, ' \
               f'сумма вклада: {self.dep_amount}, процент: {self.dep_interest}'


class Bank:
    def __init__(self, clientBase=None):
        if clientBase is None:
            clientBase = []
        self.clientBase = clientBase

    def addClient(self, client):
        self.clientBase.append(client)

    def showByMoney(self, money):
        '''
        Принимает количество денег и выводит информацию обо всех клиентах, у которых размер вклада больше.
        '''
        print(f'Клиенты, у которых размер вклада больше {money}:')
        [print(x) for x in self.clientBase if x.dep_amount > money]

    def showByCode(self, code):
        '''
        Принимает код и выводит всю информацию о клиенте с данным кодом.
        '''
        print(f'Информация о клиенте с кодом {code}:')
        [print(x) for x in self.clientBase if x.code == code]

    def showByProc(self, proc):
        '''
        Принимает процент и выводит информацию обо всех клиентах, у которых процент по вкладу больше данного.
        '''
        print(f'Клиенты, у которых процент по вкладу больше {proc}:')
        [print(x) for x in self.clientBase if x.dep_interest > proc]


bank = Bank()
bank.addClient(Client(12345, 'Вадим', '12.12.2022', 1000, 3))
bank.addClient(Client(67890, 'Петр', '08.12.2022', 2000, 5))
bank.addClient(Client(36925, 'Николай', '20.12.2022', 3000, 6))

bank.showByMoney(1)
print()
bank.showByCode(12345)
print()
bank.showByProc(3)