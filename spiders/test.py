from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http.request import Request
from bs4 import BeautifulSoup
from project.items import ProjectItem
import re
from pattern.web import plaintext
import requests
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

    
    

 def parse(self, response):
  item = ProjectItem()
  soup = BeautifulSoup(response.body,"html.parser")
  li = soup.find_all("a", {"class": "trip-search-oneresult js-tracktor-search-result"})
 
 #links = li.find("a", {"class": "trip-search-oneresult js-tracktor-search-result"})
  f = open('csvfile.csv','a')
  for l in li:
   #print "--------------------------------------------------------------------------------------------------------------"
   a = 'https://www.blablacar.in'+l.get('href')
   r2 = requests.get(a)
   soup2 = BeautifulSoup(r2.content,"html.parser")
   
   #print "'%s'"%a
   #for b in a:
    #r2 = requests.get(b)
    #soup2 = BeautifulSoup(r2.content,"html.parser")
    
   #links = soup2.find_all("div", {"class": "RideDetails trip-container"})
   
   #for link in links:
    
   
   try:
     source = soup2.find("span",{"class":"RideName-location RideName-location--arrowAfter"}).get_text()
     print ('\nsource : %s'%source.strip())
     f.write('\nsource : %s'%source.strip())
   except:
     pass
   try:
     destination = soup2.find("span",{"class":"RideName-location RideName-location--arrowAfter"}).next_sibling.get_text()
     print ('\ndestination : %s'%destination.strip())
     f.write('\ndestination : %s'%destination.strip())
   except:
     pass
   try:
     price = soup2.find("span",{"class":"Booking-price u-block"}).text[1:-1]
     print ('\nprice : %s'%price.strip())
     f.write('\nprice : %s'%price.strip())
     #print "departurepoint: %s"%(l.find("dd",{"class":"js-tip-custom"}).get_text())
     #print "departurepoint: %s"%(l.find("h3",{"class":"time u-darkGray"}).get_text())
     #print i
   except:
     pass
   try:
     departuredate = soup2.find("strong",{"class":"RideDetails-infoValue"}).get_text()
     print ('\ndeparturedate : %s'%departuredate.strip())
     f.write('\ndeparturedate : %s'%departuredate.strip())
   except:
     pass
   try:
     departurepoint = soup2.find("span",{"class":"RideDetails-infoValue RideDetails-infoValue--clickable tip js-display-map"}).get_text()
     print ('\ndeparturepoint : %s'%departurepoint.strip())
     f.write('\ndeparturepoint : %s'%departurepoint.strip())
   except:
     pass
   try:
     departure = soup2.find_all("span",{"class":"RideDetails-infoValue RideDetails-infoValue--clickable tip js-display-map"})[1].get_text()
     print ('\ndropoffpoint : %s'%departure.strip())
     f.write('\ndropoffpoint : %s'%departure.strip())
   except:
     pass
   try:
     avail = soup2.find("span",{"class":"Booking-seats u-block"}).get_text()
     print ('\navailableseats : %s'%avail.strip())
     f.write('\navailableseats : %s'%avail.strip())
   except:
     pass
   try:
     photo = soup2.find("a",{"class":"PhotoWrapper PhotoWrapper--medium"}).get('href')
     print ('\nphoto : %s'%photo.strip())
     f.write('\nphoto : %s'%photo.strip())
   except:
     pass
   try:
     name = soup2.find("h4",{"class":"ProfileCard-info ProfileCard-info--name u-truncate"}).get_text()
     print ('\nname : %s'%name.strip())
     f.write('\nname : %s'%name.strip())
   except:
     pass
   try:
     age = soup2.find("div",{"class":"ProfileCard-info"}).get_text()
     print ('\nage : %s'%age.strip())
     f.write('\nage : %s'%age.strip())
   except:
     pass
   try:
     stars = soup2.find("p",{"class":"ratings-container"}).get_text()
     print ('\nstars : %s'%stars.strip())
     f.write('\nstars : %s'%stars.strip())
   except:
     pass
   try:
     car = soup2.find("p",{"class":"Profile-carDetails u-cell"}).get_text()
     print ('\ncardetails : %s\n'%car.strip())
     f.write('\ncardetails : %s'%car.strip())
   except:
     pass
   try:
     options = soup2.find("div",{"class":"RideDetails-infoValue"}).get_text()
     print ('\noptions : %s'%options.strip())
     f.write('\noptions : %s'%options.strip())
   except:
     pass
  f.close()   
  
