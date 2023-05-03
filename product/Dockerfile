FROM python:3.8
   
ENV PYTHONUNBUFFERED 1  

ENV DockerHOME=/home/hamza/Desktop/wor/product/product/.env

RUN mkdir -p $DockerHOME  

WORKDIR $DockerHOME  

ENV PYTHONDONTWRITEBYTECODE 1


RUN pip install --upgrade pip  

COPY . $DockerHOME  
RUN pip install -r requirements.txt  
EXPOSE 8000  
CMD python manage.py runserver  