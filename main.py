import argparse
import sys
from src import app

if __name__ == '__main__':
    sys.path.append("./")
    parser = argparse.ArgumentParser(description='A Crawler for twitter API')

    parser.add_argument(
        '-t',
        '--term',
        type=str,
        required=True,
        help='Term to be crawled')

    parser.add_argument(
        '-p',
        '--persist',
        type=str,
        choices=['screen', 'txt', 'sql', 'nosql'],
        default='screen',
        help='How the application will persist data')

    parser.add_argument(
        '-s',
        '--stream',
        type=int,
        choices=[-1, 0, 1],
        default=-1,
        help="""How the app should get data. If this option set to 0,
            then provide a date for -sDate and -eDate""")

    parser.add_argument(
        '-sDate',
        '--start_date',
        type=str,
        default=0,
        help="""How the app should get data.""")

    parser.add_argument(
        '-l',
        '--limit',
        type=int,
        default=1,
        help='How much tweets will be crawled.')

    args = parser.parse_args()
    app.serve(args)
