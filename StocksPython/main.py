# This is a sample Python script.
import yfinance as yf
import pprint
import utils



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    AAL = yf.Ticker("AAL")
    pprint.pp(AAL.info)
    AAL_History = AAL.history(period="2y")
    AAL_History = utils.moving_average(AAL_History, 200)
    AAL_History = utils.moving_average(AAL_History, 50)
    
    print(AAL_History)



