name = input("Введите наименование товара: ")
price = int(input("Введите цену товара (рубли): "))
weight = int(input("Введите вес товара (кг): "))
quantity = int(input("Введите количество: "))
total = price * weight

print("Чек")
print(f"{name} - {weight} кг - {price} руб/кг")
print(f"Итого: {total} руб")
print(f"Внесено: {quantity} руб")
print(f"Сдача: {quantity - total} руб")


