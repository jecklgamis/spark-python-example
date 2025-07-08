import logging
import os

from pyspark.sql import SparkSession


def run_job():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    spark_home = os.getenv("SPARK_HOME")
    if not spark_home:
        logger.info("SPARK_HOME not set")
        exit(1)

    log_file = spark_home + "/README.md"
    spark = SparkSession.builder.appName("simple-app").getOrCreate()
    log_data = spark.read.text(log_file).cache()

    num_a = log_data.filter(log_data.value.contains('a')).count()
    num_b = log_data.filter(log_data.value.contains('b')).count()

    logger.info("Lines with a: %i, lines with b: %i" % (num_a, num_b))
    spark.stop()


run_job()
