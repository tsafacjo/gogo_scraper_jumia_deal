FROM python:3.8.3
 
WORKDIR /app
COPY . /app

RUN pip3 install Scrapy
RUN pip3 install boto
RUN pip3 install botocore
#RUN pip3 install --no-cache-dir -r requirements.txt
 
CMD ["scrapy", "crawl", "jumia_car"] 