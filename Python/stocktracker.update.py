import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt 
import time
import smtplib 


ts = TimeSeries(key='###', output_format='pandas')  #get key from https://www.alphavantage.co/support/#api-key
data, meta_data = ts.get_intraday(symbol='aapl',interval='1min', outputsize='full')

close_data = data['4. close'] 
last_price = close_data[0] 
print(last_price) 

#####sender_email = "blank@gmail.com" 
#####rec_email = "blank@gmail.com" 
###password = ("blank")
message = "AAPL STOCK ALERT!!! The stock is at above price you set " + "%.6f" % last_price 

target_sell_price = 140 
if last_price > target_sell_price:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password) 
    print("Login Success") 
    server.sendmail(sender_email, rec_email, message) 
    print("Email was sent") 
