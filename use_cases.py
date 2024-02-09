from typing import Union

def search_ddg(repo, query: str) -> Union[dict, list]:
    """Search DuckDuckGo for a query
    Args:
        repo (DuckDuckGoGateway): The DuckDuckGoGateway repository
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
    return repo.search(query)
