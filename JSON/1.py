import json

# Загрузка данных из JSON-файла
with open('sample-data.json') as f:
    data = json.load(f)

# Вывод заголовка
print("Статус интерфейса")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Описание", "Скорость", "MTU"))
print("-" * 80)

# Итерация по интерфейсам и вывод информации
for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
