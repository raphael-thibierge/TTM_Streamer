import os
from binance.websockets import BinanceSocketManager
from binance.client import Client


stream_types = [
    'trade',
    'aggTrade',
    'ticker',
    'bookTicker',
    'kline_1m',
    'kline_5m',
    'kline_15m',
    'kline_30m',
    'kline_1h',
    'kline_6h',
    'kline_12h',
    'kline_1d',
    'depth'
]

def get_binance_client():
    key = os.getenv('BINANCE_API_KEY')
    secret = os.getenv('BINANCE_API_SECRET')
    if not key or not secret:
        raise Exception('Binance API credentials not found in \'.env\' file')

    return Client(key, secret)


def get_binance_websocket_manager():
    return BinanceSocketManager(get_binance_client())


def load_currencies():
    currencies = os.getenv('CURRENCIES')
    if not currencies:
        raise Exception('CURRENCIES not found in \'.env\' file')
    return currencies.split(',')


def load_references():
    references = os.getenv('REFERENCES')
    if not references:
        raise Exception('REFERENCES not found in \'.env\' file')
    return references.split(',')


def load_default_symbols():
    symbols = os.getenv('DEFAULT_SYMBOLS')
    if not symbols:
        return []
    return symbols.split(',')


def compute_symbols():
    currencies = load_currencies()
    references = load_references()
    symbols = load_default_symbols()

    for currency in currencies:
        if currency not in references:
            for reference in references:
                symbols.append(currency + reference)

    return symbols


def get_all_streams(symbols):
    streams = []
    for symbol in symbols:
        for stream_type in stream_types:
            streams.append('{}@{}'.format(symbol.lower(), stream_type))

    return streams
