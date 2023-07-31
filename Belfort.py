import yfinance as yf
import datetime



def main():
        try:
                entry = yf.Ticker('AAPL')
                print(entry.info)
                
                getInfo(entry)
        except:
                timeOfDeath = datetime.datetime.now()
                print("There was an issue connecting to the Yahoo Servers at",timeOfDeath)

def getInfo(val):
        currentTime = datetime.datetime.now()
        selectCompany = ('AAPL')
        price = getPrice(selectCompany)
        print(price)

def getPrice(compPrice):
        sharePrice = entry.info["currentPrice"]
        return sharePrice


main()
