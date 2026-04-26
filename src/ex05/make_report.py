#!/usr/bin/env python3
import os
import config
import analytics

# вспомогательная ф-я для формата "1 раза 2 раз"
def get_times_word(num: int) -> str:
    num = abs(num)
    if num % 10 == 1 and num % 100 != 11:
        return "раз"
    elif num % 10 in (2, 3, 4) and num % 100 not in (12, 13, 14):
        return "раза"
    else:
        return "раз"


if __name__ == '__main__':
    data_path = os.path.join(os.getcwd(), config.DATA_FILE)
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Файл {data_path} не найден.")
    
    researcher = analytics.Research(data_path)
    data = researcher.file_reader()
    
    calculated_data = analytics.Research.Calculations(data)
    heads, tails = calculated_data.counts()
    fraction_heads, fraction_tails = calculated_data.fractions()
    analytic_data = analytics.Research.Analytics(data)
    predicted_pairs = analytic_data.predict_random(config.NUM_STEPS)
    predicted_heads = sum(1 for p in predicted_pairs if p[0] == 0)
    predicted_tails = config.NUM_STEPS - predicted_heads  
    format_to_pct = lambda x: f"{x * 100:.2f}".replace('.', ',')

    report_data = {
        "total": heads + tails,
        "tails_str": f"{tails} {get_times_word(tails)}",
        "heads_str": f"{heads} {get_times_word(heads)}",
        "fraction_heads": format_to_pct(fraction_heads),
        "fraction_tails": format_to_pct(fraction_tails),
        "steps": config.NUM_STEPS,
        "predicted_tails_str": f"{predicted_tails} {get_times_word(predicted_tails)}",
        "predicted_heads_str": f"{predicted_heads} {get_times_word(predicted_heads)}"
    }
    report_text = config.REPORT_TEMPLATE.format(**report_data)
    print(report_text)
    analytic_data.save_file(report_text, config.REPORT_FILENAME, config.REPORT_EXTENSION)

