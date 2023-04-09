---
title: FastAPI
description: A FastAPI server
tags:
  - fastapi
  - python
---


venv2\Scripts\activate 

uvicorn main:app --reload

ngrok http 8000

 haiyore nyaruko-san


 Run your FastAPI application using the uvicorn server with the following command: uvicorn main:app --host 0.0.0.0 --port 80


# FastAPI Example

This example starts up a [FastAPI](https://fastapi.tiangolo.com/) server.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Frailwayapp-starters%2Ffastapi)
## ✨ Features

- FastAPI
- Python 3

## 💁‍♀️ How to use

- Deploy using the button 👆
- Clone locally and install packages with Pip using `pip install -r requirements.txt` or Poetry using `poetry install`
- Connect to your project using `railway link`
- Run locally using `uvicorn main:app --reload`

## 📝 Notes

- To learn about how to use FastAPI with most of its features, you can visit the [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/).
- FastAPI provides automatic documentation to call and test your API directly from the browser. You can access it at `/docs` with [Swagger](https://github.com/swagger-api/swagger-ui) or at `/redoc` with [Redoc](https://github.com/Rebilly/ReDoc).



ec2 




direccion de ec2  momentanea http://13.58.125.222/docs#/


https://www.youtube.com/watch?v=SgSnz7kW-Ko video explicando

FastAPI Tutorial
This is a simple example FastAPI application that pretends to be a bookstore.

Deploying to AWS EC2
Log into your AWS account and create an EC2 instance (t2.micro), using the latest stable Ubuntu Linux AMI.

SSH into the instance and run these commands to update the software repository and install our dependencies.

-sudo apt-get update
-sudo apt install -y python3-pip nginx

Clone the FastAPI server app https://github.com/WilsonRock/FastAPIDownloader.git


Add the FastAPI configuration to NGINX's folder. Create a file called fastapi_nginx (like the one in this repository).

sudo vim /etc/nginx/sites-enabled/fastapi_nginx
And put this config into the file (replace the IP address with your EC2 instance's public IP):

server {
    listen 80;   
    server_name <YOUR_EC2_IP>;    
    location / {        
        proxy_pass http://127.0.0.1:8000;    
    }
}
Start NGINX.

-sudo service nginx restart
Start FastAPI.

configurar env pytrhon

sudo apt-get install virtualenv2
sudo apt install python3-virtualenv   

virtualenv venv2  intentar este o el sgte para activar el entorno virtual

source venv2/Scripts/activate



python3 -m uvicorn main:app
Update EC2 security-group settings for your instance to allow HTTP traffic to port 80.

Now when you visit your public IP of the instance, you should be able to access your API.

Deploying FastAPI to AWS Lambda
We'll need to modify the API so that it has a Lambda handler. Use Mangum:

from mangum import Mangum

app = FastAPI()
handler = Mangum(app)
We'll also need to install the dependencies into a local directory so we can zip it up.

pip install -t lib -r requirements.txt
We now need to zip it up.

(cd lib; zip ../lambda_function.zip -r .)
Now add our FastAPI file and the JSON file.

zip lambda_function.zip -u main.py
zip lambda_function.zip -u books.json

