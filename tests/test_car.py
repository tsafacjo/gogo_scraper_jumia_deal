import unittest
from unittest.mock import patch
from scrapy.http import HtmlResponse, Request
from gogoscraper.spiders.jumiadeals_car import QuotesSpider, VehiculescrapyItem

class TestQuotesSpider(unittest.TestCase):

    def setUp(self):
        self.spider = QuotesSpider()

    @patch('scrapy.Request')
    def test_start_requests(self, mock_request):
        start_requests = list(self.spider.start_requests())
        self.assertEqual(len(start_requests), 1)
        mock_request.assert_called_with(url="https://www.jumia.cm/vehicules", callback=self.spider.parse)

    def test_parse(self):
        html = """
        <html>
            <body>
                <a class="post-link" href="/vehicle1"></a>
                <a class="post-link" href="/vehicle2"></a>
                <!-- Add more HTML elements as needed for testing -->
            </body>
        </html>
        """
        request = Request(url="https://www.jumia.cm/vehicules")
        response = HtmlResponse(url=request.url, body=html, encoding='latin', request=request)
        parse_results = list(self.spider.parse(response))
        #self.assertEqual(len(parse_results), 2)  # Assuming there are two posts
        # Add more assertions to check if parse_results contains the expected data

    def test_parse_post(self):
        html = """
        <html>
            <body>
                <h1><span>Vehicle Title</span></h1>
                <div class="post-text-content"><p>Vehicle Description</p></div>
                <dd><span>Town Name</span></dd>
                <main>
                    <div>
                        <nav>
                            <ul>
                                <li><a><span>Vehicle Category</span></a></li>
                            </ul>
                        </nav>
                    </div>
                </main>
                <h3><span>Transaction Type</span></h3>
                <dd><time>Published Date</time></dd>
                <aside>
                    <span><span content="Price">Price Value</span></span>
                </aside>
                <div class="phone-box"><a>Phone Number</a></div>
                <div class="new-attr-style">
                    <h3><span><a>Vehicle Mark</a></span></h3>
                    <span>Vehicle Model</span>
                    <span>Transmission Type</span>
                    <span>Fuel Type</span>
                    <span>Year</span>
                    <span>Kilometer Count</span>
                </div>
                <div>
                    <dl>
                        <span>Seller Name</span>
                    </dl>
                </div>
            </body>
        </html>
        """
        request = Request(url="https://www.jumia.cm/vehicle1")
        response = HtmlResponse(url=request.url, body=html, encoding='utf-8', request=request)
        item = next(self.spider.parse_post(response))

        self.assertIsInstance(item, VehiculescrapyItem)  # Replace with the actual item class
        self.assertEqual(item['title'], 'Vehicle Title')
        self.assertEqual(item['description'], 'Vehicle Description')
        self.assertEqual(item['town'], 'Town Name')
        self.assertEqual(item['category'], 'Vehicle Category')
        self.assertEqual(item['transactionType'], 'Transaction Type')
        self.assertEqual(item['publishedDate'], 'Published Date')
        self.assertEqual(item['price'], 'Price Value')
        self.assertEqual(item['phoneNumber'], 'Phone Number')
        self.assertEqual(item['mark'], 'Vehicle Mark')
        self.assertEqual(item['model'], 'Vehicle Model')
        self.assertEqual(item['transmission'], 'Transmission Type')
        self.assertEqual(item['carburant'], 'Fuel Type')
        self.assertEqual(item['annee'], 'Year')
        self.assertEqual(item['kilometrage'], 'Kilometer Count')
        self.assertEqual(item['seller'], 'Seller Name')
        self.assertEqual(item['url'], 'https://www.jumia.cm/vehicle1')
        # Add more assertions if necessary

if __name__ == '__main__':
    unittest.main()
