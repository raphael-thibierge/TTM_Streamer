# load dependencies
from src.Database import Database
from src import BinanceManager, BinanceToInfux
from dotenv import load_dotenv


def multi_process(data):
    global db
    data = data['data']
    measurement = None

    if 'e' not in data and 'u' in data:
        measurement = BinanceToInfux.bookticker_to_measurement(data)
    else:
        event = data['e']
        if 'aggTrade' in event:
            measurement = BinanceToInfux.aggtrade_to_measurement(data)
        elif 'trade' in event:
            measurement = BinanceToInfux.trade_to_measurement(data)
        elif 'kline' in event:
            measurement = BinanceToInfux.kline_to_measurement(data)
        elif '24hrTicker' in event:
            measurement = BinanceToInfux.ticker_to_measurement(data)
        elif 'depthUpdate' in event:
            measurement = BinanceToInfux.depth_to_measurement(data)
        else:
            print(data)

    if measurement is not None:
        db.store_measurement(measurement)


load_dotenv()

db = Database()

print("Open Binance API client...")
bm = BinanceManager.get_binance_websocket_manager()

print("Preparing symbols...")
symbols = BinanceManager.get_symbols()
print(">>> " + ','.join(symbols))

print("Preparing streams...".format(len(symbols) * len(BinanceManager.stream_types)))
streams = BinanceManager.get_all_streams(symbols)
print(">>> {} streams".format(len(streams)))

print("Start streaming...")
bm.start_multiplex_socket(streams, multi_process)
bm.start()
print(">>> started")



