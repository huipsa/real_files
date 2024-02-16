cook_book = {}
with open("recipes.txt", "r", encoding="utf-8") as lines:
    last_key = ""
    for line in lines:
        line = line.strip()
        if line.isdigit():
            continue
        elif line and "|" not in line:
            cook_book[line] = []
            last_key = line
        elif line and "|" in line:
             nm, qt, msr = line.split(" | ")
             cook_book.get(last_key).append(dict(ingredient_name=nm, quantity=int(qt), measure=msr))

def real_shop_list(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingredient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .split(', ')
  shop_list = real_shop_list(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()

