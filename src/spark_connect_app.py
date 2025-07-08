#!/usr/bin/env python3

from datetime import datetime, date

from pyspark.sql import Row
from pyspark.sql import SparkSession


def run_job():
    spark = SparkSession.builder.remote("sc://localhost:15002").getOrCreate()
    df = spark.createDataFrame([
        Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
        Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
        Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
    ])
    df.show()


if __name__ == "__main__":
    run_job()
