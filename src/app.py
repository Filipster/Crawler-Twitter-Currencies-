from argparse import Namespace
# from src.services import twitter
from src.services import twitter_v2
import pandas as pd


def serve(args: Namespace) -> None:
    print(args)

    if args.stream == 1:
        pass
    else:
        tweets = twitter_v2.sample_tweet(
            args.term, args.stream, args.limit)

    if args.persist == 'screen':
        print(tweets)
    elif args.persist == 'txt':
        res = pd.DataFrame.from_dict(tweets)
        res.to_csv('src/data/export.txt', mode='w', index=False, sep=";")
