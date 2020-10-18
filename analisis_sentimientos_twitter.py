# -*- coding: utf-8 -*-
"""estadísticas twitter2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k5Ab_ADlMIgEooneoWO28VkPSEil19rn

***`CONECTAR MEDIANTE API A TWITTER `***

##Conectar a la API Twitter
"""

import tweepy
import json

# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# key secret API user
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# con este objeto realizaremos todas las llamadas al API
api = tweepy.API(auth,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

"""##Exportar Tweets  Bbva"""

import pandas as pd
#Buscar Tweets    
bbva1 = {}
bbva1['tweets'] = []
for tweet in tweepy.Cursor(api.search, q="bbva_peru", tweet_mode="extended").items(1000):
  bbva1['tweets'].append(tweet._json)

id_bbva =pd.DataFrame(list(map(lambda rec : rec.get('id'), bbva1['tweets'])))
id_bbva.rename(columns={0: 'id'},inplace=True)

texto=list(map(lambda rec : rec.get('full_text'), bbva1['tweets']))
id_bbva['texto']=texto
create_at =list(map(lambda rec : rec.get("created_at"), bbva1['tweets']))
id_bbva['create_at ']=create_at 
retweet_count=list(map(lambda rec : rec.get('retweet_count'), bbva1['tweets']))
id_bbva['retweet_count']=retweet_count
#  TWEETS ( USUARIO ) usuario
usuario=list(map(lambda rec : rec.get('user'), bbva1['tweets']))
###    favourites_count
favourites_count=list(map(lambda rec : rec.get('favourites_count'), usuario))
id_bbva['favourites_count ']=favourites_count
## followers_count
followers_count=list(map(lambda rec : rec.get('followers_count'), usuario))
id_bbva['followers_count ']=followers_count
## friends_count
friends_count=list(map(lambda rec : rec.get('friends_count'), usuario))
id_bbva['friends_count ']=friends_count
## listed_count
listed_count=list(map(lambda rec : rec.get('listed_count'), usuario))
id_bbva['listed_count']=listed_count
screen_name=list(map(lambda rec : rec.get('screen_name'), usuario))
id_bbva['screen_name']=screen_name
created_at_user=list(map(lambda rec : rec.get('created_at'), usuario))
id_bbva['created_at_user']=created_at_user
statuses_count=list(map(lambda rec : rec.get('statuses_count'), usuario))
id_bbva['statuses_count']=statuses_count

import pandas as pd
import numpy as np
def remove_salt(text):
    text = text.replace('\n', ' ').replace('\r', '')
    return text
id_bbva["texto"] = id_bbva["texto"].apply(lambda x: remove_salt(x))

id_bbva['Bancos'] = "Bbva"

id_bbva

"""Exportar Tweets Bbva solo Id y texto"""

#data frame , solo id y texto para analisis de sentimiento AWS
id_bbva2 = id_bbva[["id","texto"]]
#id2["id"] = id2.index

#from google.colab import files
#id_bbva2.to_csv('Bbva_id.csv',encoding='utf-8-sig',index = False) 

#files.download('Bbva_id.csv')

"""##Exportar Tweets  BCPComunica"""

#Buscar Tweets  bcp
bcp1 = {}
bcp1['tweets'] = []
for tweet in tweepy.Cursor(api.search, q="BCPComunica", tweet_mode="extended").items(1000):
  bcp1['tweets'].append(tweet._json)

id_bcp =pd.DataFrame(list(map(lambda rec : rec.get('id'), bcp1['tweets'])))
id_bcp.rename(columns={0: 'id'},inplace=True)

texto=list(map(lambda rec : rec.get('full_text'), bcp1['tweets']))
id_bcp['texto']=texto
create_at =list(map(lambda rec : rec.get("created_at"), bcp1['tweets']))
id_bcp['create_at ']=create_at 
retweet_count=list(map(lambda rec : rec.get('retweet_count'), bcp1['tweets']))
id_bcp['retweet_count']=retweet_count
#  TWEETS ( USUARIO ) usuario
usuario=list(map(lambda rec : rec.get('user'), bcp1['tweets']))
###    favourites_count
favourites_count=list(map(lambda rec : rec.get('favourites_count'), usuario))
id_bcp['favourites_count ']=favourites_count
## followers_count
followers_count=list(map(lambda rec : rec.get('followers_count'), usuario))
id_bcp['followers_count ']=followers_count
## friends_count
friends_count=list(map(lambda rec : rec.get('friends_count'), usuario))
id_bcp['friends_count ']=friends_count
## listed_count
listed_count=list(map(lambda rec : rec.get('listed_count'), usuario))
id_bcp['listed_count']=listed_count
screen_name=list(map(lambda rec : rec.get('screen_name'), usuario))
id_bcp['screen_name']=screen_name
created_at_user=list(map(lambda rec : rec.get('created_at'), usuario))
id_bcp['created_at_user']=created_at_user
statuses_count=list(map(lambda rec : rec.get('statuses_count'), usuario))
id_bcp['statuses_count']=statuses_count

id_bcp['Bancos'] = "Bcp"

import pandas as pd
import numpy as np
def remove_salt(text):
    text = text.replace('\n', ' ').replace('\r', '')
    return text
id_bcp ["texto"] = id_bcp["texto"].apply(lambda x: remove_salt(x))

#data frame , solo id y texto para analisis de sentimiento AWS
id_bcp2 = id_bcp[["id","texto"]]
#id2["id"] = id2.index

#from google.colab import files
#id_bcp2.to_csv('Bcp_id_todo.csv',encoding='utf-8-sig',index = False) 
#files.download('Bcp_id_todo.csv')

"""##Exportar Tweets  Interbank"""

#Buscar Tweets  ibk
ibk1 = {}
ibk1['tweets'] = []
for tweet in tweepy.Cursor(api.search, q="interbank", tweet_mode="extended",lan ='es').items(1000):
  ibk1['tweets'].append(tweet._json)

id_ibk =pd.DataFrame(list(map(lambda rec : rec.get('id'), ibk1['tweets'])))
id_ibk.rename(columns={0: 'id'},inplace=True)

texto=list(map(lambda rec : rec.get('full_text'), ibk1['tweets']))
id_ibk['texto']=texto
create_at =list(map(lambda rec : rec.get("created_at"), ibk1['tweets']))
id_ibk['create_at ']=create_at 
retweet_count=list(map(lambda rec : rec.get('retweet_count'), ibk1['tweets']))
id_ibk['retweet_count']=retweet_count
#  TWEETS ( USUARIO ) usuario
usuario=list(map(lambda rec : rec.get('user'), ibk1['tweets']))
###    favourites_count
favourites_count=list(map(lambda rec : rec.get('favourites_count'), usuario))
id_ibk['favourites_count ']=favourites_count
## followers_count
followers_count=list(map(lambda rec : rec.get('followers_count'), usuario))
id_ibk['followers_count ']=followers_count
## friends_count
friends_count=list(map(lambda rec : rec.get('friends_count'), usuario))
id_ibk['friends_count ']=friends_count
## listed_count
listed_count=list(map(lambda rec : rec.get('listed_count'), usuario))
id_ibk['listed_count']=listed_count
screen_name=list(map(lambda rec : rec.get('screen_name'), usuario))
id_ibk['screen_name']=screen_name
created_at_user=list(map(lambda rec : rec.get('created_at'), usuario))
id_ibk['created_at_user']=created_at_user
statuses_count=list(map(lambda rec : rec.get('statuses_count'), usuario))
id_ibk['statuses_count']=statuses_count

id_ibk['Bancos'] = "Ibk"

import pandas as pd
import numpy as np
def remove_salt(text):
    text = text.replace('\n', ' ').replace('\r', '')
    return text
id_ibk ["texto"] = id_ibk ["texto"].apply(lambda x: remove_salt(x))

#data frame , solo id y texto para analisis de sentimiento AWS
id_ibk2 = id_ibk[["id","texto"]]
#id2["id"] = id2.index

id_ibk2.head()

#from google.colab import files
#id_ibk2.to_csv('Ibk_id_todo.csv',encoding='utf-8-sig',index = False) 
#files.download('Ibk_id_todo.csv')

"""##Exportar Tweets Scotiabank"""

#Buscar Tweets  scotiabank
scot1 = {}
scot1['tweets'] = []
for tweet in tweepy.Cursor(api.search, q="ScotiabankPE", tweet_mode="extended").items(1000):
  scot1['tweets'].append(tweet._json)

id_scot =pd.DataFrame(list(map(lambda rec : rec.get('id'), scot1['tweets'])))
id_scot.rename(columns={0: 'id'},inplace=True)

texto=list(map(lambda rec : rec.get('full_text'), scot1['tweets']))
id_scot['texto']=texto
create_at =list(map(lambda rec : rec.get("created_at"), scot1['tweets']))
id_scot['create_at ']=create_at 
retweet_count=list(map(lambda rec : rec.get('retweet_count'), scot1['tweets']))
id_scot['retweet_count']=retweet_count
#  TWEETS ( USUARIO ) usuario
usuario=list(map(lambda rec : rec.get('user'), scot1['tweets']))
###    favourites_count
favourites_count=list(map(lambda rec : rec.get('favourites_count'), usuario))
id_scot['favourites_count ']=favourites_count
## followers_count
followers_count=list(map(lambda rec : rec.get('followers_count'), usuario))
id_scot['followers_count ']=followers_count
## friends_count
friends_count=list(map(lambda rec : rec.get('friends_count'), usuario))
id_scot['friends_count ']=friends_count
## listed_count
listed_count=list(map(lambda rec : rec.get('listed_count'), usuario))
id_scot['listed_count']=listed_count
screen_name=list(map(lambda rec : rec.get('screen_name'), usuario))
id_scot['screen_name']=screen_name
created_at_user=list(map(lambda rec : rec.get('created_at'), usuario))
id_scot['created_at_user']=created_at_user
statuses_count=list(map(lambda rec : rec.get('statuses_count'), usuario))
id_scot['statuses_count']=statuses_count

id_scot['Bancos'] = "Scot"

import pandas as pd
import numpy as np
def remove_salt(text):
    text = text.replace('\n', ' ').replace('\r', '')
    return text
id_scot ["texto"] = id_scot["texto"].apply(lambda x: remove_salt(x))

#data frame , solo id y texto para analisis de sentimiento AWS
id_scot2 = id_scot[["id","texto"]]
#id2["id"] = id2.index

#from google.colab import files
#id_scot2.to_csv('Scot_id_todo.csv',encoding='utf-8-sig',index = False) 
#files.download('Scot_id_todo.csv')

"""# ##Unir data frame de bancos"""

bancos_id = pd.concat([id_bbva, id_bcp, id_ibk, id_scot])

#from google.colab import files
#bancos_id.to_csv('bancos_id.csv',encoding='utf-8-sig',index = False) 
#files.download('bancos_id.csv')

"""# ##Cargar resultados de analisis de sentimiento de AWS"""

from google.colab import drive
drive.mount('/content/drive')

# Usamos la librería files de colab
import pandas as pd
from google.colab import files
AWS_Bcp = pd.read_json("/content/drive/My Drive/0.1_Capacitacion_DSW/Resultados_competencia_Bbva/AWS_BCP.json", encoding = 'utf-8')
AWS_Bbva = pd.read_json("/content/drive/My Drive/0.1_Capacitacion_DSW/Resultados_competencia_Bbva/AWS_BBVA.json", encoding = 'utf-8')
AWS_Ibk = pd.read_json("/content/drive/My Drive/0.1_Capacitacion_DSW/Resultados_competencia_Bbva/AWS_IBK.json", encoding = 'utf-8') 
AWS_Scot = pd.read_json("/content/drive/My Drive/0.1_Capacitacion_DSW/Resultados_competencia_Bbva/AWS_SCOT.json", encoding = 'utf-8')

AWS_Bcp1 = AWS_Bcp[["Sentiment","text"]]
AWS_Bbva1 = AWS_Bbva[["Sentiment","text"]]
AWS_Ibk1 = AWS_Ibk[["Sentiment","text"]]
AWS_Scot1 = AWS_Scot[["Sentiment","text"]]

import re
def tokenization(text):
    text = re.split('\W+', text)
    return text[1]

AWS_Bcp1['id'] = AWS_Bcp1["text"].apply(lambda x: tokenization(x))
AWS_Bcp2 = AWS_Bcp1[["Sentiment","id"]]

AWS_Bbva1['id'] = AWS_Bbva1["text"].apply(lambda x: tokenization(x))
AWS_Bbva2 = AWS_Bbva1[["Sentiment","id"]]

AWS_Ibk1['id'] = AWS_Ibk1["text"].apply(lambda x: tokenization(x))
AWS_Ibk2 = AWS_Ibk1[["Sentiment","id"]]

AWS_Scot1['id'] = AWS_Scot1["text"].apply(lambda x: tokenization(x))
AWS_Scot2 = AWS_Scot1[["Sentiment","id"]]

bancos_sentimental= pd.concat([AWS_Bcp2, AWS_Bbva2, AWS_Ibk2, AWS_Scot2])

"""# ## Cruzar data frame de estadisticas del comentario aasociadas al banco y el resultado del analisis de sentimiento"""

#bancos_sentimental.drop(['Sentiment','id'],axis=0)
bancos_sentimental.drop([0], inplace=True)
#bancos_sentimental.head()

bancos_sentimental['id']=bancos_sentimental['id'].astype(int)
bancos_id['id']=bancos_id['id'].astype(int)

bancos_todo = pd.merge(bancos_id, bancos_sentimental, how='left', on='id')

##### LIMPIEZA 
import nltk
import string
stopwords=nltk.download("stopwords")
def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    text = re.sub(r'^RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
    text = re.sub(r'#', '', text)
    text = re.split('\W+', text)
    text = [item.lower() for item in text]
    
    return text

def remove_stopwords(text):
    stopword = nltk.corpus.stopwords.words('spanish')
    text = [word for word in text if not word in stopword]
    text = ' '.join([str(elem) for elem in text]) 
     
    return text

#LIMPIEZA TEXTO BBVA
bancos_todo['texto'] = bancos_todo['texto'].apply(lambda x: remove_punct(x))
bancos_todo['texto'] = bancos_todo['texto'].apply(lambda x: remove_stopwords(x))

from google.colab import files
bancos_todo.to_csv('bancos_todo.csv',encoding='utf-8-sig',index = False) 
files.download('bancos_todo.csv')