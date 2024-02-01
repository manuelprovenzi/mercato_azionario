from aplhavantage import AP
import plotly.graph_objects as go
from secret import API_KEY
import matplotlib.pyplot as plt
#look polygon.io
def main():
    ap = AP(API_KEY)
    
    
    #menu cmd
    giorni = input("di quanti giorni vuoi il grafico? ")
    ticker = input("di che ticker? ")
    
    
    arrValori,arrDate = ap.getTickerList(ticker,int(giorni))

    
    open_data = [x[0] for x in arrValori]
    high_data = [x[1] for x in arrValori]
    low_data = [x[2] for x in arrValori]
    close_data = [x[3] for x in arrValori]

    # Crea il grafico a candela
    fig = go.Figure(data=[go.Candlestick(x=arrDate,
                                         open=open_data,
                                         high=high_data,
                                         low=low_data,
                                         close=close_data)])
    # Mostra il grafico
    fig.show()

if __name__=="__main__":
    main()