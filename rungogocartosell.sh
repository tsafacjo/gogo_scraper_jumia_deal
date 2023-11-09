#!/bin/bash

echo "start $0"

cd /home/tsafacjo/Documents/workspace/gogoScraper

pwd 

pid=$$ 

echo "start $pid"


scrapy crawl jumia_car -o jumia_carwspapers_$(date +'%m-%d-%Y').csv -t json
