# gogoScraper

This a simple python scraper to get different jumia  deal information using scrapy

## Architecture 

![Architecture de gogo car trends ](imag/gogo_car_analyzer.jpg "Architecture")


## Build:

 docker build -t tsafacjo/jumia-car-scrap --platform linux/arm64 .
 
 docker tag tsafacjo/jumia-car-scrap  tsafacjo/jumia-car-scrap:0.2

 docker push tsafacjo/jumia-car-scrap:0.2   



