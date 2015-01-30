from lxml import etree
import urllib2
import pprint
import smtplib
from getpass         import getpass
from smtplib         import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import re
from datetime import *
from collections import defaultdict
#store XML data in racedataTEST database
#race: racecoursecode, racedate, jumptime, 
#odds racenumber, servertime, winodds, placeodds
COMMASPACE = ', '


#nested dict class
class Vividict(dict):
	def __missing__(self, key):
		value = self[key] = type(self)()
		return value

# class Oddsdata( object ):
#     def __init__( self, updatedate=None, updatetime=None, racedate=None, racenumber=None, horsenumber=None, winodds=None, placeodds=None, iswinfav=None, isplacefav=None ):
#         self.updatedate= updatedate
#         self.updatetime= updatetime 
#         self.racedate= racedate
#         self.racenumber = racenumber
#         self.horsenumber = horsenumber
#         self.winodds = winodds
#         self.placeodds = placeodds
#         self.iswinfav = iswinfav
#         self.isplacefav = isplacefav


# def groupBy( facts, name ):
#     total= collections.defaultdict( int )
#     for f in facts:
#         key= getattr( f, name )
#         total[key] += f.count


#global var 
oddsdata = Vividict()
#get data from database..put here


#todos:
'''
PART 1
Cron Job
runs program  every 30mins collects data into DB
runs program every 30 secs between 10m < 2m then every 1sec < 2mins
Each new collect - computes STARTPRICE, MAXPRICE, THIS-LAST pc change, THIS PRICE
Write to email and send  

At end of race check HKJC flag-
output odds movements versus final position plus FINAL ODDS and 

writes AGG DATA TO DB AFTER RACE


'''
#MORNING LINE 
def writeIntro():

	#get next race date from DB

    f = open("email.html", "w")
    f.write(
    	'''<HTML>
			<HEAD>
			 <TITLE>METABET TIPPING SERVICE</TITLE>
			</HEAD>
			<body>
			<br><img src="cid:image1"><br>
			<p>
	       <h1>Welcome to the HKJC Exclusive Tipping Service!</h1>
	       <h2> Next race in Hong Kong </h2>	
	       <p>

	       <br>
		''')
    f.close()


def writeEnd():
	f = open("email.html", "a+")
	f.write(
        '''
        <p>	       
        Till the next time!
         </body>
			</HTML>
        '''
		)
	f.close()

#need print items for vividict
#TODO: Table entries 
def printitems(dictObj, indent=0):
    p=[]
    p.append('<ul>\n')
    for k,v in dictObj.iteritems():
        if isinstance(v, dict):
            p.append('<li>'+ k+ ':')
            p.append(printitems(v))
            p.append('</li>')
        else:
            p.append('<li>'+ str(k)+ ':'+ str(v)+ '</li>')
    p.append('</ul>\n')
    return '\n'.join(p)


def writeData():
	f = open("email.html", "a+")
	f.write(printitems(oddsdata))
	f.close()

#write to HTML
# see http://www.dalkescientific.com/writings/diary/archive/2005/04/24/interactive_html.html
def doCharts():
    pass

def getStats(racenumber, horsenumber):
    pass

#open HTML file
def sendMail():
	# me == my email address
	# you == recipient's email address
    me = "sdp@posteo.de"
    #"vincevincent@email.com", "sdp@posteo.de", "publicvince102@gmail.com", 
    recipients= ["nastybi@gmail.com", "publicvince102@gmail.com"]
    writeIntro()
    writeData()
    writeEnd()
	# Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Welcome Subscriber! Metabet Tipping Service"
    msg['From'] = me
    msg['To'] = COMMASPACE.join(recipients)

	# Create the body of the message (a plain-text and an HTML version).
	#USE HTML FILE
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
	
	#html from file
    html = open('email.html', 'r').read()

    img_fp = open('../HKG.jpg', 'rb')
    img = MIMEImage(img_fp.read(), _subtype='image/jpg')
    img_fp.close()
    img.add_header('Content-ID', '<image1>')
    msg.attach(img)

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    login, password = 'sdp@posteo.de', getpass('Your password:')
    recipients = [login]

	# Send the message via local SMTP server. port 465
    s = SMTP_SSL('smtp.posteo.de', 465, timeout=10)
    # s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    s.set_debuglevel(1)
    try:
	    s.login(login, password)
	    s.sendmail(msg['From'], msg['To'], msg.as_string())
    finally:
	    s.quit()


# s = smtplib.SMTP('localhost')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
# s.sendmail(me, you, msg.as_string())
# s.quit()


#get todays venue
pp = pprint.PrettyPrinter(indent=4)

#return a dictionary of data for 
def getOddsData(racecoursecode, racedate, numberofraces):


	venue =  racecoursecode
	date = racedate
	noraces = numberofraces
	baseurl = 'http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_'
	headers = { 'User-Agent' : 'Mozilla/5.0' }
	#ALL RACES each race split 
	winandplace = urllib2.Request('http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_winplaodds&date=18-01-2015&venue=' + venue + '&start=1&end=' + str(noraces), None, headers)
	i = 1
	while i <= noraces:
	    bettypes = [ 'qin', 'qpl']  
	    #racepools = urllib2.Request(baseurl + 'full&date=' + date + '&venue=' + venue+ '&raceno=' + str(i)+ '&pool=' + bettypes.pop() + '&tag=' + bettypes.pop().upper() + '/RACE', None, headers)
	    #print etree.fromstring(urllib2.urlopen(racepools).read()).xpath('text()')
	    i = i+1
	#all scratched, all reserves?
	scratched = urllib2.Request('http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_scratched&date=18-01-2015&venue=' + venue + '&start=1&end=' + str(noraces), None, headers)
	reserves = urllib2.Request('http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_reserve&date=18-01-2015&venue=' + venue + '&start=1&end=' + str(noraces), None, headers)


	j = 	1
	# print "Pool Totals for %s today %s" % (venue, date)
	# while j <= noraces:
	#     print("Race Number: %d" % j)
	#     # pooltots = urllib2.Request('http://bet.hkjc.com/racing/getXML.aspx?type=pooltot&date=' + date + '&venue=' + venue+ '&raceno=' + str(j), None, headers)
	#     # print etree.fromstring(urllib2.urlopen(racepools).read()).xpath('text()')
	#     j = j+1

	print ("win and place per race\n")
	pattern = re.compile(r".*#PLA.*")
	#first element is servertime 
	winandplacerace = etree.fromstring(urllib2.urlopen(winandplace).read()).xpath('text()')[0].split('@@@')
	pp.pprint(winandplacerace) #list raceno+1 elements first is servertime
	noraces = len(winandplacerace)
	oddsdata["updatetime"]= winandplacerace.pop(0) 
	oddsdata["updatedate"] = datetime.today()
	# print "servertime\n"
	
	#turn parsed data into dictionary
	'''
	'WIN;1=8.4=0;2=108=0;3=44=0;4=12=0;5=68=0;6=15=0;7=3.5=1;8=4.9=0;9=96=0;10=3.9=0;11=19=0;12=57=0;13=13=0;14=152=0#PLA;1=2.7=0;2=17=0;3=10=0;4=3.4=0;5=12=0;6=3.9=0;7=2.2=0;8=1.5=1;9=14=0;10=1.5=0;11=4.4=0;12=9.6=0;13=4.0=0;14=18=0',
	each is an Oddsdata object 

	'''
	if oddsdata["updatetime"] != '': 

		horseobjects = []

		r = 0
		for race in winandplacerace:
			place = False
			r = r+1
			for horse in race.split(';'):
				if pattern.search(horse):
					place = True
				if horse == 'WIN':
					continue	
				# o = Oddsdata()
				# data = horse.split('=')
				# oddsdata["race" + str(r)]["win"][data[0]] = data[1]
				# o.updatedate = updatedate
				# o.updatetime = updatetime
				# o.horsenumber = data[0]
				# o.racenumber = str(r)
				if not place:
					data = horse.split('=')
					# o.winodds = data[1]
					# o.iswinfav = data[2]
					oddsdata["race" + str(r)]["win"][data[0]] = data[1]
				else:
					# o.placeodds = data[1]
					# o.isplacefav = data[2]
					data = horse.split('=')
					oddsdata["race" + str(r)]["place"][data[0]] = data[1]

		# print ("scratched\n")
		# print etree.fromstring(urllib2.urlopen(scratched).read()).xpath('text()')	

		# # reddit_file = urllib2.urlopen(winandplace).read()
		# print ("reserves\n")
		# print etree.fromstring(urllib2.urlopen(reserves).read()).xpath('text()')
		pp.pprint(oddsdata)
		return oddsdata
	# for ob in horseobjects:
	# 	attrs = vars(ob)
	# 	print ', '.join("%s: %s" % item for item in attrs.items())

	# keys = oddsdata.keys()
	# length = len(oddsdata[keys[0]])
	# items = ['<table style="width:300px">', '<tr>']
	# for k in keys:
	# 	items.append('<td>%s</td>' % k)
	# items.append('</tr>')

	# for i in range(length):
	# 	items.append('<tr>')
	# 	for k in keys:
	# 		items.append('<td>%s</td>' % oddsdata[k][i])
	# 		items.append('</tr>')

	# items.append('</table>')

	# print '\n'.join(items)




def sendToDB():
	pass



if __name__ == "__main__":
    # sendMail()
    getOddsData('HV', '21/01/2015' ,8)
    sendMail()



# reddit = etree.fromstring(reddit_file)

# print reddit.xpath('text()')

# for item in reddit.xpath('/sr'):
#     print "racecourse =", item.xpath("./text()")[0]
#     # print "description =", item.xpath("./description/text()")[0]
#     # print "thumbnail =", item.xpath("./*[local-name()='thumbnail']/@url")[0]
#     # print "link =", item.xpath("./link/text()")[0]
#     print "-" * 100