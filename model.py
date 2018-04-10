# model.py
import csv

BB_FILE_NAME = 'umbball.csv'
FB_FILE_NAME = 'umfootball.csv'

ball_seasons = []


def init_ball(ball):
    global ball_seasons
    if ball == 'BB':
        csv_file_name = BB_FILE_NAME
        with open(csv_file_name) as f:
            reader = csv.reader(f)
            next(reader)  # throw away headers
            next(reader)  # throw away headers
            ball_seasons = []  # reset, start clean
            for r in reader:
                r[3] = int(r[3])
                r[4] = int(r[4])
                r[5] = float(r[5])
                ball_seasons.append(r)
    else:
        csv_file_name = FB_FILE_NAME
        with open(csv_file_name) as f:
            reader = csv.reader(f)
            next(reader)  # throw away headers
            ball_seasons = []  # reset, start clean
            for r in reader:
                r[3] = int(r[3])
                r[4] = int(r[4])
                r.remove(r[5])
                r[5] = float(r[5])
                ball_seasons.append(r)


def get_ball_seasons(sortby='year', sortorder='desc'):

    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(ball_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list
