import csv,json
import os
import glob
import requests
import json

class AISearchHelper():
    
      
    def Search(self,ResponseID:int,SearchText:str,Top:int):
        url = os.environ['aisearch_api_endpoint']       
        headers = {"Content-Type": "application/json; charset=utf-8" ,"api-key" : os.environ['aisearch_api_key']}       
        data = {
                
                "search": ""+SearchText+"",
                "filter": "ResponseID eq "+str(ResponseID),
                "top": Top
                
               }
 
        response = requests.post(url, headers=headers, json=data)  
        return response.text


   