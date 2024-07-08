from pydantic_settings import BaseSettings


class Config(BaseSettings):
    db_user: str = ""
    db_pass: str = ""
    debug: bool = False
    aisearch_api_key: str = ""
    openai_api_key: str = ""
    local: bool = False

    # The following we just keep here for reference.
    # When needed we can override them via environment variables.
    aisearch_url: str = (
        "https://eql-ai-sandbox-search.search.windows.net/indexes/"
        "azureblob-index/docs/search?api-version=2016-09-01"
    )
    openai_api_version: str = "2024-02-01"
    openai_endpoint: str = "https://eql-ai-workshop-sandbox.openai.azure.com/"
    openai_modelname: str = "gpt-4"


config = Config(_env_file=".env")
