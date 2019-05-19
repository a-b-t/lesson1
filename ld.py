tem = {'city': 'Москва', 'temperature': 20}
tem['temperature'] -= 5
a = tem.get('country', 'Россия')
tem['date']='27.05.2019'
print(tem, a, len(tem))