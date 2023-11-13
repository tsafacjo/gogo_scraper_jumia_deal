import scrapy
import os
#from tutorial import  PostItem
from datetime import datetime,timedelta
from gogoscraper.items import VehiculescrapyItem

class QuotesSpider(scrapy.Spider):
    name = "jumia_car"
    root_url="https://www.jumia.cm/vehicules"
    raw_root_url="https://www.jumia.cm"
    is_yesterday_reached=False
    is_first_run=False

    def start_requests(self):

        
        print("test "+os.environ.get("AWS_ACCESS_KEY_ID","vide"))

        print("test "+os.environ.get("AWS_SECRET_ACCESS_KEY","vide"))

        urls = ["https://www.jumia.cm/vehicules"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        main parse
        """
        # keywords
        category="vehicule"
        # get  all the single post
        posts = response.css("a.post-link")

        for post in posts :
           ## print("short url "+post.attrib['href']) 
            yield scrapy.Request(self.raw_root_url+"/"+post.attrib['href'], callback=self.parse_post)

                    # if we reach yesterday we skip the processing
        #pagination 
        #next_url=""
        ##self.parse(next_url)
        pages =response.css("ul.pagination li a::text")

        print("nb articles  "+str(len(pages)))
        print("last element  "+str(pages[-2].get()))

        # if we reach yesterday we skip the processing
        #if self.is_yesterday_reached :
        #    return
        # we  avoid infinite loop
        if QuotesSpider.is_first_run :
            pass
        else :    
          QuotesSpider.is_first_run= True    
          for page_number in   range(0,35): #int(pages[-2].get())):#range(0,int(pages[-2].get())):
                print("Yesterday  **"+str(self.is_yesterday_reached))
                print("url "+self.root_url+"/"+category+"?page="+str(page_number))
                yield scrapy.Request(self.root_url+"/"+"?page="+str(page_number), callback=self.parse)
                # if we reach yesterday we skip the processing


    def parse_pagination(self, response):
        for post in posts :
           ## print("short url "+post.attrib['href']) 
           print("ici **")
           yield scrapy.Request(self.raw_root_url+"/"+post.attrib['href'], callback=self.parse_post)
        print(" "+str(response.css("h1 span::text").get()))

    def parse_post(self, response):

        
        # if we reach limit we quit
        #         if "Hier" in str(datetime.now().year)+response.css("dd time::text")[0].get()  or  "Aujourd'hui" not  in str(datetime.now().year)+response.css("dd time::text")[0].get() :
        #             self.is_yesterday_reached =True
        # 
        #             return
        length_info = len(response.css("div.new-attr-style h3 span::text")) 
        return VehiculescrapyItem(
        id = response.url,
		title = str(response.css("h1 span::text").get()),
		description = response.css("div.post-text-content p::text").get(),
        town = response.css("dd span::text")[1].get(),
        category = response.css("main div nav ul  li a span::text")[6].get(),
        transactionType =  response.css("h3 span::text")[0].get(),
        publishedDate = response.css("dd time::text")[0].get(), #str(datetime.now().year)+response.css("dd time::text")[0].get().replace("Aujourd'hui",datetime.today().strftime("%b. #%d")).replace("Hier",(datetime.today()- timedelta(days=1)).strftime("%b. %d")),
        price =  response.css("aside span span")[0].attrib['content'],
        priceCurency = response.css("aside span span")[1].attrib['content'], 
        phoneNumber = response.css("div.phone-box a::text")[0].get(),
        mark = response.css("div.new-attr-style h3 span a::text")[0].get(),
        model = response.css("div.new-attr-style h3 span::text")[0].get(),
        transmission =  response.css("div.new-attr-style h3 span::text")[1].get(),
        carburant=  response.css("div.new-attr-style h3 span::text")[2].get(),
        annee = response.css("div.new-attr-style h3 span::text")[3].get(),
        kilometrage =    response.css("div.new-attr-style h3 span::text")[4].get() if length_info>= 5 else '',
        seller = response.css("div dl  span::text ")[0].get(),
        url = response.url
            )
