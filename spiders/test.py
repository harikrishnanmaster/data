from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http.request import Request
from bs4 import BeautifulSoup
from project.items import ProjectItem


class PagesSpider(CrawlSpider):
    """
    the Page Spider for wikipedia
    """

    name = "project"
    #allowed_domains = ["wikipedia.org"]

    start_urls = ['https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/?fn=new+delhi&fcc=IN&tn=chandigarh&tcc=IN&sort=trip_date&order=asc&limit=10&page=%s' % page for page in xrange(1,15)]
    

    rules = (
        Rule(LinkExtractor(),
             callback='parse_page',
             # hook to be called when this Rule generates a Request
             process_request='parse'),
    )

    custom_settings = {
        'FEED_URI' : 'tmp/tesmdz.csv'
    }
    

    def parse(self, response):
     item = ProjectItem()
     soup = BeautifulSoup(response.body,"html.parser")
     li = soup.find_all("article", {"class": "row"})
     f = open('csvfile.csv','a')
     for l in li:
      try:
      #item['url'] = response.url
       #item['source'] = l.find("span", {"class":"from trip-roads-stop"}).get_text()
       #item['destination'] = l.find("span", {"class": "trip-roads-stop"}).get_text()
       #item['departurepoint'] = l.find("dd", {"class": "js-tip-custom"}).get_text()
       
       source = l.find("span", {"class":"from trip-roads-stop"}).get_text()
       f.write('\nsource : %s'%source.strip())
       
       #yield{'source': source.strip()}
      except:
       pass
      try:
       destination = l.find("span", {"class": "trip-roads-stop"}).get_text()
       f.write('\ndestination : %s'%destination.strip())
       #yield{'destination': destination.strip()}
      except:
       pass
      try:
       departurepoint = l.find("dd", {"class": "js-tip-custom"}).get_text()
       f.write('\ndeparturepoint : %s'%departurepoint.strip())
       #yield{'departurepoint': departurepoint.strip()}
      except:
       pass
      try:
       dropoffpoint = l.find("i", {"class": "bbc-icon2-circle first size16 u-red"}).get_text()
       f.write('\ndroppoffpoint : %s'%dropoffpoint.strip())
       #yield{'droppoffpoint': dropoffpoint.strip()}
      except:
       pass
      try:
      
       departure_date = l.find("h3", {"class": "time u-darkGray"}).get_text()
       f.write('\ndeparturedate : %s'%departure_date.strip())
       #yield{'departuredate': departure_date.strip()}
      except:
       pass
      try:
      
       price = l.find("span", {"class": "offer span2 u-alignRight"}).get_text()
       f.write('\nprice : %s'%price.strip())
       #yield{'price': price.strip()}
      except:
       pass
      try:
       options = l.find("div", {"class": "availability"}).get_text()
       f.write('\noptions : %s'%options.strip())
       #yield{'options': options.strip()}
      except:
       pass
      try:
       Drivername = l.find("h2", {"class": "ProfileCard-info ProfileCard-info--name u-truncate"}).get_text()
       f.write('\nDriver name : %s'%Drivername.strip())
       #yield{'Driver name': Drivername.strip()}
      except:
       pass
      try:
       Driverage =  l.find("div", {"class": "ProfileCard-info"}).get_text()
       f.write('\nDriver age : %s'%Driverage.strip())
       #yield{'Driver Age': Driverage.strip()}
      except:
       pass
      try:
       comforttravel = l.find("i", {"class": "bbc-icon2-comfort-plus size26 u-blue u-cell u-right no-margin-right tip"}).get_text()
       f.write('\ncomfort travel : %s'%comforttravel.strip())
       #yield{'Comfort travel': comforttravel.strip()}
      except:
       pass
      try:
       stars = l.find("span", {"class": "u-textBold u-darkGray"}).get_text()
       f.write('\nstars : %s'%stars.strip())
       #yield{'stars': stars.strip()}
      except:
       pass
      try:
       photo = l.find("img", {"class": "PhotoWrapper-user PhotoWrapper-user--medium u-rounded "}).get('src')
       f.write('\nphoto : %s'%photo.strip())
       #yield{'photo': photo.strip()}
      except:
       pass
      try:
       fbfriends = l.find("span", {"class": "tip user-trust-fb u-gray "}).get_text()
       f.write('\nfb friends : %s'%fbfriends.strip())
       #yield{'fbfriends': fbfriends.strip()}
      except:
       pass
      try:
       govtid = l.find("div", {"class": "ProfileCard-info u-blue "}).get_text()
       f.write('\ngovtid : %s'%govtid.strip())
       #yield{'govtid': govtid.strip()}
      except:
       pass
      try:
       approval = l.find("i", {"class": "bbc-icon2-instant size26 u-yellow u-cell u-right no-margin-right tip "}).get_text()
       #yield{'source': source.strip()}
       #yield{'destination': destination.strip()}
       #yield{'departurepoint': departurepoint.strip()}
       #yield{'droppoffpoint': dropoffpoint.strip()}
       #yield{'departuredate': departure_date.strip()}
       #yield{'price': price.strip()}
       #yield{'options': options.strip()}
       #yield{'Driver name': Drivername.strip()}
       #yield{'Driver Age': Driverage.strip()}
       #yield{'Comfort travel': comforttravel.strip()}
       #yield{'stars': stars.strip()}
       #yield{'photo': photo.strip()}
       #yield{'fbfriends': fbfriends.strip()}
       #yield{'govtid': govtid.strip()}
       f.write('\napproval : %s'%approval.strip())
       #yield{'approval': approval.strip()}
 
       
      except:
       pass
     #description = soup.find("div", {"id": "mw-content-text"})
    # get the first tag
     #description = string_from_listing(description.find('p'))

     #item['description'] = description

     f.close()     

