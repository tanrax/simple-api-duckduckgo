from fastapi import FastAPI
from gateways.externals import DuckDuckGoGateway
from use_cases import search_ddg

app = FastAPI()

@app.get("/search/")
def api_search(q: str):
    """Search for a query in DuckDuckGo.
    Args:
        q (str): The query to search for.
    Returns:
        dict: The search results."""
    repo = DuckDuckGoGateway()
    return search_ddg(repo, q)
