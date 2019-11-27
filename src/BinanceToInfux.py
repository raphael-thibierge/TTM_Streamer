from src import utils


def aggtrade_to_measurement(msg):
    return {
        'measurement': msg['e'],  # Event type
        'time': utils.timestamp_to_datetime(msg['T']),  # Trade time
        'tags': {
            's': msg['s'],      # Symbol
            'm': msg['m'],      # Is the buyer the market maker?
            'M': msg['M'],      # Ignore
        },
        'fields': {
            'a': msg['a'],      # Aggregate trade ID
            'p': msg['p'],      # Price
            'q': msg['q'],      # Quantity
            'f': msg['f'],      # First trade ID
            'l': msg['l'],      # Last trade ID
        },
    }


def bookticker_to_measurement(msg):
    return {
        'measurement': 'bookTicker',    # Event type
        'time': utils.datetime_now(),  # Event time
        'tags': {
            's': msg['s'],          # Symbol
        },
        'fields': {
            'u': msg['u'],          # order book updateId
            'b': msg['b'],          # best bid price
            'B': msg['B'],          # best bid qty
            'a': msg['a'],          # best ask price
            'A': msg['A'],          # best ask qty
        },
    }


def kline_to_measurement(msg):
    return {
        'measurement': msg['e'],    # Event type
        'time': utils.timestamp_to_datetime(msg['k']['t']),  # Kline start time
        'tags': {
            's': msg['s'],          # Symbol
            'i': msg['k']['i'],     # Interval
            'B': msg['k']['B'],     # Ignore
        },
        'fields': {
            'T': msg['k']['T'],     # Kline close time
            'f': msg['k']['f'],     # First trade ID
            'L': msg['k']['L'],     # Last trade ID
            'o': msg['k']['o'],     # Open price
            'c': msg['k']['c'],     # Close price
            'h': msg['k']['h'],     # High price
            'l': msg['k']['l'],     # Low price
            'v': msg['k']['v'],     # Base asset volume
            'n': msg['k']['n'],     # Number of trades
            'q': msg['k']['q'],     # Quote asset volume
            'V': msg['k']['V'],     # Taker buy base asset volume
            'Q': msg['k']['Q'],     # Taker buy quote asset volume
        },
    }


def ticker_to_measurement(msg):
    return {
        'measurement': msg['e'],    # Event type
        'time': utils.timestamp_to_datetime(msg['E']), # Event time
        'tags': {
            's': msg['s'],          # Symbol
        },
        'fields': {
            'p': msg['p'],          # Price change
            'P': msg['P'],          # Price change percent
            'w': msg['w'],          # Weighted average price
            'x': msg['x'],          # First trade(F)-1 price (first trade before the 24hr rolling window)
            'c': msg['c'],          # Last price
            'Q': msg['Q'],          # Last quantity
            'b': msg['b'],          # Best bid price
            'B': msg['B'],          # Best bid quantity
            'a': msg['a'],          # Best ask price
            'A': msg['A'],          # Best ask quantity
            'o': msg['o'],          # Open price
            'h': msg['h'],          # High price
            'l': msg['l'],          # Low price
            'v': msg['v'],          # Total traded base asset volume
            'q': msg['q'],          # Total traded quote asset volume
            'O': msg['O'],          # Statistics open time
            'C': msg['C'],          # Statistics close time
            'F': msg['F'],          # First trade ID
            'L': msg['L'],          # Last trade Id
            'n': msg['n'],          # Total number of trades
        },
    }


def trade_to_measurement(data):
    return {
        'measurement': data['e'],    # Event type
        'time': utils.timestamp_to_datetime(data['T']),  # Trade time
        'tags': {
            's': data['s'],          # Symbol
            'M': data['M'],          # Ignore
            'm': data['m'],          # Is the buyer the market maker?
        },
        'fields': {
            't': data['t'],          # Trade ID
            'p': data['p'],          # Price
            'q': data['q'],          # Quantity
            'b': data['b'],          # Buyer order ID
            'a': data['a'],          # Seller order ID
        },
    }


def depth_to_measurement(data):
    return {
        'measurement': data['e'],  # Event type
        'time': utils.timestamp_to_datetime(data['E']),  # Event time
        'tags': {
            's': data['s'],  # Symbol
        },
        'fields': {
            'U': data['U'],  # First update ID in event
            'u': data['p'],  # Final update ID in event
            'b': data['b'],  # Bids to be updated
            'a': data['a'],  # Asks to be updated
        },
    }