from phone_store import PHONES

def search_by_props(name,memory,color):
    phones = []
    for phone in PHONES:
        if phone['name'] == name and phone['memory'] == memory and phone['color'] == color:
            phones.append(phone)

    if len(phones) == 0:
        print("Извините у нас нет в наличии этот телефон")
    else:
        for phone in phones:
            print(str(phone)+"\n")

def search_by_price():
    phones_1 = []
    price = int(input("Введите сумму:"))
    for phone in PHONES:
        if phone['price'] == price:
            print(phone)
    if len(phones_1) == 0:
        print("Извините у нас нет телефон на эту сумму")
    else:
        for phone in phones_1:
            print(str(phone)+ "\n")