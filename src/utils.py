import json
from pathlib import Path

from langchain_community.document_loaders import FireCrawlLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

with (Path(__file__).parent.parent / 'credential.json').open() as f:
    credential = json.load(f)

with (Path(__file__).parent / 'roles' / 'basic.json').open() as f:
    basic_summarizer = json.load(f)

with (Path(__file__).parent / 'roles' / 'topic.json').open() as f:
    topic_summarizer = json.load(f)

llm = ChatGroq(temperature=0, model_name="llama3-70b-8192", groq_api_key=credential['groq_api_key'])


def crawl(url: str) -> str:
    """
    Crawl the content of the given URL. FireCrawl is used to handle the anti-scraping mechanism, such as
    JavaScript rendering and IP blocking.
    :param url: URL to crawl
    :return: Content of the URL
    """
    loader = FireCrawlLoader(
        api_key=credential['fire_crawl_api_key'],
        url=url,
        mode="scrape"
    )
    docs = loader.load()
    return docs[0].page_content


def summarize(url: str) -> str:
    """
    Summarize the content of the given URL.
    :param url: URL to summarize
    :return: Summarized content
    """
    system, human = basic_summarizer['system'], basic_summarizer['human']
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({'content': crawl(url)})


def summarize_with_topic(url: str, topic: str) -> str:
    """
    Summarize the content of the given URL with the specified topic.
    :param url: URL to summarize
    :param topic: Topic to summarize
    :return: Summarized content
    """
    system, human = topic_summarizer['system'], topic_summarizer['human']
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({'content': crawl(url), 'topic': topic})
