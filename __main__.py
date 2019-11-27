from Trade import Trade
from AggregateTrade import AggregateTrade
from Kline import Kline
from Ticker import Ticker
from BookTicker import BookTicker
from Database import Database
import BinanceManager

# load env
from dotenv import load_dotenv
load_dotenv()


db = Database()


def multi_process(msg):
    msg = msg['data']
    measurement = None

    if 'e' not in msg and 'u' in msg:
        measurement = BookTicker.msg_to_measurement(msg)
    else:
        event = msg['e']
        if 'aggTrade' in event:
            measurement = AggregateTrade.msg_to_measurement(msg)
        elif 'trade' in event:
            measurement = Trade.msg_to_measurement(msg)
        elif 'kline' in event:
            measurement = Kline.msg_to_measurement(msg)
        elif '24hrTicker' in event:
            measurement = Ticker.msg_to_measurement(msg)
        else:
            print(msg)

    if measurement is not None:
        db.store_measurement(measurement)


print("Open Binance API client...")
bm = BinanceManager.get_binance_websocket_manager()

print("Preparing symbols...")
symbols = BinanceManager.compute_symbols()
print(">>> " + ','.join(symbols))

print("Preparing streams...".format(len(symbols) * len(BinanceManager.stream_types)))
streams = BinanceManager.get_all_streams(symbols)
print(">>> {} streams".format(len(streams)))


print("Start streaming...")
bm.start_multiplex_socket(streams, multi_process)
bm.start()
print(">>> started")
