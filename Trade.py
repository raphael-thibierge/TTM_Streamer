import utils


class Trade:

    @staticmethod
    def process(msg):
        print(Trade.msg_to_measurement(msg))

    @staticmethod
    def msg_to_measurement(msg):
        """
            msg example
            {
                "e": "trade",     //
                "E": 123456789,   // Event time
                "s": "BNBBTC",    //
                "t": 12345,       //
                "p": "0.001",     //
                "q": "100",       //
                "b": 88,          //
                "a": 50,          //
                "T": 123456785,   //
                "m": true,        //
                "M": true         //
            }
        """
        return {
            'measurement': msg['e'],    # Event type
            'time': utils.timestamp_to_datetime(msg['T']),  # Trade time
            'tags': {
                's': msg['s'],          # Symbol
                'M': msg['M'],          # Ignore
                'm': msg['m'],          # Is the buyer the market maker?
            },
            'fields': {
                't': msg['t'],          # Trade ID
                'p': msg['p'],          # Price
                'q': msg['q'],          # Quantity
                'b': msg['b'],          # Buyer order ID
                'a': msg['a'],          # Seller order ID
            },
        }
