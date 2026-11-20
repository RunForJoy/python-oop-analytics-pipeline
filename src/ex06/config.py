DATA_FILE = "data.csv"
NUM_STEPS = 3
REPORT_FILENAME = "report"
REPORT_EXTENSION = "txt"
LOG_FILE = "analytics.log"

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

REPORT_TEMPLATE = (
    "В нашем эксперименте с подбрасыванием монеты из {total} наблюдений "
    "{tails_str} выпала решка и {heads_str} — орёл. "
    "Вероятности составляют {fraction_tails}% и {fraction_heads}% соответственно. "
    "Мы прогнозируем, что в следующих {steps} наблюдениях решка выпадет {predicted_tails_str}, "
    "а орёл — {predicted_heads_str}."
)
