from app.banki_ru import Service

from app.banki_ru import Card

if __name__ == '__main__':

    manager = Service()

    tinkoff_black = Card(
        'Tinkoff black',
        bank='Tinkoff',
        card_type='Visa Platinum',
        img='tcs.png',
        max_percent=6,
        min_percent=6,
        cost_from=0,
        cost_to=1_188,
        bonus=None,
        has_cashback=True,
        cashback_from=0,
        cashback_to=5
    )

    multicarta = Card(
        'Мультикарта Привелегия',
        bank='VTB',
        card_type=['Visa Platinum', 'Mastercard'],
        img='vtb.png',
        max_percent=7,
        min_percent=0,
        cost_from=0,
        cost_to=2_988,
        bonus=None,
        has_cashback=True,
        cashback_from=0,
        cashback_to=2.5
    )

    premium = Card(
        'Премиум Infinite',
        bank='Газпромбанк',
        card_type=['Visa Platinum', 'Mastercard'],
        img='vtb.png',
        max_percent=7,
        min_percent=0,
        cost_from=0,
        cost_to=19_999,
        bonus=None,
        has_cashback=True,
        cashback_from=0,
        cashback_to=3
    )

    manager.add(tinkoff_black)
    manager.add(multicarta)
    manager.add(premium)

    search_type = manager.search_type('Visa')
    for item in search_type:
        print('Searching cards:', item.name, ',', item.card_type)

    search_bank = manager.search_bank('VTB')
    for item in search_bank:
        print('Searching cards:', item.name, '\"', item.bank, '\"')

    sort_cashback = manager.sort(3)
    for item in sort_cashback:
        print('Cashback:', item.name, item.cashback_from, '-', item.cashback_to, '%')


