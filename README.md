# Crawler Twitter Project

## Goals

- Build an application to ingest tweets about criptocurrencies
- Aimed for: **Bitcoin and Monero**

## Technology

- Python 3.7.5
- TinyDB (mongo like)
- SQLlite (mysql like)

## How to use

1. Clone this repository (git clone https://gitlab.com/dataflow1/crawler-twitter-currencies.git)
2. Create a virtual environment _(skippable)_
3. Run pip install -r requirements.txt
   - If you are on mac or linux: pip3 install -r requirements.txt
4. Run python main.py (plus the suffixes explained below)

## Suffixes for the Main.py

- **-t or --term**: (OBRIGATORY) Searches for the given term.
- **-p or --persist**: (OBRIGATORY) Chooses which mode to persist tweets data. **OPTIONS**: ['txt', 'sql', 'nosql', 'screen']
- **-s or --stream**: (OPTIONAL) Enables the application to ingest tweets by stream of data. Every new tweet with the choosen word will be ingested.
- **-l or --limit**: (OPTIONAL) Limit the number of tweets crawled

### Examples

- _python main.py -t "bitcoin" -p "txt" -s_ || This will start the application for ingest stream of "bitcoin" tweets and save them on a .txt file

