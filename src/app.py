from argparse import Namespace
from src.services import twitter


def serve(args: Namespace) -> None:
    print(args.stream)

    twitter.login()
