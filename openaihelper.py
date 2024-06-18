import json
import os
from openai import AzureOpenAI


class OpenAIHelper():

 def Prompt(self, UserPrompt: str, SystemPrompt: str):
    #endpoint = "https://insightassistsearch.openai.azure.com/"
    #deployment = "gpt35turbo16k"

    client = AzureOpenAI(
        api_key = os.environ['openai_api_key'],  
        api_version = os.environ['openai_api_version'],
        azure_endpoint = os.environ['openai_api_endpoint']
    )
      
    completion = client.chat.completions.create(
        model=os.environ['openai_modelname'],
        messages=[
        {
                "role": "system",
                "content": SystemPrompt,
            },
            {
                "role": "user",
                "content": UserPrompt,
            }
        ]
    )
      
    jsondata = json.loads(completion.to_json())

    response = jsondata["choices"][0]["message"]["content"]
    return response
 
 
