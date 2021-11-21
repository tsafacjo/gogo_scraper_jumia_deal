import scrapy
#from tutorial import  PostItem
from datetime import datetime
from tutorial.items import PostItem

class QuotesSpider(scrapy.Spider):
    name = "jumia"
    root_url="https://www.jumia.cm/"

    def start_requests(self):

        urls = ["https://www.jumia.cm/immobilier"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        main parse
        """
        # get  all the single post
        posts = response.css("a.post-link")

        for post in posts :
           ## print("short url "+post.attrib['href']) 
            yield scrapy.Request(self.root_url+"/"+post.attrib['href'], callback=self.parse_post)
        #pagination 
        #next_url=""
        ##self.parse(next_url)
        pages =response.css("ul.pagination li a::text")

        print("nb articles  "+str(len(pages)))
        print("last element  "+str(pages[-2].get()))
        return 
        for page in pages[0:3] :
            print("url "+page.attrib['href'])
            yield scrapy.Request(self.root_url+"/"+page.attrib['href'], callback=self.parse)


    def parse_pagination(self, response):
        for post in posts :
           ## print("short url "+post.attrib['href']) 
            yield scrapy.Request(self.root_url+"/"+post.attrib['href'], callback=self.parse_post)
        print(" "+str(response.css("h1 span::text").get()))

    def parse_post(self, response):
  
        return PostItem(id = response.url,
		title = str(response.css("h1 span::text").get()),
		description = response.css("div.post-text-content p::text").get(),
        town = response.css("dd span::text")[1].get(),
        category = response.css("nav ul  li a span::text")[7].get(),
        transactionType =  response.css("h3 span::text")[0].get(),
        area=  response.css("h3 span::text")[1].get()  if response.css("h3 span::text")[0].get() in ["vente"] else response.css("h3 span::text")[2].get(),
        publishedDate = str(datetime.now().year)+response.css("dd time::text")[0].get().replace("Aujourd'hui",datetime.today().strftime("%b. %d")),
        price =  response.css("aside span span")[0].attrib['content'],
        priceCurency = response.css("aside span span")[1].attrib['content'], 
        phoneNumber = response.css("div.phone-box a::text")[0].get(),
        url = response.url
            )

 