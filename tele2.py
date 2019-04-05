# def is_archived(tariff):
#     return tariff.archived
#
# def is_actual(tariff):
#     return not tariff.archived
#
# def my_filter(func, items):
#     result = []
#     for item in items:
#         if func(item):
#             result.append(item)
#
class Tariff:
    def __init__(
            self,
            name,
            price=0, #без абонентской платы
            price_period='month',
            gb = 0, #-1 no limit
            minutes =0,
            sms = 0,
            hit = False,
            gb_unlim = None,
            minutes_unlim_tele2 = True,
            archived = False
    ):
        self.archived = archived
        self.name = name
        self.price = price
        self.price_period= price_period
        self.sms = sms
        self.hit = hit
        self.minutes = minutes
        self.gb_unlim = gb_unlim
        self.gb = gb
        self.minutes_unlim_tele2 = minutes_unlim_tele2


class TariffManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def actual(self):
        return list(filter(lambda x: not x.archived, self.items))

    def archived(self):
        return list(filter(lambda o: o.archived, self.items)) #передаем только имя функции - а сама функция filter

if __name__ == '__main__':
    manager = TariffManager()
    my_online = Tariff('Мой онлайн', price=290, hit=True, gb=15, gb_unlim='vk', minutes=400)
    my_tele = Tariff('Мой ', price=290, price_period='day', hit=True, gb=15, gb_unlim='vk', minutes=400)
    univer = Tariff("Универ", price=0, archived=True)

    manager.add(my_online)
    manager.add(my_tele)
    manager.add(univer)

    actual = manager.actual()
    for item in actual:
        print('actual:', item.name)

    archived = manager.archived()
    for item in archived:
        print('archived:', item.name)

#card, service - 2 classa
#card name,
# бонусы и скидки - толкьо одинб категории - можно выбрать много, валюта - одна
#банки - многоБ в каком формате данные
#поиск, сортировка