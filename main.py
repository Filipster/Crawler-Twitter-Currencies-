import argparse
import datetime
from src import app

if __name__ == '__main__':
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
        default=str(datetime.datetime.now().strftime('%Y%m%d0000')),
        help='When set to 0, the app will get data from this date to -eDate')

    parser.add_argument(
        '-eDate',
        '--end_date',
        type=str,
        default=str(datetime.datetime.now().strftime('%Y%m%d%H%M')),
        help="""When stream set to 0,
            the app will get data from startDate to this""")

    args = parser.parse_args()
    app.serve(args)
