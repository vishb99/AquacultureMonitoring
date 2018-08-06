import requests
import csv
import time


def create_initial_file():
    filename = "live_data.csv"
    with open(filename, 'a+') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(["MMSI", "IMO", "ShipId", "LAT", "LON", "Speed", "Heading", "Course", "Status", "TimeStamp", "DSRC", "UTC_Seconds"])


def write_data_to_csv(data):
    filename = "live_data.csv"
    with open(filename, 'a+') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in data:
            spamwriter.writerow(
                [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]])


def stream_data():
    create_initial_file()
    url = 'https://services.marinetraffic.com/api/exportvessels/v:8/46f63e3f6582d897ccd2b8443867c12c1e26c725/timespan:5/protocol:json'
    while True:
        try:
            response = requests.get(url)
            write_data_to_csv(response.json())
            print("added ship data")
        except:
            print("Unexpected error")

        time.sleep(120)

stream_data()