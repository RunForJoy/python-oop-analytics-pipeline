#!/usr/bin/env python3
import sys

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        with open(self.path, encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines() # сплитует строку по \n  в список
            if len(lines) < 2:
                raise ValueError("Нет данных для чтения")
            header = lines[0]
            data_rows = lines[1:]
            num_of_columns = len(header.split(','))
            if num_of_columns != 2:
                raise ValueError("Не верная структура файла для чтения")
         
            for row in data_rows:
                # игнорим пустые строки в конце файла
                if not row.strip(): 
                    continue
                if set(val.strip() for val in row.split(',')) != {'0', '1'}:
                    raise ValueError("Не верная структура файла для чтения")
                        
            return content


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Передайте путь к файлу аргументом скрипта.\n" \
            "Пример запуска скрипта: python3 first_constructor.py data.csv", file=sys.stderr); 
        sys.exit(1)
    else:
        researcher = Research(sys.argv[1])
        print(researcher.file_reader(), end='')