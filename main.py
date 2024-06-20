from chunkpdf import ChunkPDF
from sqlhelper import SQLHelper 
from chunkpdf import ChunkPDF 
from aisearchhelper import AISearchHelper
from openaihelper import OpenAIHelper
from confighelper import ConfigHelper

print("Started")

ConfigA = ConfigHelper()
ConfigA.SetEnvironmentVariables()

ResponseID = 1   # client 1
PromptGroupID = 1  # Procurement campaign / area of business   Batch of Q and A

s = SQLHelper()
prompts = s.get_prompts(PromptGroupID)
a = AISearchHelper()
o = OpenAIHelper()
i = 0
while i < len(prompts):
    response = a.Search(ResponseID,prompts[i].aisearchtext,2)
    #Prompt after search with Q and A
    UserPromptFinal = "Document content: "+response+" Question start : "+prompts[i].UserPrompt
    ResultText = o.Prompt(UserPromptFinal,prompts[i].SystemPrompt)
    UserPromptFinalScore = "Score the following between 1 and 5 based on how well the answer was able to answer the question. Only return an integer between 1 and 5. If the answer is unable to answer the question it would be 1. If the answer is able to answer the question correctly it would be 5 : "+UserPromptFinal+" Answer:"
    ResultScore = o.Prompt(UserPromptFinalScore,prompts[i].SystemPrompt)
    s.insert_promptoutput(PromptGroupID,ResponseID,ResultText,ResultScore)
    print("Completed prompt "+prompts[i].Description)
    i+=1

print("Completed all")