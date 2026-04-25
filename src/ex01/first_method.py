#!/usr/bin/env python3

class Research:
    def file_reader(self):
        with open('data.csv', encoding='utf-8') as f:
            return f.read()


if __name__ == '__main__':
    reasecher = Research()
    print(reasecher.file_reader(), end='')