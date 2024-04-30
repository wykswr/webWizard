# webWizard
A simple CLI allowing you to summarize web pages and articles.

## Setup

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

Some websites have anti-scraping measures such as javascript rendering and IP blocking. We use [FireCrawl](https://www.firecrawl.dev) to bypass these measures,
get your API key from [FireCrawl](https://www.firecrawl.dev) and set it in credentials.json file.

The LLM we use is gpt-3.5-turbo-0125, set up your OpenAI API key in the credentials.json file.

The credentials.json file should look like this:

```json
{
    "fire_crawl_api_key": "YOUR_FIRECRAWL_API_KEY",
    "open_ai_api_key": "YOUR_OPENAI_API_KEY"
}
```

## Usage

To summarize a web page, run the following command:

```
python cli.py <URL>
```

To summarize a web page with respect to a specific topic, run the following command:

```
python cli.py <URL> --topic <TOPIC>
```

## Example

Summarize BBC news article:

```
python cli.py https://www.bbc.com/news/uk-england-lincolnshire-68908558
```

Check the Fairview Crescent residence on UBC Housing website:

```
python cli.py https://vancouver.housing.ubc.ca/residences-rooms/residences/ --topic "Fairview Crescent"
```

## Limitations
* We don't control context length, if your input is too long, the model might not be able to summarize it.
* The current design does not support memory.