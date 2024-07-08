#  ETL off a SQS Queue

This project aims to develop a scalable and secure solution to read messages from an Amazon Simple Queue Service (SQS) queue, mask Personally Identifiable Information (PII) data, and store the masked data in a PostgreSQL database. The solution should be able to handle a growing dataset and ensure data integrity and security.


## Project Structure:

- **main.py**: The main application script that reads messages from the SQS queue, masks PII data, and writes to the PostgreSQL database.<br>
- **requirements.txt**: Lists the dependencies required to run the application.<br>
- **docker-compose.yml**: Used to run the application and PostgreSQL database using Docker Compose.<br>
- **exe.py**: Used to install the dependencies and build docker containers for the application


## Prerequisites, Setup and Execution:

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
git clone https://github.com/parthdodia/Fetch-ETL.git
```
- Open your terminal and go in the directory of this project. Simply run this file.
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
- You will see the data extracted from SQS queue and loaded into the database. <br>


## How it Works:

- The exe.py script installs the required dependencies. It also runs the .yml file that extracts the custom docker image and creates a container for them.
- The main.py script calls other classes that read the messages from SQS queue, mask the required attributes, and store the masked data in a PostgreSQL database.


## Contributing:

- Contributions are welcome! Please submit a pull request with your changes.<br>
- Please ensure that your changes are tested and follow the project's coding standards.<br>


