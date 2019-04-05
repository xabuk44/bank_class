class Card:
    def __init__(self,
                 name,
                 *,
                 card_type,
                 bank,
                 max_percent=0,
                 min_percent=0,
                 # fix perc ==  max = min
                 #no perc == max = min = 0
                 # percent float == max = 7 min = 0
                 cost_from=0,
                 cost_to=0,
                 img=True,
                 bonus=None,
                 has_cashback=False,
                 cashback_from=0,
                 cashback_to=0,
            ):
        self.name = name
        self.bank = bank
        self.card_type = card_type
        self.max_percent = max_percent
        self.min_percent = min_percent
        self.cost_from = cost_from
        self.cost_to = cost_to
        self.img = img
        self.bonus = bonus
        self.has_cashback = has_cashback
        self.cashback_from = cashback_from
        self.cashback_to = cashback_to


class Service:
    def __init__(self):
        self.cards = []

    def add(self, item):
        self.cards.append(item)

    def search_type(self, params):
        return filter(lambda x: params in x.card_type, self.cards)

    def search_bank(self, params):
        return filter(lambda x: params in x.bank, self.cards)

    def sort(self, do):
        a = list(filter(lambda x: x.has_cashback, self.cards))
        return list(filter(lambda x: do < x.cashback_to, a))

    # def sort(self, field):
    #     return sorted(self.cards, reverse=reverse)

    def filter_by_percent(self, percent):
        pass

    def filter_by_cashback(self, cashback):
        pass

