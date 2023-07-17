from influxdb import InfluxDBClient

influxdb_client = InfluxDBClient(

    host='https://us-east-1-1.aws.cloud2.influxdata.com/orgs/21a7613931f3ea65/load-data/tokens',
    port=8086,
    username='mazlan237@graduate.utm.my',
    password='passwordis123',
    database='waterlevel'
)

def write_data_to_influxdb(measurement, fields, tags=None):

    json_body = [{
        'measurement': measurement,
        'tags': tags or {},
        'fields': fields,
    }]
    influxdb_client.write_points(json_body)
