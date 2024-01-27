from aplhavantage import AP
from secret import API_KEY
import matplotlib.pyplot as plt
#look polygon.io
def main():
    ap = AP(API_KEY)
    
    
    #menu cmd
    giorni = input("di quanti giorni vuoi il grafico? ")
    ticker = input("di che ticker? ")
    
    
    arrValori,arrDate = ap.getTickerList(ticker,int(giorni))

    # Crea il grafico
    plt.plot(arrDate, arrValori, marker='o', linestyle='-', color='b')

    # Aggiungi etichette agli assi e un titolo
    plt.xlabel('Date')
    plt.ylabel('Valori più alti')
    plt.title("ticker:"+ticker)

    # Aggiungi una griglia
    plt.grid(True)

    # Rotazione delle etichette sull'asse x per una migliore leggibilità
    plt.xticks(rotation=45)

    # Mostra il grafico
    plt.show()
    

if __name__=="__main__":
    main()