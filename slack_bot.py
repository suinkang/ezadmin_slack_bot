import pandas as pd
import json
import requests
import config

ACCESS_TOKEN = config.ACCESS_TOKEN
channel_id = config.CHANNEL_ID

# data preprocessing
df = pd.read_csv('stock.csv')
column_names=['상품명','옵션','정상재고']
selected_df = df[column_names]
selected_df = selected_df.dropna()

message = selected_df.to_string()
data = {'Content-Type': 'application/x-www-form-urlencoded',
        'token': ACCESS_TOKEN,
        'channel': channel_id, 
        'text': message
        } 
try:
    URL = "https://slack.com/api/chat.postMessage"
    res = requests.post(URL, data=data)
except:
    print(1)