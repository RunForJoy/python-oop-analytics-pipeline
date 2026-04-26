#!/usr/bin/env python3

import os
from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True) -> list:
        with open(self.path, encoding='utf-8') as f:
            self.output_content = []
            content = f.read()
            lines = content.splitlines() # сплитует строку по \n  в список
                        
            if has_header and len(lines) < 2:
                raise ValueError("Нет данных для чтения.")
            elif not has_header and len(lines) < 1:
                raise ValueError("Неверная структура файла для чтения. Файл пуст.")
            
            start_index = 1 if has_header else 0
            data_rows = lines[start_index:]
         
            for row in data_rows:
                if not row.strip(): 
                    continue

                line = [int(val.strip()) for val in row.split(',')]

                if set(line) != {0, 1}:
                    raise ValueError("Неверная структура файла для чтения.")
                
                self.output_content.append(line)

            return self.output_content
        

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = 0
            tails = 0
            for i in self.data:
                if i[0] == 1:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

            
        def fractions(self):
            heads, tails = self.counts()
            return heads/(heads+tails), tails/(heads+tails)

    class Analytics(Calculations):
        def predict_random(self, count):
            predictions = []
            for _ in range(count):
                heads = randint(0, 1)
                tails = int(not heads)
                predictions.append([heads, tails])
            return predictions

        def predict_last(self):
            if not self.data:
                raise ValueError('Список пуст')
            return self.data[-1]
        
        def save_file(self, data, file_name, extension):
            full_path = os.path.join(os.getcwd(), f"{file_name}.{extension}")
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(data)

# os.getcwd() - get current working directory/Возвращает текущую рабочую директорию
# os.path.join(a, b) - автоматическая склейка путей (подставляет правильный разделитель для ОС)
# на Linux/macOS разделитель путей /
# на Windows разделитель путей \

# т.е код ниже cломается на Windows:
# path = os.getcwd() + "/" + f"{file_name}.{extension}"