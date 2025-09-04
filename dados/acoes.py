import yfinance as yf
from datetime import datetime
from matplotlib import pyplot as plt

end_data=datetime.now().strftime('%Y-%m-%d')
print(end_data)

bb= yf.Ticker('BBAS3.SA')
data_bb= bb.history(
    start= '2025-08-23',
    end = end_data
)
data_bb['Close'].plot()
plt.savefig('bb.png')