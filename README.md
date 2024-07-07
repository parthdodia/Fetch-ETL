#  ETL off a SQS Queue

This project aims to develop a scalable and secure solution to read messages from an Amazon Simple Queue Service (SQS) queue, mask Personally Identifiable Information (PII) data, and store the masked data in a PostgreSQL database. The solution should be able to handle a growing dataset and ensure data integrity and security.

## Project Structure:

script.py: The main application script that reads messages from the SQS queue, masks PII data, and writes to the PostgreSQL database.
requirements.txt: Lists the dependencies required to run the application.
docker-compose.yml: Used to run the application and PostgreSQL database using Docker Compose.

## Setup and Installation:

Clone the repository: git clone https://github.com/your-username/pii-data-masking.git
Install the dependencies: pip install -r requirements.txt
Create a PostgreSQL database and update the postgres_conn variable in script.py with the correct credentials.
Create an SQS queue and update the sqs_queue_url variable in script.py with the correct URL.
Run the application using Docker Compose: docker-compose up

## How it Works:

The script.py script reads messages from the SQS queue using the boto3 library.
Each message is parsed as JSON and the PII data (device_id and ip) is masked using the hashlib library.
The masked data is then written to the PostgreSQL database using the psycopg2 library.
The script continues to read messages from the queue until the queue is empty, at which point it sleeps for a short period before checking the queue again.

## Configuration:

sqs_queue_url: The URL of the SQS queue to read from.
postgres_conn: The connection details for the PostgreSQL database.
masked_fields: A list of fields to mask in the PII data.

## Security:

The PII data is masked using a SHA-256 hash, making it irreversible and secure.
The PostgreSQL database is used to store the masked data, ensuring data integrity and security.

##Scalability:

The application is designed to handle a growing dataset by using a message queueing system (SQS) and a scalable database (PostgreSQL).
The application can be easily scaled horizontally by adding more instances of the application.

## Testing:

The application has been tested using a local SQS queue and PostgreSQL database.
The testing process involved sending sample messages to the SQS queue and verifying that the data was correctly masked and stored in the PostgreSQL database.

## Contributing:

Contributions are welcome! Please submit a pull request with your changes.
Please ensure that your changes are tested and follow the project's coding standards.


