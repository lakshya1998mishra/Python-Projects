#SMS Push Notification system
# import requests
# from numpy.random import randint
# url='https://www.sms4india.com/api/v1/sendCampaign'
#
# #get Request
# def sendPostRequest(reqUrl,apikey,secretKey,useType,phoneNo,senderId,textMessage):
#     req_parms={
#         'apikey':apikey,
#         'secret':secretKey,
#         'usetype':useType,
#         'phone':phoneNo,
#         'message':textMessage,
#         'senderid':senderId
#     }
#     return requests.post(reqUrl,req_parms)
#
# values=randint(1000,9999,1)
# otp=str(values[0])
# response=sendPostRequest(url,'QTDKGH0WSCLQGVSXBOSOKMYYICOQ48ZH','MN21FE5PRXB3RGL3','stage','7792874337','7976365986',otp)
#
# print(response.text)
# otpv=input()
# if(otpv==otp):
#     print("OTP Verified")
# else:
#     print("Wrong Otp")
# ------------------------------------------------------------------------------------------
import pandas as pd
import sklearn.model_selection
import numpy as np
import pandas as pd

triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
songs_metadata_file = 'https://static.turi.com/datasets/millionsong/song_data.csv'

song_df_1 = pd.read_table(triplets_file,header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']
print(song_df_1.head())