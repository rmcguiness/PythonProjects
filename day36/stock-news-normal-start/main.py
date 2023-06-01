import requests
import os
import json
from dotenv import load_dotenv
from newsapi import NewsApiClient
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


load_dotenv()
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY =  os.environ.get('STOCK_API_KEY')
NEWS_API_KEY =  os.environ.get('NEWS_API_KEY')

account_sid = "ACf10c2dec482c6378f9b04b55f12a87bf"
twilio_auth_token = os.environ.get("AUTH_TOKEN")

newsapi = NewsApiClient(api_key=NEWS_API_KEY)


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
req_params = {
    "function":'TIME_SERIES_DAILY_ADJUSTED',
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=req_params).json()
daily_data = [val for (key,val) in response['Time Series (Daily)'].items()]

close_price_1 = float(daily_data[1]['4. close'])
#TODO 2. - Get the day before yesterday's closing stock price
close_price_2 = float(daily_data[2]['4. close'])
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(close_price_1 - close_price_2)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = close_price_1 - close_price_2/close_price_2
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if(percent_diff > .05):
    all_articles = newsapi.get_everything(q=f'{STOCK_NAME} OR {COMPANY_NAME}' ,
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
    top_three = all_articles['articles'][:3]

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    
#TODO 9. - Send each article as a separate message via Twilio. 
    for article in top_three:
        client = Client(account_sid, twilio_auth_token)
        message = client.messages \
            .create(
            body=f"Headline:{article['title']}. \n Brief:{article['description']} \n {article['url']}",
            from_="18668758481",
            to="7326758146"
        )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

