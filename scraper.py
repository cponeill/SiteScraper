import urllib2
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
import csv

def scraper():

	""" 
	Scrape a website for a specfic variable. 
	In this case, the software is scraping the Gold.org website for the asking price of Gold
	and exporting that information to a file named output.csv.
	"""

	with open("output.csv", "w") as csvfile:
		fieldnames = ["Time", "Price"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		url  = "http://gold.org"
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page)
		gold = soup.findAll(attrs={"class":"value"})
		ask  = gold[0].string

		writer.writeheader()
		for i in range(0, 60):
			now = datetime.now().strftime("%I:%M:%S%p")
			writer.writerow({"Time": now, "Price": ask})
			sleep(30)

print "Scraping the Gold.org website for the current asking price of gold."
scraper()