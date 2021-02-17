import argparse
import datetime

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
        choices=[0, 1],
        default=0,
        help="""How the app should get data. If this option set to 0,
            then provide a date for -sDate and -eDate""")

    parser.add_argument(
        '-sDate',
        '--startDate',
        type=str,
        default=str(datetime.datetime.now().strftime('%Y-%m-%d 00:00:00')),
        help='When set to 0, the app will get data from this date to -eDate')

    parser.add_argument(
        '-eDate',
        '--endtDate',
        type=str,
        default=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        help="""When stream set to 0,
            the app will get data from startDate to this""")

    args = parser.parse_args()
    print(args)
