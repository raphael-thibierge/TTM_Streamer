import os
from influxdb import InfluxDBClient


class Database:

    def __init__(self):
        self.host = os.getenv('INFLUX_HOST')
        self.port = os.getenv('INFLUX_PORT')
        self.user = os.getenv('INFLUX_USER')
        self.password = os.getenv('INFLUX_PASSWORD')
        self.db_name = os.getenv('INFLUX_DATABASE')
        if not self.host or not self.port or not self.user or not self.password or not self.db_name:
            raise Exception('INFLUX env has missing values. Check \'.env.example\'')

        self.client = InfluxDBClient(self.host, self.port, self.user, self.password, self.db_name)

    def store_measurement(self, measure):
        self.client.write_points([measure])
