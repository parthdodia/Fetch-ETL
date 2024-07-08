from PSQL_client import PSQL_client
from SQSHandler import SQSHandler
from Mask import Mask

# Create a connections to the SQS queue and PostgreSQL database
queue = SQSHandler()
queue.connect()

db = PSQL_client()
db.connect()

#Mask sensitive data
mask = Mask()

print("\n Executed!")  

db.drop_table()
print('\n Table dropped') 

# Continue reading from the SQS queue until no more messages are available
while queue.read_queue() is not None:
    for response in mask.mask(queue.read_queue()):
        db.add_data(response)

queue.disconnect()
db.disconnect()