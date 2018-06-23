import re
"""Q.1- Extract the user id, domain name and suffix from the following email addresses. 
emails = "zuck26@facebook.com" "page33@google.com"
"jeff42@amazon.com"
desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]
"""
emails = "zuck26@facebook.com"" ""page33@google.com"" ""jeff42@amazon.com"
pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
print(re.findall(pattern, emails,flags=re.IGNORECASE))


#Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.  
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
print(re.findall(r'\bB\w+', text, flags=re.IGNORECASE))  #\b\B is for making 'b' as boundary and flag makes case insensitive.

#Q.3- Split the following irregular sentence into words
sentence = "A, very very; irregular_sentence"
print(" ".join(re.split('[;,\s_]+', sentence)))

#OPTIONAL::Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. 
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
tweet = re.sub('http\S+\s*', '', tweet)  # remove URLs
tweet = re.sub('RT|cc', '', tweet)  # remove RT and cc
tweet = re.sub('#\S+', '', tweet)  # remove hashtags
tweet = re.sub('@\S+', '', tweet)  # remove mentions
tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations
tweet = re.sub('\s+', ' ', tweet)  # remove extra whitespace
print(tweet)
