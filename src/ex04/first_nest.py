#!/usr/bin/env python3
import sys
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
            return (heads, tails)

            
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



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Передайте путь к файлу аргументом скрипта.\n" \
            "Пример запуска скрипта: python3 first_constructor.py data.csv", file=sys.stderr); 
        sys.exit(1)
    else:
        researcher = Research(sys.argv[1])
        data = researcher.file_reader()
        calculated_data = Research.Calculations(data)
        heads, tails = calculated_data.counts()
        fraction_heads, fraction_tails = calculated_data.fractions()
        analytics = Research.Analytics(data)
        predicted_pairs = analytics.predict_random(3)
        last_element = analytics.predict_last()

        print(data)
        print(heads, tails)
        print(f"{fraction_heads:.4f} {fraction_tails:.4f}")
        print(predicted_pairs)
        print(last_element)

        # print(f"Данные из file_reader: {data}")
        # print(f"Количество орлов и решек из метода counts: {heads}, {tails}")
        # print(f"Доли орлов и решек из метода fractions: {fraction_heads:.4f}; {fraction_tails:.4f}")
        # print(f"Cписок списков из predict_random для трёх шагов: {predicted_pairs}")
        # print(f"Cписок из predict_last: {last_element}")


# ранее юзала
# calculated_data = researcher.Calculations(data)
# analytics = researcher.Analytics(data)
# ответ от нейросетки по лучшей практике применения в файле png

        