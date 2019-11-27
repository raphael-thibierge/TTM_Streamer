import utils


class BookTicker:

    @staticmethod
    def process(msg):
        for ticker in msg:
            print(BookTicker.msg_to_measurement(ticker))

    @staticmethod
    def msg_to_measurement(msg):
        """
            msg example
            {
                "u":400900217,     //
                "s":"BNBUSDT",     // symbol
                "b":"25.35190000", //
                "B":"31.21000000", //
                "a":"25.36520000", //
                "A":"40.66000000"  //
            }
        """
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
