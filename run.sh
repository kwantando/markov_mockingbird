#!/usr/bin/env bash

if [ -f dadtellsjokes.json ]; then
    rm dadtellsjokes.json
fi

scrapy runspider scraper.py -o dadtellsjokes.json

if [ -f dadtellsjokes.txt ]; then
    rm dadtellsjokes.txt
fi

python3 formatter.py dadtellsjokes

if [ -f dadJokes.db ]; then
    rm dadJokes.db
fi

python ../markov-text-master/markov.py parse dadJokes 3 dadtellsjokes.txt
python ../markov-text-master/markov.py gen dadJokes 10
