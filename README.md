# VICINITY OpenHAB Adapter IKEA Light

Adapter used to connect the IKEA light to the adapter and expose it to the VICINITY neighborhood.
This adapter is currently a quick fix for HITS use case and is not planned to have a continuous development.
The adapter does however give a good starting point for developing support for multiple light bulbs.
## Prerequisites

Before running this adapter, ensure that you have the following in place:

- Python 3.6.5+ 
    ###### Ubuntu 14.04 and 16.04: <br>
    `$ sudo add-apt-repository ppa:deadsnakes/ppa`<br>
    `$ sudo apt-get update`<br>
    `$ sudo apt-get install python3.6`<br> 
    ###### Ubuntu 17.10
    comes with a pre-installed 3.6, use `python3` to invoke it
    ###### Windows 10
    Download binary from: https://www.python.org/downloads/ <br>
    Make sure to update your Environment Variables

- PostgreSQL 9.6+
    ###### Ubuntu 17.04 - 17.10
    `$ sudo apt-get install postgresql-9.6` <br>
    
## Installation
1. Clone this repository using `git clone` <br>

2. Inside the project directory run `pip install -r requirements.txt` to install the necessary requirements

Inside the project directory run <br>
`$ python manage.py makemigrations`<br>
`$ python manage.py migrate`<br>

## Run

Run the adapter on a port of your choice 

`$ python manage.py runserver <your_host>:<your_port>`

Example:

`$ python manage.py runserver 127.0.0.1:9000`



