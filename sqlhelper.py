import os
import pyodbc, struct

class Prompt():
    PromptID: int
    PromptGroupID: str
    Description: str
    UserPrompt: str
    SystemPrompt: str
    aisearchtext: str


class SQLHelper():
    def __init__(self):  
        self.connection_string = os.environ['sql_connection_string']

    def get_promptgroups(self):
            rows = []
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT promptgroupid,promptgroupname FROM dbo.promptgroup")

            for row in cursor.fetchall():
                print(row.promptgroupid, row.promptgroupname)
                rows.append(f"{row.promptgroupid}, {row.promptgroupname}")
            return rows

    def get_prompts(self,promptgroupid: int):
            rows = []
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT [PromptID],[PromptGroupID],[Description],[UserPrompt],[SystemPrompt],[aisearchtext] FROM dbo.prompt where promptgroupid = "+str(promptgroupid))

            for row in cursor.fetchall():
                p1 = Prompt()
                p1.PromptID = row.PromptID
                p1.PromptGroupID = row.PromptGroupID
                p1.Description = row.Description
                p1.UserPrompt = row.UserPrompt
                p1.SystemPrompt = row.SystemPrompt
                p1.aisearchtext = row.aisearchtext
                rows.append(p1)
            return rows

    def insert_promptoutput(self,PromptID: int,ResponseID: int,PromptOutput: str,PromptScore: int):
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO promptoutput (PromptID, ResponseID,PromptOutput,PromptScore) VALUES (?, ?, ?, ?)", PromptID, ResponseID, PromptOutput,PromptScore )
            conn.commit()

