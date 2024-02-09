import requests
from bs4 import BeautifulSoup
from typing import Union

class DuckDuckGoGateway:
    """Gateway to DuckDuckGo search engine"""
    url = "https://duckduckgo.com/html/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0",
    }

    def search(self, query: str) -> Union[dict, list]:
        """ Search DuckDuckGo for a query
        Args:
            query (str): The query to search for
        Returns:
            Union[dict, list]: A list of search results
            Example:
            [
                {
                    "title": "DuckDuckGo — Privacy, simplified.",
                    "link": "https://duckduckgo.com/",
                    "body": "The Internet privacy company that empowers you to seamlessly take control of your personal information online, without any tradeoffs.",
                    "icon": "/assets/meta/DDG-icon_256x256.png",
                },
                ...
            ]
        """
        data_output = []
        response = requests.get(self.url, headers=self.headers, params={"q": query})
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("div", class_="result")
        for result in results:
            title = result.find("h2", class_="result__title").find("a").text.strip()
            link = result.find("div", class_="result__extras__url").text.strip().splitlines()[0]
            body = result.find("a", class_="result__snippet").text.strip()
            icon_obj = result.find("img", class_="result__icon__img")
            icon = icon_obj["src"][2:] if icon_obj else False

            data_output.append(
                {
                    "title": title,
                    "link": link,
                    "body": body,
                    "icon": icon,
                }
            )
        return data_output
