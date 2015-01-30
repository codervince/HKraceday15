#twitter
from TwitterAPI import TwitterAPI
import tweepy

# api = TwitterAPI('8zrOxnJpBaWvmwANmPGYJvyID', 'o6unM1nofwdq9ilxI9b6sV38QztLvToUpEecKOfX3E2Ymxsqhm', '2740028155-PnJzs0EiwBpyMHR9h9xEnmenLeIUi1RM5CfnBt5', 'rH80feDWUmW151tfzOTcwbILnU1ottGmor8lnzQYeXzEE')


CONSUMER_KEY = 'JCFpk4C3KGqDuFmbFbKATgsy4'
CONSUMER_SECRET = 'WA6RFGfNaBTSoXAo8zAa2HPZfOMQSoqUBk3H7erN7lkfRiRorA'
ACCESS_TOKEN_KEY = '2740028155-KfdPjXN8m2EtbR7nHAg0xaXHns13NTRvKlZTx6G'
ACCESS_TOKEN_SECRET = 'hopjfdNaSvgs2aCVk1ezKfKNI3yi5sR2rHmxXyH9Tu2XC'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

print("tweepy\n")
twapi = tweepy.API(auth)
res = twapi.search("#hv #HKRacing #HValley",geocode="22.279328,114.162813,50")
for tweet in res:
	print tweet.text

#etsting




api = TwitterAPI(
CONSUMER_KEY,
CONSUMER_SECRET,
ACCESS_TOKEN_KEY,
ACCESS_TOKEN_SECRET)

TRACK_TERM = '@HKJC_Racing'




r1 = api.request('search/tweets', {'q': 'Goldweaver'})
for item in r1:
	print item['text']

# @HKJC_Racing

print ("News from HKJC:\n")
r2 = api.request('search/tweets', {'q': '@HKJC_Racing OR @SCMPRacingPost OR #shatin OR @winwithmetabet OR @annacotsteel'})
for item in r2:
	print (item['text'] if 'text' in item else item)


# print("Tracking #hv:\n") 
# r3 = api.request('statuses/filter', {'track': TRACK_TERM, 'count':100 }  )
# for item in r3:
# 	print(item['text'] if 'text' in item else item)



racenumber = 10
intro = "#hkjc #shatin R" + str(racenumber)

TWEET_TEXT4= "#hkjc #shatin R4: DW on #9 best avg prizemoney season; 2 is overs, best lastsecspd, #5 early recent speed"
TWEET_TEXT5= "#hkjc #shatin R5: 1f #5 best spd scores cdt; #13 3rd 14-15prize, 1draw LW + cd; also #7, #4 early speed"
TWEET_TEXT6 = intro + "JMO after lean spell quick Dble on #3; #2 early spd L3; #13 well pos, best 1stsec; #1 has early spd to cross"
TWEET_TEXT7 = intro + "#10 best avg season prize, early spd L3; JMO bw #14; BP in form as is mount #6;#3 has 3 wins in cls & r/o L1"
TWEET_TEXT8 = intro + "Rankings avg prze/seasn: #1-#2-#10-#3-#8; r7 was this order; newcomers: #7+#10 race exp"
TWEET_TEXT9 = intro + "Rankings avg prze/seasn: #9-#2-#11-#12 but poor figs; #13 interesting, #9 KAD + Br1 both overs; #2 has best lsec spd"
TWEET_TEXT10 = intro + "#1 is clearly proven form horse; avgpmoney: #1-#2-#7!(2runs)-#6; on spd also consider #5"




racenumber = 1 
intro = "#happyvalley R"
TWEET1 = intro + "#hv C+3 watching the rails this evening - #3 best prizemoney + in form; #1 start best time drct "
TWEET2 = intro + "2 Lots in fav of 1F #7 - #8 has good speed dist & improver likes HV; #1 another leader; #12 improver good HV place rec."


# ff =  "2 is overs"
# TWEET_TEXT = "#hkjc #shatin #r" + racenumber + horse1 + ""
r5 = api.request('statuses/update', {'status': TWEET2})
print('SUCCESS' if r5.status_code == 200 else 'FAILURE')