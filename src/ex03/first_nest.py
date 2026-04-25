#!/usr/bin/env python3
import sys

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
        def counts(self, data):
            self.data  = data
            heads = 0
            tails = 0
            for i in data:
                if i[0] == 1:
                    heads += 1
                else:
                    tails += 1
            return (heads, tails)

            
        def fractions(self, heads, tails):
            return heads/(heads+tails), tails/(heads+tails)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Передайте путь к файлу аргументом скрипта.\n" \
            "Пример запуска скрипта: python3 first_constructor.py data.csv", file=sys.stderr); 
        sys.exit(1)
    else:
        researcher = Research(sys.argv[1])
        data = researcher.file_reader()
        calculated_data = researcher.Calculations()
        heads, tails = calculated_data.counts(data)
        fraction_heads, fraction_tails = calculated_data.fractions(heads, tails)
        print(data)
        print(heads, tails)
        print(f"{fraction_heads:.4f} {fraction_tails:.4f}")


# data = researcher.file_reader()  # Python сам передаст has_header=True
# Если позже понадобится файл без заголовка:
# data = researcher.file_reader(has_header=False)