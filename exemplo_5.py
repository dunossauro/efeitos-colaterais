from typing import Text
from urllib.request import urlopen


def web_scrap_pika(url: str) -> Text:
    """Dada uma url, retorna o html da página."""
    return urlopen(url).read()


web_scrap_pika('http://gogle.com.br/')
# web_scrap_pika('http://google.com.br/')
