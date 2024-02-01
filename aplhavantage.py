import requests
from datetime import datetime, timedelta

#"1. open": "187.7100",
#2. high": "188.6500",
# "3. low": "186.7700"
#"4. close": "187.8700",
#"5. volume": "4575058"

class AP:
    api_key="demo"
    def __init__(self,api):
        self.api_key=api
        pass
    def getTickerList(self,ticker,num_days):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={self.api_key}"
        response=requests.get(url)
        data = response.json()
        time_series_daily = data["Time Series (Daily)"]
        arrValue=[]
        arrDate=[]
        errors = []
        # Data di partenza
        start_date= datetime.today()

        # Ciclo che itera all'indietro nelle date
        for i in range(0,num_days):
            current_date = start_date - timedelta(days=i)
            current_date_str = current_date.strftime("%Y-%m-%d")

            # Verifica se la data esiste nel tuo JSON
            if current_date_str in time_series_daily:
                open = float(time_series_daily[current_date_str]["1. open"])
                high = float(time_series_daily[current_date_str]["2. high"])
                low = float(time_series_daily[current_date_str]["3. low"])
                close = float(time_series_daily[current_date_str]["4. close"])
                
                
                arrValue.append(("{:.2f}".format(open),"{:.2f}".format(high),"{:.2f}".format(low),"{:.2f}".format(close)))
                
                arrDate.append(current_date)
                
            else:
                errors.append(current_date_str)
                
        return arrValue,arrDate