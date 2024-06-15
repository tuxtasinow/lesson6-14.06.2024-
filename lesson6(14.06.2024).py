my_dict = {'Alex' : 1996, 'Dan' : 1985, 'Matt' : 1973}  #Словарь
print(my_dict)
print(my_dict['Dan'])  #Обращение к ключу
print(my_dict.get('Sasha'))  #Обращение к несуществующему ключу без ошибки
my_dict.update({'Sarcho' : 2002, 'Michel' : 1999}) #Добавление пары
del my_dict['Sarcho'] #Удаление
print(my_dict)


my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}  #Множество
print(my_set)
my_set.add(6) #Добавление
my_set.add(7) #Добавление
my_set.discard(3)  #Удаление без вывода ошибки
print(my_set)