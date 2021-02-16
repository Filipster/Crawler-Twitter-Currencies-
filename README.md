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
- **-sDate or --startDate**: (OPTIONAL) If _-s_ were not given, then choose a start date do look for tweets. **PATTERN**: "YYYY-MM-DD HH:ii:SS"
- **-eDate or --endDate**: (OPTIONAL) If _-sDate_ were given, then choose a end date do look for tweets. **PATTERN**: "YYYY-MM-DD HH:ii:SS" || **DEFAULT VALUE**: "now()"

### Examples

- _python main.py -t "bitcoin" -p "txt" -s_ || This will start the application for ingest stream of "bitcoin" tweets and save them on a .txt file
- _python main.py -t "monero" -p "nosql" -sDate "2021-02-10 00:00:00" -eDate "2021-02-10 23:59:59"_ || This will start the application for ingest "monero" tweets from sDate to eDate and save them on a noSQL database
- _python main.py -t "monero" -p "screen" -s_ || This will start the application for ingest stream of "monero" tweets and just print them on the screen
