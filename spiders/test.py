from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http.request import Request
from bs4 import BeautifulSoup
from project.items import ProjectItem
import re
from pattern.web import plaintext
from scrapy.selector import HtmlXPathSelector
import requests
from scrapy.selector import Selector
class PagesSpider(CrawlSpider):
    """
    the Page Spider for wikipedia
    """

    name = "pro"
    #allowed_domains = ["wikipedia.org"]

    start_urls = ['https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/?fn=new+delhi&fcc=IN&tn=chandigarh&tcc=IN&sort=trip_date&order=asc&limit=10&page=%s' % page for page in xrange(1,15)]
    

    rules = (
        Rule(LinkExtractor(),
             callback='parse_page',
             # hook to be called when this Rule generates a Request
             process_request='parse'),
    )

   
    def parse(self, response):
     sel = Selector(response)
     #hxs = HtmlXPathSelector(response)
     #li = hxs.xpath("//a[@class='trip-search-oneresult js-tracktor-search-result']")
     f = open('csvfile.csv','a')
     for href in sel.xpath("//a[@class='trip-search-oneresult js-tracktor-search-result']/@href").extract():
      a = "https://www.blablacar.in%s"%href
      
      
      #print a 
      #for l in a:
      r = requests.get(a)
      hxs = HtmlXPathSelector(r)
      hxs2 = Selector(r)
      #for source in hxs2.xpath("//span[@class='RideName-location RideName-location--arrowAfter']/text()").extract():
      source = hxs.xpath("//span[@class='RideName-location RideName-location--arrowAfter']/text()").extract()[0]
      if source:

       print '\nsource : %s'%source.strip()
       f.write('\nsource : %s'%source.strip())
      else:
       pass
      destination =  hxs.xpath("//span[@class='RideName-location RideName-location--arrowAfter']/following-sibling::node()/text()").extract()[0]
      if destination:
       print destination.strip()
      
       f.write('\ndestination : %s'%destination.strip())
      else:
       pass
      for prices in hxs.xpath("//span[@class='Booking-price u-block'][1]/text()").extract():
        price =  prices[1:-1]
        print '\nprice : %s'%price.strip()
        f.write('\nprice : %s'%price.strip())
      else:
        pass
      departuredate = hxs.xpath("//strong[@class='RideDetails-infoValue']/span/text()").extract()[0]
      if departuredate:
       print '\ndeparturedate : %s' %departuredate.strip()
       f.write('\ndeparturedate : %s'%departuredate.strip())
      else:
       pass
      departurepoint = hxs.xpath("//span[@class='RideDetails-infoValue RideDetails-infoValue--clickable tip js-display-map']/span/text()").extract()
      if departurepoint:
       d = departurepoint[0]
       print '\ndeparturepoint : %s'%d.strip()
       f.write('\ndeparturepoint : %s'%d.strip())
      else:
       pass
      departure = hxs.xpath("//span[@class='RideDetails-infoValue RideDetails-infoValue--clickable tip js-display-map']/span/text()").extract()
      if departure:
       d2 = departure[1]
       print '\ndropoffpoint : %s'%d2.strip()
       f.write('\ndropoffpoint : %s'%d2.strip())
      else:
       pass
      avail = hxs.xpath("//span[@class='Booking-seats u-block']//text()").extract()[0]
      if avail:
       print '\nseats_left : %s'%avail.strip()
       f.write('\nseats_left : %s'%avail.strip())
      else:
       pass
      photo = hxs.xpath("//a[@class='PhotoWrapper PhotoWrapper--medium']//img/@src").extract()[0]
      if photo:
       print '\ncar_owner_image  : %s'%photo.strip()
       f.write('\ncar_owner_image  :  %s'%photo.strip())
      else:
       pass
      name = hxs2.xpath("//h4[@class='ProfileCard-info ProfileCard-info--name u-truncate']/a/text()").extract()[0]
      if name:
       print '\ncar_owner_name  : %s'%name.strip()
       f.write('\ncar_owner_name  : %s'%name.strip())
      else:
       pass
      age = hxs2.xpath("//div[@class='ProfileCard-info']//text()").extract()[0]
      if age:
       print '\ncar_owner_age  : %s'%age.strip()
       f.write('\ncar_owner_age  : %s'%age.strip())
      else:
       pass
      car = hxs.xpath("//p[@class='Profile-carDetails u-cell']/text()").extract()
      if car:
       carz = car[0]
       care = car[1]
       print '\ncar_model : %s'%carz.strip()
       print '\n%s'%care.strip()
       f.write('\ncar_model :%s'%carz.strip())
       f.write('\n%s'%care.strip())
      #for c in care:
      else:
        pass
       #print c.strip()
       #print carz.strip()
       #f.write('\ncardetails : %s'%c.strip())
      #else:
       #pass
      stars = hxs.xpath("//span[@class='u-textBold u-darkGray']/text()").extract()
      for s in stars:
       
       print '\ncar_owner_rating : %s'%s
       f.write('\ncar_owner_rating : %s'%s.strip())
      else:
       pass
      options = hxs.xpath("//div[@class='RideDetails-infoValue']/span/text()").extract_first()
      
      op = options
      if op:
        print '\noptions : %s'%op.strip()
        f.write('\noptions : %s'%op.strip())

      else:
        pass
      
      #for o in options:
 
       #print o[0]
       #f.write('\noptions : %s'%o.strip())
      #else:
       #pass
     f.close()
     
