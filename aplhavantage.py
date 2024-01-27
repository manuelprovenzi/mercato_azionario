class AP:
    api_key="demo"
    def __init__(self,api):
        self.api_key=api
        pass
    def getTickerList(self,ticker):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={self.api_key}"
        pass