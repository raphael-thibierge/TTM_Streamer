import utils


class Ticker:

    @staticmethod
    def process(msg):
        print(Ticker.msg_to_measurement(msg))

    @staticmethod
    def msg_to_measurement(msg):
        """
            msg example
            {
                "e": "24hrTicker",  //
                "E": 123456789,     //
                "s": "BNBBTC",      //
                "p": "0.0015",      //
                "P": "250.00",      //
                "w": "0.0018",      //
                "x": "0.0009",      //
                "c": "0.0025",      //
                "Q": "10",          //
                "b": "0.0024",      //
                "B": "10",          //
                "a": "0.0026",      //
                "A": "100",         //
                "o": "0.0010",      //
                "h": "0.0025",      //
                "l": "0.0010",      //
                "v": "10000",       //
                "q": "18",          //
                "O": 0,             //
                "C": 86400000,      //
                "F": 0,             //
                "L": 18150,         //
                "n": 18151          //
            }
        """
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
