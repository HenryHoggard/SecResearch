import urllib2
from BeautifulSoup import BeautifulSoup
import re
import MySQLdb



url = ''
country = ''
ip = ''
notifier = ''
webserver = ''
system = ''
date = ''
time = ''



def scrapewebsite(defaceid):

    for x in range(16979299, 17034801):
        try:
            opener = urllib2.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:10.0.2) Gecko/20100101 Firefox/10.0.2')]
            f = opener.open("http://zone-h.org/mirror/id/"+ str(x))
                    
            webpage = f.read()
            
            print webpage
            #webpage = urlopen("http://zone-h.org/mirror/id/"+ str(defaceid)).read()
            if 'Invalid defacement' in webpage:
                print 'waaaaaaaa'
                continue

            
            regexFindURL = re.compile('rel="nofollow">(.*)</a></li>')
            regexFindCountry = re.compile('title="(.*)"></li>')
            regexFindIP = re.compile('<strong>IP address:</strong> (.*)  <img src="')
            regexFindServer = re.compile('<strong>Web server:</strong> (.*)</li>')
            regexFindNotifier = re.compile('<strong>Notified by:</strong> (.*)</li>')
            regexFindSystem = re.compile('<strong>System:</strong> (.*)</li>')
            regexFindDate = re.compile('<strong>Mirror saved on:</strong> (.*) ')
            
            webserver= re.findall(regexFindServer, webpage)
            url= re.findall(regexFindURL, webpage)
            country = re.findall(regexFindCountry, webpage)
            ip = re.findall(regexFindIP, webpage)
            notifier = re.findall(regexFindNotifier, webpage)
            system = re.findall(regexFindSystem, webpage)
            date = re.findall(regexFindDate, webpage)
               
            regexFindTime = re.compile('<strong>Mirror saved on:</strong> ' + date[0]+ ' (.*)</li>')
            time= re.findall(regexFindTime, webpage)


            
      
            
            
            insertdb(x, url[0], country[0], ip[0], notifier[0], webserver[0], system[0], date[0], time[0])
        except:
	    print 'errororor'	
  
def insertdb(id, url, country, ip, notifier, webserver, system, date, time):

    db = MySQLdb.connect("localhost","username","password","secresearch")

    cursor = db.cursor()

    query = "INSERT INTO defaces VALUES ('','%i', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (id, url, country, ip, notifier, webserver, system, date, time)


    try:
        cursor.execute(query)
        db.commit()
        print 'worked'
    except Exception, e:
        db.rollback()
        print 'error'
        print e
    db.close()



if __name__ == "__main__":
   scrapewebsite(16979279)
