import os
class ConfigHelper():
    def SetEnvironmentVariables(self):
      os.environ["sql_connection_string"] = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:xxxx.database.windows.net,1433;Database=xxxxx;UID=u4563;PWD=xxxxx;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"
      os.environ["openai_api_key"] = "xxxxxxxxxx"
      os.environ["openai_api_version"] = "2024-02-01"
      os.environ["openai_api_endpoint"] = "https://xxxxxx.openai.azure.com/"
      os.environ["openai_modelname"] = "xxxxx"
      os.environ["aisearch_api_endpoint"] = "https://xxxxx.search.windows.net/indexes/azureblob-index/docs/search?api-version=2023-11-01"
      os.environ["aisearch_api_key"] = "xxxxxx"
      #test
      #test





