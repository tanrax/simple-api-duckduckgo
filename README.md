# Simple API for DuckDuckGo

Simple API for DuckDuckGo that performs searches by scraping.

No money or registration is necessary.

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
  {
    "title": "Internet Speed Test | Fast.com",
    "link": "fast.com",
    "body": "Download speed is most relevant for people who are consuming content on the Internet, and we want FAST.com to be a very simple and fast speed test. What about ping, latency, upload and other things? When you click the \"Show more info\" button, you can see your upload speed and connection latency (ping).",
    "icon": "external-content.duckduckgo.com/ip3/fast.com.ico"
  },
  {
    "title": "Internet Speed Test - HighSpeedInternet.com",
    "link": "www.highspeedinternet.com/tools/speed-test",
    "body": "Use this tool to test your internet speed and compare it to others, find out how much speed you need, and learn how to improve your internet speed. Find out the fastest types of internet, the reasons for slow internet, and the best internet providers in your area.",
    "icon": "external-content.duckduckgo.com/ip3/www.highspeedinternet.com.ico"
  },
  {
    "title": "Test Definition & Meaning - Merriam-Webster",
    "link": "www.merriam-webster.com/dictionary/test",
    "body": "Learn the various meanings and uses of the word test as a noun, verb, and adjective. Find synonyms, examples, etymology, and related phrases of test in this comprehensive dictionary entry.",
    "icon": "external-content.duckduckgo.com/ip3/www.merriam-webster.com.ico"
  },
  {
    "title": "Internet Speed Test | Check Broadband Speed | Google Fiber",
    "link": "fiber.google.com/speedtest/",
    "body": "Test your internet speed and compare it with Google Fiber plans. Learn how to measure download, upload, ping and jitter speeds, and find out what factors affect your internet performance.",
    "icon": "external-content.duckduckgo.com/ip3/fiber.google.com.ico"
  },
  {
    "title": "TEST | English meaning - Cambridge Dictionary",
    "link": "dictionary.cambridge.org/dictionary/english/test",
    "body": "Learn the meaning of test as a noun and a verb in English, with synonyms, idioms, and usage examples. Find out how to use test in different contexts, such as medical, educational, or business, and how to test something or someone.",
    "icon": "external-content.duckduckgo.com/ip3/dictionary.cambridge.org.ico"
  },
  {
    "title": "TEST Definition & Usage Examples | Dictionary.com",
    "link": "www.dictionary.com/browse/test",
    "body": "Learn the meaning and usage of the word test as a noun and a verb, with synonyms, origin, and related terms. Find out how to use test in a sentence, with examples from various fields and contexts.",
    "icon": "external-content.duckduckgo.com/ip3/www.dictionary.com.ico"
  },
  {
    "title": "Test Definition & Meaning | Britannica Dictionary",
    "link": "www.britannica.com/dictionary/test",
    "body": "Learn the various meanings and uses of the word test, from a set of questions or problems to measure someone's skills, knowledge, or abilities, to a careful study of a part of the body or a substance taken from the body, to a planned and usually controlled act or series of acts to learn something, to see if something works properly, etc. See examples and synonyms for each meaning.",
    "icon": "external-content.duckduckgo.com/ip3/www.britannica.com.ico"
  },
  {
    "title": "Speedtest by Ookla - Apps on Google Play",
    "link": "play.google.com/store/apps/details?id=org.zwanoo.android.speedtest",
    "body": "Speedtest by Ookla is a popular app for testing your internet connection speed, ping, and video streaming quality. You can also compare providers, regions, and VPN options, and see real-world data and maps of mobile network coverage.",
    "icon": "external-content.duckduckgo.com/ip3/play.google.com.ico"
  },
  {
    "title": "TEST definition and meaning | Collins English Dictionary",
    "link": "www.collinsdictionary.com/dictionary/english/test",
    "body": "Learn the various meanings and uses of the word test as a verb and a noun, with synonyms, examples, and pronunciation. Find out how to test something, someone, or a situation, and what a test is in different contexts, such as chemistry, medicine, or sport.",
    "icon": "external-content.duckduckgo.com/ip3/www.collinsdictionary.com.ico"
  },
  {
    "title": "Test - Definition, Meaning & Synonyms | Vocabulary.com",
    "link": "www.vocabulary.com/dictionary/test",
    "body": "If your boss tells you not to test her patience, she means don't push her today, because she might just snap.",
    "icon": "external-content.duckduckgo.com/ip3/www.vocabulary.com.ico"
  },
  {
    "title": "Test - definition of test by The Free Dictionary",
    "link": "www.thefreedictionary.com/test",
    "body": "Define test. test synonyms, test pronunciation, test translation, English dictionary definition of test. n. 1. A procedure for critical evaluation; a means of determining the presence, quality, or truth of something; a trial: a test of one's eyesight;...",
    "icon": "external-content.duckduckgo.com/ip3/www.thefreedictionary.com.ico"
  },
  {
    "title": "COVID-19 diagnostic testing - Mayo Clinic",
    "link": "www.mayoclinic.org/tests-procedures/covid-19-diagnostic-test/about/pac-20488900",
    "body": "RT-PCR test. Also called a molecular test, this COVID-19 test detects genetic material of the virus using a lab technique called reverse transcription polymerase chain reaction (RT-PCR). A health care professional collects a fluid sample by inserting a long nasal swab (nasopharyngeal swab) into your nostril and taking fluid from the back of your nose.",
    "icon": "external-content.duckduckgo.com/ip3/www.mayoclinic.org.ico"
  },
  {
    "title": "Speedtest Apps: Our internet speed test available across a variety of ...",
    "link": "www.speedtest.net/apps",
    "body": "Speedtest Apps are free native apps that measure the speed of your broadband, cellular or Wi-Fi connection on each device. You can use them to check your connection straight from your mobile, desktop, browser, Apple TV or command line interface.",
    "icon": "external-content.duckduckgo.com/ip3/www.speedtest.net.ico"
  },
  {
    "title": "Test - Wikipedia",
    "link": "en.wikipedia.org/wiki/Test",
    "body": "Test cricket, a series of matches played by two national representative teams. Test match (rugby league), a match between teams of the Rugby League International Federation. Test match (rugby union), an international match usually played between two senior national teams. The Test (greyhound competition), a greyhound race run between 1941 and 2008.",
    "icon": "external-content.duckduckgo.com/ip3/en.wikipedia.org.ico"
  },
  {
    "title": "Internet Speed Test - Measure Network Performance | Cloudflare",
    "link": "speed.cloudflare.com",
    "body": "Test your Internet connection and check your network performance with Cloudflare's global edge network. See your download, upload, latency, jitter and packet loss results in seconds.",
    "icon": "external-content.duckduckgo.com/ip3/speed.cloudflare.com.ico"
  },
  {
    "title": "About Speedtest",
    "link": "www.speedtest.net/about",
    "body": "Speedtest is a global leader in internet performance testing and analysis, with over 18 million tests taken every day in more than 100 countries. Whether you want to check your download speed, upload speed, latency, or jitter, Speedtest can help you measure and improve your connection quality.",
    "icon": "external-content.duckduckgo.com/ip3/www.speedtest.net.ico"
  },
  {
    "title": "Speed Test by Speedcheck - Test my internet speed",
    "link": "www.speedcheck.org",
    "body": "Speed Test by Speedcheck is a tool that measures the connection speed and quality of your device to the internet. It runs multiple tests for download, upload and ping, and provides detailed explanations and tips for each aspect of your internet speed.",
    "icon": "external-content.duckduckgo.com/ip3/www.speedcheck.org.ico"
  },
  {
    "title": "Join a Test Meeting | Zoom",
    "link": "zoom.us/test",
    "body": "Join Meeting Test Test your internet connection by joining a test meeting. Join. If you are unable to join the meeting, visit Zoom Support Center for useful information.",
    "icon": "external-content.duckduckgo.com/ip3/zoom.us.ico"
  },
  {
    "title": "What do your blood test results mean? A toxicologist explains the ...",
    "link": "theconversation.com/what-do-your-blood-test-results-mean-a-toxicologist-explains-the-basics-of-how-to-interpret-them-216341",
    "body": "Normal blood test ranges. Depending on the lab that analyzed your sample, the results from your blood test may be broken down into individual tests or collections of related tests called panels ...",
    "icon": "external-content.duckduckgo.com/ip3/theconversation.com.ico"
  },
  {
    "title": "You can order a test to find out your biological age. Is it worth it? - NPR",
    "link": "www.npr.org/sections/health-shots/2024/02/05/1228753141/biological-age-test-dna",
    "body": "What the test can do is estimate how fast or slow you're aging compared to your peers. Let's say you're 50 and you get back an age of 45. That means you're aging slower than the average 50-year-old.",
    "icon": "external-content.duckduckgo.com/ip3/www.npr.org.ico"
  },
  {
    "title": "Crash tests indicate nation's guardrail system can't handle heavy ...",
    "link": "apnews.com/article/electric-vehicles-crash-test-guardrails-nebraska-3ec299a7ad87d0f63a6dd9357f663fce",
    "body": "Trevor Donahoo, Engineering Testing Technician, connects testing equipment inside the Rivian cab during a crash test research by the U.S. Army Engineer Research and Development Center and the University of Nebraska-Lincoln's Midwest Roadside Safety Facility on Oct. 12, 2023 in Lincoln, Neb. Preliminary tests point to concerns that the nation's roadside guardrails are no match for new heavy ...",
    "icon": "external-content.duckduckgo.com/ip3/apnews.com.ico"
  },
  {
    "title": "ETS Announces TOEFL® TestReady™",
    "link": "www.ets.org/news/press-releases/introducing-toefl-testready-new-era-test-preparation.html",
    "body": "Princeton, N.J. (February 7, 2024) - ETS announced today an innovative, first-of-its-kind test prep platform for learners preparing for the TOEFL iBT ® test. With the goal of elevating test takers to their highest proficiency, TOEFL ® TestReady™ cements itself as the only comprehensive test prep platform currently available that leverages AI to offer personalized insights and targeted ...",
    "icon": "external-content.duckduckgo.com/ip3/www.ets.org.ico"
  },
  {
    "title": "TEST | definition in the Cambridge English Dictionary",
    "link": "dictionary.cambridge.org/us/dictionary/english/test",
    "body": "Learn the meaning of test as a noun and a verb in English, with synonyms, idioms, and usage examples. Find out how to use test in different contexts, such as medical, educational, or business, and how to test someone or something.",
    "icon": "external-content.duckduckgo.com/ip3/dictionary.cambridge.org.ico"
  },
  {
    "title": "Test your English - Every level and every skill",
    "link": "test-english.com",
    "body": "Unlock your language potential with 10-minute daily lessons, personalized corrections, level assessments, and certificates. Try one month FREE! On test-english.com you will find lots of free English exam practice materials to help you improve your English skills: grammar, listening, reading, writing.",
    "icon": "external-content.duckduckgo.com/ip3/test-english.com.ico"
  },
  {
    "title": "Axe: Syracuse basketball passes first test after an emotional week ...",
    "link": "www.syracuse.com/orangebasketball/2024/02/axe-syracuse-basketball-passes-first-test-after-an-emotional-week-podcast.html",
    "body": "Brent Axe | baxe@syracuse.com. Syracuse, N.Y. —It's been an emotional week for the Syracuse University men's basketball team. Head coach Adrian Autry dropped the hammer in his postgame press ...",
    "icon": "external-content.duckduckgo.com/ip3/www.syracuse.com.ico"
  },
  {
    "title": "Giants Insider: Saquon Barkley Likely to Test 2024 NFL Free Agency for ...",
    "link": "bleacherreport.com/articles/10108374-giants-insider-saquon-barkley-likely-to-test-2024-nfl-free-agency-for-new-contract",
    "body": "The New York Giants have the option of placing the franchise tag on star running back Saquon Barkley for the second straight offseason, but it sounds like they're willing to let him test free agency.",
    "icon": "external-content.duckduckgo.com/ip3/bleacherreport.com.ico"
  },
  {
    "title": "Senate takes first step toward debating foreign aid package ... - CNN",
    "link": "www.cnn.com/2024/02/07/politics/senate-takes-test-vote-foreign-aid/index.html",
    "body": "The Senate voted on Wednesday to take the first step toward debating a major foreign aid package with assistance for Ukraine and Israel without border security provisions, but a key test vote ...",
    "icon": "external-content.duckduckgo.com/ip3/www.cnn.com.ico"
  },
  {
    "title": "Speedtest oleh Ookla - Uji Kecepatan Broadband Global",
    "link": "www.speedtest.net/id",
    "body": "Speedtest oleh Ookla adalah aplikasi yang memungkinkan Anda mengurangi kecepatan jaringan internet Anda di semua perangkat. Anda dapat menggunakan Speedtest di Android, iOS, Windows, Mac, Chrome, AppleTV, CLI, dan aplikasi bawaan gratis untuk menunggu hasil pengaturan, analisis, dan solusi jaringan.",
    "icon": "external-content.duckduckgo.com/ip3/www.speedtest.net.ico"
  },
  {
    "title": "FFXIV Xbox Series Open Beta Test Details - IGN",
    "link": "www.ign.com/wikis/ffxiv/FFXIV_Xbox_Series_Open_Beta_Test_Details",
    "body": "The full launch is scheduled immediately after the conclusion of the open beta test, and all game data will be transferred and a redownload won't be required. Up Next: FFXIV 6.5 Patch Notes.",
    "icon": "external-content.duckduckgo.com/ip3/www.ign.com.ico"
  }
]
```
