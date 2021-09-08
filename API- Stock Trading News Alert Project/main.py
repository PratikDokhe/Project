import requests
import datetime

# STOCK = "TATAMOTORS.BSE"
# COMPANY_NAME = "Tata Motors"
# STOCK = "ADANIPOWER.BSE"
# COMPANY_NAME = "Adani Power"
STOCK = "JKPAPER.BSE"
COMPANY_NAME = "JK Paper"

move_in_stock = ""
today = datetime.date.today()

offset = max(1, (today.weekday() + 6) % 7 - 3)
timedelta = datetime.timedelta(offset)

yesterday = today - timedelta

offset = max(1, (yesterday.weekday() + 6) % 7 - 3)
timedelta = datetime.timedelta(offset)

day_before_yesterday = yesterday - timedelta
yesterday = str(yesterday)
day_before_yesterday = str(day_before_yesterday)


def is_price_move():
    global move_in_stock
    api_key = "A2IMYA3IMFMHUMG2"
    url = "https://www.alphavantage.co/query"
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": api_key
    }

    response = requests.get(url, params=parameters)

    data = response.json()

    yesterday_price = float(data["Time Series (Daily)"][yesterday]['4. close'])
    day_before_yesterday_price = float(data["Time Series (Daily)"][day_before_yesterday]['4. close'])

    high_5 = (day_before_yesterday_price * 105) / 100
    low_5 = (day_before_yesterday_price * 95) / 100

    if yesterday_price <= low_5:
        move_in_stock = "negative"
        return True
    elif yesterday_price >= high_5:
        move_in_stock = "positive"
        return True
    else:
        return False


def fetch_news(move):
    api_key = "0458c00703f74420b229b8c01c0e58b6"
    url = "https://newsapi.org/v2/everything"
    parameters = {
        "apiKey": api_key,
        "language": "en",
        "qInTitle": COMPANY_NAME,
        "sortBy": "relevancy"
    }
    response = requests.get(url, params=parameters)

    news_data = response.json()
    news_articles = news_data["articles"]

    if move == "negative":
        print(f"{STOCK} showed Down-move of 5% or more...! \nHere are top 5 news :-\n")
    elif move == "positive":
        print(f"{STOCK} showed Up-move of 5% or more...! \nHere are top 5 news :-\n")

    for i in range(0, 5):
        try:
            headline = news_articles[i]["title"]
            brief = news_articles[i]["description"]
            print(f"{i + 1}. Headline: {headline} \nBrief: {brief}\n\n")
        except IndexError:
            break


if is_price_move():
    fetch_news(move_in_stock)
else:
    print("No noticeable stock movement in your stock")
