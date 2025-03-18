from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# influxdb
url = "http://localhost:8086"
token = "NXVH9ZsoTPVAK851CKZXBIdEwSNfvflhKHpmN8PUwx25gRbz-T5asKrRg3I2VcZjR1bOFyVUA0R9QSwhR5zYiQ=="
bucket = "mybucket"
org = "RWTH"

# General client
client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

# Write client
write_api = client.write_api(write_options=SYNCHRONOUS)
p = Point("my_measurement").tag("tagkey", "tagvalue").field("value", 25.9)
write_api.write(bucket=bucket, org=org, record=p)