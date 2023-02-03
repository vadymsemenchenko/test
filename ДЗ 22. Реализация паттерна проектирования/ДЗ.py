# Выбрать паттерн проектирования и реализовать его на конкретном примере
# (паттерн из GoF, который рассматривали или не рассматривали, но не Singleton, не Iterator, не Decorator).

# Мой паттерн проектирования Facade. Я инвестор своего дома, есть рабочие строители и поставщики материалов,
# а также мои друзья которые пришли после постройки дома расслабится.

class Builder:
    def build(self):
        print('Building...')


class Supplier:
    def sell(self):
        print('Materials...')


class Investor:
    def invest(self):
        print('Investing...')


class Frends:
    def relax(self):
        print('We are relax...')


class Building_My_House:
    def __init__(self):
        self.investor = Investor()
        self.supplier = Supplier()
        self.builder = Builder()

    def build_project(self):
        for i in range(1):
            self.investor.invest()

        for i in range(10):
            self.supplier.sell()

        for i in range(15):
            self.builder.build()

        print('Project finished!')


class My_House:
    def __init__(self):
        self.building_my_house = Building_My_House()
        self.frends = Frends()

    def start_project(self):
        self.building_my_house.build_project()
        for i in range(3):
            self.frends.relax()


if __name__ == "__main__":
    my_house = My_House()
    my_house.start_project()





