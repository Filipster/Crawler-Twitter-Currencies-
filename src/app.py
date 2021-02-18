from argparse import Namespace
from dotenv import load_dotenv
import os


def serve(args: Namespace) -> None:
    load_dotenv('./src/env/.env')

    print(args.stream)
    print(os.getenv("NOSQL_PASS"))
