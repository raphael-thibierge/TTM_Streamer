import utils


class AggregateTrade:

    @staticmethod
    def process(msg):
        print(AggregateTrade.msg_to_measurement(msg))

    @staticmethod
    def msg_to_measurement(msg):
        """
            msg example
            {
                "e": "aggTrade",  //
                "E": 123456789,   // Event time  --> not used
                "s": "BNBBTC",    //
                "a": 12345,       //
                "p": "0.001",     //
                "q": "100",       //
                "f": 100,         //
                "l": 105,         //
                "T": 123456785,   //
                "m": true,        //
                "M": true         //
            }
        """
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
