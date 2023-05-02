from re import findall
from typing import List
import requests
import json


def get_tag_content(tag: str, data: str) -> List[str]:
    """
    The function returns list of contents of specified HTML-tag.
    :param tag: HTML-tag
    :param data: source HTML-code
    """
    pattern = fr'>.*</{tag}>'
    closing_tags_length = len(tag) + 3
    matches = findall(pattern, data)
    result = [match[1:-closing_tags_length] for match in matches]
    return result


if __name__ == '__main__':
    # Test 1:
    with open('examples.html', 'r') as f:
        text = f.read()
    print(get_tag_content('h3', text))

    # Test 2:
    # TODO
    request = requests.get('https://nhl.com/')
    data = json.loads(request.text)
    print(data)
