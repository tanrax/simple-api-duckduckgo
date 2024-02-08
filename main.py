from typing import Union
from fastapi import FastAPI
from gateways.externals import DuckDuckGoGateway
from use_cases import search_ddg

app = FastAPI()

@app.get("/search/")
def api_search(q: str):
    repo = DuckDuckGoGateway()
    return search_ddg(repo, q)
