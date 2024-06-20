import os
class ConfigHelper():
    def SetEnvironmentVariables(self):
      os.environ["sql_connection_string"] = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:xxxx.database.windows.net,1433;Database=insightassistsqldb;UID=u4563;PWD=sqlhello_1H;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"
      os.environ["openai_api_key"] = "xxxx"
      os.environ["openai_api_version"] = "2024-02-01"
      os.environ["openai_api_endpoint"] = "https://xxxx.openai.azure.com/"
      os.environ["openai_modelname"] = "xxxx"
      os.environ["aisearch_api_endpoint"] = "https://xxxx.search.windows.net/indexes/azureblob-index/docs/search?api-version=2023-11-01"
      os.environ["aisearch_api_key"] = "xxxxx"
      #test
      #test





