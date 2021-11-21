FROM python:3.8
 
WORKDIR /app
COPY . /app
 
RUN pip install scrapy
 
ENTRYPOINT ["scrapy crawl "]
CMD ["jumia"]
