from typing import Union

def search_ddg(repo, query: str) -> Union[dict, list]:
    return repo.search(query)
