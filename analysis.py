#importing all dependencies
import numpy as np
import matplotlib.pyplot as plt
import tweepy
#accessing the twitter API
consumer_key='883GiGZYB29hxXQ1K9jkwZ4jf'
consumer_secret_key='XYArqcWFVjYrmEmPFE6LMQLXrWAGUIZiQIYw4HZ16iHUYTCmhJ'
access_token='946944526572142592-BA6IveKbSm1BfwuFNC6HtPpozy64lQY'
access_token_secret='EYe2v4m3tyyG3K8wtcRGglUaQX7DgQ6mVivZ2AGVTJbi9'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
#importing data from afinn dict
d = {}
file=open("C:\\Users\\rajsh\\Desktop\\Sentiment\\afinn.txt")
for line in file:
    ' '.join(line.split())
    x= line.split()
    print(x)
    d[x[0]] =int(x[len(x) - 1])
    
print(d)
def checkKey(dict, key): 
      
    if key in dict: 
        return 1
    else: 
        return 0
rating=0
ratings={}
ratings=list()
tweets={}
tweets=list()

#importing tweets
for tweet in tweepy.Cursor(api.search, q='demonitisation' + ' -RT',since="2016-09-09",lang="en").items(2000):
    text=tweet.text.lower()
    for word in text.split():   
        if(checkKey(d,word)==1):
            rating=rating+int(float(d[word]))
            
           
         
    print("\n",text)     
    print("rating of tweet=",rating)
    ratings.append(rating)
    tweets.append(text)
    rating=0
ratings=np.array(ratings)  
# finding top 5 positive and negative tweets
top_5_index = np.argsort(ratings)[-5:]

print("TOP 5 POSITIVE TWEETS\n")
for i in range(0,len(top_5_index)):
    print(tweets[top_5_index[i]])
    print("tweet rating=",ratings[top_5_index[i]])
    print("\n")


worst_5_index=ratings.argsort()[:5]
print("TOP 5 NEGATIVE TWEETS\n")
for i in range(0,len(worst_5_index)):
    print(tweets[worst_5_index[i]])
    print("tweet rating=",ratings[worst_5_index[i]])
    print("\n")
# finding total no of tweets and positive , neg, neutral tweets
pos_count= 0
neg_count= 0
zero_count = 0
for num in ratings: 
    if num == 0: 
        zero_count +=1
    elif num<0: 
        neg_count +=1
    else:
        pos_count +=1

print("total number of tweets=",len(ratings))
print("total number of positive tweets=",pos_count)
print("total number of negative tweets=",neg_count)
print("total number of neutral tweets=",zero_count)

"""pos=pos_count/len(ratings) * 100
neg=neg_count/len(ratings) * 100
zero=zero_count/len(ratings) * 100
print("percentage of positive tweets=",pos)
print("percentage of negative tweets=",neg)
print("percentage of neutral tweets=",zero)
"""


"""#plotting pie chart
labels = 'postive', 'negative', 'neutral', 
sizes = [pos_count, neg_count,zero_count]
explode = (0.1, 0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
"""






#plotting graph for tweets
fig, ax = plt.subplots()
ax.plot(ratings)



ax.spines['left'].set_position('zero')


ax.spines['right'].set_color('none')
ax.yaxis.tick_left()


ax.spines['bottom'].set_position('zero')


ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom() 

plt.xlabel('#tweets')
plt.ylabel('ratings')
plt.title('twitter sentiment analysis')
plt.show()






