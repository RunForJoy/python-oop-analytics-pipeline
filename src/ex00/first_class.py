#!/usr/bin/env python3

class Must_Read():
    with open('data.csv', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    # your tests and your error handling
    Must_Read()