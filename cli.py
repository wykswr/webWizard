from argparse import ArgumentParser
from src.utils import summarize, summarize_with_topic


def get_args():
    parser = ArgumentParser(description='A simple CLI for website summarization')
    parser.add_argument('url', type=str, help='URL of the website to summarize')
    parser.add_argument('--topic', '-t', type=str, help='Topic of the website')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    if args.topic:
        print(summarize_with_topic(args.url, args.topic))
    else:
        print(summarize(args.url))
