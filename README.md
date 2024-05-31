Computer Components API
--> Introduction
The Computer Components API is a RESTful API built with Python using the Scrapy framework for web scraping and Flask for creating the API endpoints.
It allows users to retrieve information about computer components such as processors, GPUs, motherboards, and RAM from a SQLite database.

--> Installation
To set up the project, follow these steps:

--> Clone the repository:

git clone https://github.com/your-username/computer-components-api.git
Navigate to the project directory:

--> Install the required dependencies:
pip install -r requirements.txt
Set up the SQLite database


-->Once the project is set up, you can start the Flask server by running:

python app.py

--> The API will be accessible at http://127.0.0.1:5000/computers.


GET /computers: Retrieve a list of computer components.

Example:
http://127.0.0.1:5000/computers?processor=&gpu=&motherboard=&ram
JSON Schema
The API returns data in the following JSON format:

json

[
    {
        "gpu": "Intel UHD Graphics 730",
        "motherboard": "от 8GB до 32GB DDR4",
        "processor": "Intel Core i3-13100",
        "ram": "от 512GB SSD NVMe до 4TB (SSD NVMe и HDD)"
    },
    {
        ...
    }
]
