from tda import auth, client
from tda.orders.common import OrderType
from tda.orders.generic import OrderBuilder
import json
import configtd
import datetime

#authenticate
try:
    c = auth.client_from_token_file(configtd.token_path, configtd.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path=configtd.chromedriver_path) as driver:
        c = auth.client_from_login_flow(
            driver, configtd.api_key, configtd.redirect_uri, configtd   .token_path)

#get price history for a symbol
r = c.get_price_history('ETEK',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)

print(json.dumps(r.json(), indent=4))
