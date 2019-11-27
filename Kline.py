import utils


class Kline:

    @staticmethod
    def process(msg):
        if msg['k']['x'] is True:
            print(Kline.msg_to_measurement(msg))

    @staticmethod
    def msg_to_measurement(msg):
        """
            msg example
            "e": "kline",     //
            "E": 123456789,   // Event time --> not used
            "s": "BNBBTC",    //
            "k": {
                "t": 123400000, //
                "s": "BNBBTC",  //
                "i": "1m",      //
                "T": 123460000, //
                "f": 100,       //
                "L": 200,       //
                "o": "0.0010",  //
                "c": "0.0020",  //
                "h": "0.0025",  //
                "l": "0.0015",  //
                "v": "1000",    //
                "n": 100,       //
                "q": "1.0000",  //
                "V": "500",     //
                "Q": "0.500",   //
                "x": false,     // Is this kline closed?
                "B": "123456"   //
            }
        """
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
