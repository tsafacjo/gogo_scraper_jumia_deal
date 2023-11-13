#!/bin/bash

echo "start $0"

pwd 

ls



pid=$$ 

echo "start $pid"


scrapy crawl jumia_car -o jumia_carwspapers_$(date +'%m-%d-%Y').csv -t json
