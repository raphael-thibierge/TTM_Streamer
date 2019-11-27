# load dependencies
from src.Database import Database
from src import BinanceManager, BinanceToInfux
from dotenv import load_dotenv

load_dotenv()

db = Database()

symbols = BinanceManager.get_symbols()
books = {}

for symbol in symbols:
    books[symbol] = {
        'bids': {},
        'asks': {},
    }

client = BinanceManager.get_binance_client()
ws_manager = BinanceManager.get_binance_client()

def process(msg):
    pass


ws_manager.start_multiplex_socket(
    [symbol+"@depth" for symbol in symbols],
    process
)
ws_manager.start()
