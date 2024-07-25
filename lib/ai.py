import json

import requests
from openai import AzureOpenAI

from .config import config
from .database import TenderEvent, TenderPartitipant, TenderQuestions


def ask_question_to_ai(
    tender: TenderEvent, participant: TenderPartitipant, question: TenderQuestions
) -> str:
    """Ask the AI the question and return the answer."""

    # Perform the AISearch first, to find some relevant documents sections.
    aisearch_results = call_aisearch(question.ai_search, participant.id, 2)

    UserPrompt = f"Document content: {aisearch_results}. "
    f"Question start: {question.ai_ask}. "
    return call_openai_chat(UserPrompt, question.system_prompt)


def call_aisearch(ai_search: str, filter_id: int, top: int) -> str:
    """Call the AI search with the search term and return the result.

    :param ai_search: The search term to use.
    :param filter_id: The filter to use, i.e. only consider documents with this id.
    :param top: The number of results to return.
    """
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "api-key": config.aisearch_api_key,
    }

    body = {
        "search": ai_search,
        "filter": f"ResponseID eq {filter_id}",
        "top": top,
    }

    response = requests.post(config.aisearch_url, headers=headers, json=body)
    if response.status_code != 200:
        print(f"Error calling AISearch: {response.status_code}")
        print(response.text)
        return ""
    return response.text


def call_openai_chat(user_prompt: str, system_prompt: str) -> str:
    """Call the OpenAI chat API and return the response."""

    oai_client = AzureOpenAI(
        api_key=config.openai_api_key,
        api_version=config.openai_api_version,
        azure_endpoint=config.openai_endpoint,
    )

    completion = oai_client.chat.completions.create(
        model=config.openai_modelname,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    response = json.loads(completion.to_json())
    return response["choices"][0]["message"]["content"]
