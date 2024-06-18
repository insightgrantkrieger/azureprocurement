from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import csv,json
import os
import glob
from pathlib import Path


class ChunkPDF():

    def ProcessAllPDFIntoCSV(self,ResponseID:int,InputPath:str,OutputPath:str):
        
        Path(InputPath).mkdir(parents=True, exist_ok=True)
        Path(OutputPath).mkdir(parents=True, exist_ok=True)       
        [f.unlink() for f in Path(OutputPath).glob("*") if f.is_file()] 
        txtfiles = []
        for file in glob.glob(InputPath+"*.pdf"):
          self.Process1PDFIntoCSV(ResponseID,file,OutputPath)

            

    def Process1PDFIntoCSV(self,ResponseID:int,InputPathAndFilename:str,OutputPath:str):
            print(InputPathAndFilename)

            InputFilename = InputPathAndFilename.split(os.sep)[-1]
            OutputFilename = InputFilename.replace(".pdf",".csv")
            OutPathAndFilename = os.path.join(OutputPath, OutputFilename)

            sourcefile = "1. Expression of Interest -  Briefing Document.pdf"
            loader = PyPDFLoader(InputPathAndFilename)
            pages = loader.load()

            # split documents into text

            text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False
            )

            chunks = text_splitter.split_documents(pages)
            i = 0
            with open(OutPathAndFilename, "w",newline='', encoding='utf-8') as csvfile:
                fieldnames = ['metadata_storage_name','ResponseID', 'Page','Chunk','content']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter='|')

                writer.writeheader()
                while i < len(chunks):
                    current_chunk = chunks[i]
                    page_content_clean = current_chunk.page_content.replace("\n", " ").replace("\"", ",").replace("|", ",")
                    values = {'metadata_storage_name':sourcefile,'ResponseID': ResponseID, 'Page': 0,'Chunk': i,'content':page_content_clean}
                    writer.writerow(values)
                    i += 1





