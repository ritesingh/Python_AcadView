import tweepy
"""
#Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).
print("An access token is an object that describes the security context of a process or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread.")
    #Reading Consumer key and secret from consumerKeys File

consumerKey = "wvrvuirpt5YjpoXloAlhpnI0p"
consumerSecret = "9uYJR3N36GRFDZGS4yLA8daj5xKrU9y4hPg1KCgmMc42uLUvom"

    #authenticating twitter consumer key
auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.secure=True
authUrl = auth.get_authorization_url()

    #go to this url
print("Please Visit This link and authorize the app ==> ",authUrl)

    #writing access tokes to file
pin =input("Enter The Authorization PIN:")
token = auth.get_access_token(verifier=pin)
accessTokenFile = open("accessTokens","w")
accessTokenFile.write(token[0]+'\n')
accessTokenFile.write(token[1]+'\n')
print("Now you can check your access token file!!") 

#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.
print("nslookup www.google.com \n 172.217.163.132")
print("nslookup www.facebook.com \n 157.240.16.39")


#Q.3- Using Tweepy library try to extract tweets from Twitter. 

consumer_key = "wvrvuirpt5YjpoXloAlhpnI0p"
consumer_secret = "9uYJR3N36GRFDZGS4yLA8daj5xKrU9y4hPg1KCgmMc42uLUvom"
access_key = "823162405588865024-CW0cURBdvh8UGHlM0ElF7QWjdp1FsN5"
access_secret = "UjFkwo1iEm4jK7VLs4qjmXvMBDCcUW6jp1D7H0Lf1KRF9"
 
    # Function to extract tweets
def get_tweets(username):
         
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)
 
        # Calling api
        api = tweepy.API(auth)
 
        # 200 tweets to be extracted
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)
 
        # Empty Array
        tmp=[] 
 
        # create array of tweet information: username, 
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
        for j in tweets_for_csv:
 
            # Appending tweets to the empty array tmp
            tmp.append(j) 
 
        # Printing the tweets
        for i in tmp:
            print(i)
 
 
  # Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("@realDonaldTrump") 
"""
#Q.4- What is a difference between library and API . Figure it out with examples.

"""A library is a collection of functions / objects that serves one particular purpose. 
   you could use a library in a variety of projects. example:junit.jar, log4j.jar"""

"""An API is an interface for other programs to interact with your program or library  
   without having direct access. ( giving specifications for our need to various vendors) example:Android Studio, iOS XCode and Windows .NET Framework SDK"""

#Q.5- Try to access Spotify API . Find out some library for it and play some music.
katyperry_uri="spotify:artist:i43hyhchmj8h3bkpvfvzr6i8r"  #this the id used is of my account , code source:documentation.
spotify=spotipy.Spotify()
results=spotify.artist_albums(katyperry_uri,album_type="album")
albums=results['items']
while results['next']:
    results=spotify.next(results)
    albums.extend(results['items'])
for album in  albums:
    print((album['name']))








