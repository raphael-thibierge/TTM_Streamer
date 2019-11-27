import utils


class MiniTicker:

    @staticmethod
    def process(msg):
        for ticker in msg:
            print(MiniTicker.msg_to_measurement(ticker))

    @staticmethod
    def msg_to_measurement(msg):
        """
            msg example
            {
                "e": "24hrMiniTicker",  //
                "E": 123456789,         //
                "s": "BNBBTC",          //
                "c": "0.0025",          //
                "o": "0.0010",          //
                "h": "0.0025",          //
                "l": "0.0010",          //
                "v": "10000",           //
                "q": "18"               //
            }
        """
        return {
            'measurement': msg['e'],    # Event type
            'time': utils.timestamp_to_datetime(msg['E']),  # Event time
            'tags': {
                's': msg['s'],          # Symbol
            },
            'fields': {
                'c': msg['c'],          # Close price
                'o': msg['o'],          # Open price
                'h': msg['h'],          # High price
                'l': msg['l'],          # Low price
                'v': msg['v'],          # Total traded base asset volume
                'q': msg['q'],          # Total traded quote asset volume
            },
        }
