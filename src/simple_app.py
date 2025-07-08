import logging
from datetime import date, datetime

from pyspark import Row
from pyspark.sql import SparkSession


def run_job():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    spark = SparkSession.builder.appName("simple-app").getOrCreate()
    df = spark.createDataFrame([
        Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
        Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
        Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
    ])
    logger.info("DataFrame created with %i rows" % df.count())
    df.show()

    spark.stop()


run_job()
