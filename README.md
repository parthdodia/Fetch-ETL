#  ETL off a SQS Queue

This project aims to develop a scalable and secure solution to read messages from an Amazon Simple Queue Service (SQS) queue, mask Personally Identifiable Information (PII) data, and store the masked data in a PostgreSQL database. The solution should be able to handle a growing dataset and ensure data integrity and security.


## Project Structure:

- **main.py**: The main application script that reads messages from the SQS queue, masks PII data, and writes to the PostgreSQL database.<br>
- **requirements.txt**: Lists the dependencies required to run the application.<br>
- **docker-compose.yml**: Used to run the application and PostgreSQL database using Docker Compose.<br>
- **exe.py**: Used to install the dependencies and build docker containers for the application


## Prerequisites, Setup and Installation:

- Prerequisites on your computer:
  - python 3.9 or higher
  - awscli :
  ```bash
   pip install awscli-local
  ```
  - [Docker](https://docs.docker.com/get-docker/)
  - docker-compose
  - [PSQL](https://www.postgresql.org/download/)
- Clone the repository:
```bash
git clone https://github.com/parthdodia/Fetch-ETL.git`
```
- Open your terminal and go the directory of this project. Simply run this file.
```bash
python exe.py
```
- Run the following command to verify connection with SQS:
```bash
awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue
```
- Open a new terminal window with same directory and run the main file.
```bash
python main.py
```
- Connect to the database
```bash
psql -d postgres -U postgres -p 5432 -h localhost -W
```
- Enter the password : `password`. You will see something like this : `postgres=# `. Write your query here
```bash
select * from user_logins;
```
- You will see the data extracted from SQS queue and loaded into the database.


## How it Works:

- The script.py script reads messages from the SQS queue using the boto3 library.<br>
- Each message is parsed as JSON and the PII attributes `device_id and ip` are masked using the hashlib library.<br>
- The masked data is then written to the PostgreSQL database using the psycopg2 library.<br>
- The script continues to read messages from the queue until the queue is empty, at which point it sleeps for a short period before checking the queue again. <br>


## Configuration:

- **sqs_queue_url**: The URL of the SQS queue to read from. <br>
- **postgres_conn**: The connection details for the PostgreSQL database. <br>
- **masked_fields**: A list of fields to mask in the PII data. <br>


## Security:

- The PII data is masked using a SHA-256 hash, making it irreversible and secure. <br>
- The PostgreSQL database is used to store the masked data, ensuring data integrity and security.<br>


## Scalability:

- The application is designed to handle a growing dataset by using a message queueing system (SQS) and a scalable database (PostgreSQL).<br>
- The application can be easily scaled horizontally by adding more instances of the application.<br>


## Testing:

- The application has been tested using a local SQS queue and PostgreSQL database.<br>
- The testing process involved sending sample messages to the SQS queue and verifying that the data was correctly masked and stored in the PostgreSQL database.<br>


## Contributing:

- Contributions are welcome! Please submit a pull request with your changes.<br>
- Please ensure that your changes are tested and follow the project's coding standards.<br>


