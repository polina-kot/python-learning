# TODO Напишите функцию для поиска индекса товара
def find_index(items_list, item_to_find):
    try:
        return items_list.index(item_to_find)
    except ValueError:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item =find_index(items_list, find_item)   # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
