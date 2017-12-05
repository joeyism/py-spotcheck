#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import boto3
from datetime import datetime, timedelta
from terminaltables import AsciiTable


__version__ = "1.0.0"



today = datetime.today()
previous_day = today - timedelta(days=5)
date_format = "%Y-%m-%d"

class Spot_Price_History(object):
    AvailabilityZone = None
    InstanceType = None
    ProductDescription = None
    SpotPrice = None
    Timestamp = None

    def __init__(self, AvailabilityZone, InstanceType, ProductDescription, SpotPrice, Timestamp):
        self.AvailabilityZone = AvailabilityZone 
        self.InstanceType = InstanceType 
        self.ProductDescription = ProductDescription 
        self.SpotPrice = SpotPrice 
        self.Timestamp = Timestamp.strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return '{}\t{}\t{}\t{}\t{}'.format(self.Timestamp, self.AvailabilityZone, self.InstanceType, self.ProductDescription, self.SpotPrice)

    def toList(self):
        return [self.Timestamp, self.AvailabilityZone, self.InstanceType, self.ProductDescription, self.SpotPrice]



def printSpotHistories(histories):
    table_data = [
        ["Timestamp", "Availability Zone", "Instance Type", "Product Desc", "Spot Price($)"]
    ]
    histories.reverse()
    for history in histories:
        table_data.append(Spot_Price_History(**history).toList())
    table = AsciiTable(table_data)
    print(table.table)

@click.command()
@click.option("--InstanceType", prompt="Instance Type", default="t2.micro", help="The instance type of the spot instance")
@click.option("--ProductDescription", prompt="Product Description", default="Linux/UNIX", help="The product description, i.e. Linux/UNIX vs Windows")
@click.option("--StartTime", prompt="Start Time", default=previous_day.strftime(date_format), help="The start time of spot instances retrieval")
@click.option("--EndTime", prompt="End Time", default=today.strftime(date_format), help="The end time of spot instances retrieval")
def main(instancetype, starttime, endtime, productdescription):
    client = boto3.client("ec2")

    response = client.describe_spot_price_history(
            StartTime=starttime,
            EndTime=endtime,
            InstanceTypes=[instancetype],
            ProductDescriptions = [productdescription]
            )
    printSpotHistories(response["SpotPriceHistory"])

if __name__ == '__main__':
    main()
