documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}


def id_doc():   
  doc_number = input("введите номер документа::")
  result = True
  for doc_key in documents:
    if doc_number == doc_key["number"]:
      return doc_key["name"]
    elif doc_number != doc_key["number"]:
      result = "владелец не существует или номер введен неправильно"
  return result




def a_shelf(): 
  doc_number = input("введите номер документа:") 
  rsult = True
  for doc_key, doc_value in directories.items():
    if doc_number in doc_value:
      return  doc_key
    elif doc_number not in doc_value:
      result = "полка не существует"
  return result




def doc_list():
  print("Весь список:")
  for doc_id in documents:
    doc_type = doc_id['type']
    doc_number = doc_id['number']
    doc_name = doc_id['name']
    result = ('{0}"{1}" "{2}"'.format(doc_type, doc_number, doc_name))
    print(result)
  return "Конец списка"




def add_doc():
  doc_type = input("введите тип документа:")
  doc_number = input("введите номер документа:")
  person_name = input("Введите имя владельца:")
  doc_shelf = input("Введит номер полки {} : ".format(directories.keys()))
  new_doc = dict(type=doc_type, number=doc_number, name=person_name)
  if doc_shelf not in directories:
    return "полки не существует поэтому документ не добавлен"
  else:
    directories[doc_shelf] += [doc_number]
    documents.append(new_doc)
    print("документ успешно добавлен в список и в полку")
  print("список документов:", documents, "полка документов:", directories, sep="\n")
  return "Программа завершилось!"




def command():
  print("Список команд:")
  print("doc_id - Чтобы узнать кто владелец документа")
  print("shelf - Чтобы узнать полку документа")
  print("doc_list - Чтобы узнать весь список документов")
  print("doc_add - Чтобы добавить новый документ")  
  first_command = input("Вводите команду сюда:")
  if first_command == "doc_id":
    print(id_doc())
  elif first_command == "shelf":
    print(a_shelf())
  elif first_command == "doc_list":
    print(doc_list())
  elif first_command == "doc_add":
    print(add_doc())
  else:
    print("Вы выбрали неправильную команду")
    return command()
  return "спасибо за внимание!"

print(command())