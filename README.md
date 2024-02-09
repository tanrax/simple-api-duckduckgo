# Simple API for DuckDuckGo

Simple API for DuckDuckGo that performs searches by scraping.

No money or registration is necessary.

## Use 🚀

```sh
curl localhost:8000/search/?q=test
```

Return

```json
[
  {
    "title": "Test - Test de CI Oficial",
    "link": "test-iq-online.com",
    "body": "Test oficial en Francia. 20 preguntas en 20 minutos. La prueba de CI oficial determina su CI y envía resultados certificados.",
    "icon": false
  },
  {
    "title": "Speedtest by Ookla - The Global Broadband Speed Test",
    "link": "www.speedtest.net",
    "body": "Speedtest by Ookla is a global broadband speed test that lets you measure your internet connection speed and performance. You can also access various features and insights on network performance, 5G deployment, and enterprise solutions.",
    "icon": "external-content.duckduckgo.com/ip3/www.speedtest.net.ico"
  },
...
]
```

## Endpoints 🛣️

`/search/` - Search for a term.

Params:
- `q` - The term to search for.

## Requirements 📋

- [Docker](https://www.docker.com/).
- [Docker Compose](https://docs.docker.com/compose/install/).

## Run 🏃

```
docker compose up
```

## Roadmap 🗺️

- [x] Param Query
- [ ] Good testing
- [ ] Param region
- [ ] Param time
- [ ] Pagination

## Nerd stuff 🤓

- Language: Python
- Architecture: Clean architecture
- Libraries: FastAPI, requests, beautifulsoup4, uvicorn and pytest.
