#!/usr/bin/env python3

import os
from random import randint
import logging # добавила
import json
import urllib.request
import urllib.error
from random import randint
import config   # нужен для телеги

class Research:
    def __init__(self, path):
        self.path = path
        logging.info("Research initialized with path: %s", path) 

    def file_reader(self, has_header=True) -> list:
        logging.info("Reading data from file: %s", self.path)
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
            logging.info("File read successfully, %d rows parsed", len(self.output_content))
            return self.output_content
        

    def send_report_to_telegram(self, is_success: bool) -> str:
        MSG_SUCCESS = "The report has been successfully created"
        MSG_ERROR = "The report hasn't been created due to an error."
        
        message = MSG_SUCCESS if is_success else MSG_ERROR
        
        url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = json.dumps({
            "chat_id": config.TELEGRAM_CHAT_ID,
            "text": message
        }).encode("utf-8")

        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})

        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                logging.info("Telegram message delivered successfully")
        except Exception as e:
                logging.error("Failed to deliver Telegram message: %s", e)
            
        return message
       

    class Calculations:
        def __init__(self, data):
            self.data = data
            # избавляюсь от задвоенного лога из-за повторного вызова counts для fractions
            self._counts_cache = None  
            # logging.info("Calculations initialized with %d data rows", len(data))

        def counts(self):
            if self._counts_cache is None:
                logging.info("Calculating the counts of heads and tails") 
                heads = 0
                tails = 0
                for i in self.data:
                    if i[0] == 1:
                        heads += 1
                    else:
                        tails += 1
                self._counts_cache = (heads, tails)
                logging.info("Counts result: heads=%d, tails=%d", heads, tails)
            return self._counts_cache
                
            
        def fractions(self):
            logging.info("Calculating fractions")
            heads, tails = self.counts()
            total = heads + tails
            if total == 0:
                 logging.warning("Total count is zero, returning 0.0")
                 return 0.0, 0.0
            
            heads_frac = heads / total
            tails_frac = tails / total
            logging.info("Raw fractions calculated: %.4f, %.4f", heads_frac, tails_frac)
            return heads_frac, tails_frac
            
     
    class Analytics(Calculations):
        def predict_random(self, count):
            logging.info("Generating %d random predictions", count)
            predictions = []
            for _ in range(count):
                heads = randint(0, 1)
                tails = int(not heads)
                predictions.append([heads, tails])
            logging.info("Random predictions generated: %s", predictions)
            return predictions

        def predict_last(self):
            logging.info("Getting last element from data list")
            if not self.data:
                raise ValueError('Список пуст')
            result = self.data[-1]
            logging.info("Last element: %s", result)
            return result
        
        def save_file(self, data, file_name, extension):
            logging.info("Saving report to file: %s.%s", file_name, extension)
            full_path = os.path.join(os.getcwd(), f"{file_name}.{extension}")
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(data)
            logging.info("File saved successfully: %s", full_path)

 