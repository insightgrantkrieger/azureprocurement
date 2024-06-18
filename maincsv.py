from chunkpdf import ChunkPDF
from sqlhelper import SQLHelper 
from chunkpdf import ChunkPDF 
from aisearchhelper import AISearchHelper

print("Started")
ResponseID = 1   # client 1
PromptGroupID = 1  # Procurement campaign / area of business   Batch of Q and A
c = ChunkPDF()
c.ProcessAllPDFIntoCSV(ResponseID,"C:\\azureprocurement\\source\\","C:\\azureprocurement\\output\\")
print("Completed")