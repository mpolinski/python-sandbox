"""
Retrieve and print words from URL

Usage:
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen

# 'http://sixty-north.com/c/t.txt'


def fetch_words(url):
    """
    Fetch a list of words from URL

    Args:
        url: The URL of a UTF-8 text doxument

    Returns:
        A list of strings containing the words from
        the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(story_words):
    for word in story_words:
        print(word)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    url = sys.argv[1]   # Oth argument is the module name
    main(url)
