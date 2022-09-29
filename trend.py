from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import sys
import tweepy
import json
from trendanalysis import *
from trendanalysistextblob import *
from PIL import ImageTk,Image
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="pass",
  database="twitterDb"
)
class TrendClass():
    def __init__(self , master):
        self.master = master
         
        
        master.configure(background='white')
        master.geometry("%dx%d+0+0" % (700, 600))
        #master.geometry("700x600")        
        #master.resizable(0, 0)
        
        #==============================FRAMES=========================================

        Form = Frame(master,highlightbackground="black", highlightcolor="black", highlightthickness=2,height=600, width=700)
        Form.configure(bg="white")
        Form.pack(side=TOP)
        
        label = Label(Form,bg="white")
        label.grid(row=0)
        image = ImageTk.PhotoImage(Image.open("welcome2.jpg"))
        label.config(image = image)
        label.image = image
   
        lbl_id = Label(Form,bg="white",fg="black", text = "Enter Trend Name", font=('arial', 14))
        lbl_id.grid(row=3)

        self.input_trend = Entry(Form,bg="white",font=('arial', 14),bd=2)
        self.input_trend.grid(row=4)
   
        #==============================BUTTON WIDGETS=================================
        btn_trend = Button(Form,bg="#5eabde",fg="white", text="Search Trend", width=25, command=self.SearchTrendsWithKeyword)
        btn_trend.grid(row=7,pady=10)
        
        btn_trend_All = Button(Form,bg="#5eabde",fg="white", text="Search All Trend", width=25, command=self.SearchTrends)
        btn_trend_All.grid(row=8,pady=10)
        
        lbl_trend_head = Label(Form,bg="white",fg="Red", text = "Twitter Trends List", font=('arial', 14))
        lbl_trend_head.grid(row=9)
        
        self.Trend_List = Listbox(Form,width=100)
        self.Trend_List.grid(row=10,pady=10)
        
        btn_Perform_Analysis = Button(Form,bg="#5eabde",fg="white", text="Show Analysis Using Classifier", width=25, command=self.PerformAnalysisOnTrend)
        btn_Perform_Analysis.grid(row=11,pady=10)
        
        btn_Perform_Analysis_TextBlob = Button(Form,bg="#5eabde",fg="white", text="Show Analysis Using Text Blob", width=25, command=self.PerformAnalysisOnTrendTextBlob)
        btn_Perform_Analysis_TextBlob.grid(row=12,pady=10)
        
    #Fucntion to perform analysis on trend
    def PerformAnalysisOnTrendTextBlob(self):
        trend_name=self.Trend_List.get(ACTIVE)
        # Write the selected trend on temporary file
        file = open("temp.txt","w+")
        file.write(trend_name)  
        file.close()       
        print(self.Trend_List.get(ACTIVE))
       # self.master.withdraw() 
        self.newWindow = Toplevel(self.master)        
        self.app = TrendAnalysisClassTextBlob(self.newWindow) 
    
    #Fucntion to perform analysis on trend
    def PerformAnalysisOnTrend(self):
        trend_name=self.Trend_List.get(ACTIVE)
        # Write the selected trend on temporary file
        file = open("temp.txt","w+")
        file.write(trend_name)  
        file.close()       
        print(self.Trend_List.get(ACTIVE))
        #self.master.withdraw() 
        self.newWindow = Toplevel(self.master)        
        self.app = TrendAnalysisClass(self.newWindow)        

    
    #Fucntion to search trends matching the search keyword for WOE Id India
    def SearchTrendsWithKeyword(self):
        # self.input_trend.delete(0,END)
        # self.input_trend.insert(0,'')
        self.Trend_List.delete(0,END)
        #Autentication
        consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        WOE_ID = 20070458 #India WOE ID
        twitter_trends = api.trends_place(WOE_ID) 
         
        trends = json.loads(json.dumps(twitter_trends, indent=1))       
        
        cnt=1
        searchKeyword=self.input_trend.get()
        
        for trend in trends[0]["trends"]:
            if trend["name"].find(searchKeyword)!=-1:
               self.Trend_List.insert(cnt, trend["name"])
               cnt+=1
     
    #Fucntion to search all trends for WOE Id India
    def SearchTrends(self):
        # self.input_trend.delete(0,END)
        # self.input_trend.insert(0,'')
        self.Trend_List.delete(0,END)
        #Autentication
        consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        WOE_ID = 20070458 #India WOE ID
        twitter_trends = api.trends_place(WOE_ID) 
         
        trends = json.loads(json.dumps(twitter_trends, indent=1))       
        
        cnt=1
        
        for trend in trends[0]["trends"]:
            self.Trend_List.insert(cnt, trend["name"])
            cnt+=1
            #print (trend["name"])
        
     
    
