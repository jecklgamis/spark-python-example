#!/usr/bin/env bash

if [ -z "$SPARK_HOME" ]; then
  echo "SPARK_HOME is not set. Please set it to your Spark installation directory."
  exit 1
fi

SPARK_CLUSTER_HOST=$(ipconfig getIfAddr en0)
echo "Using SPARK_CLUSTER_HOST = $SPARK_CLUSTER_HOST"

$SPARK_HOME/bin/spark-submit \
  --deploy-mode client \
  --master "spark://$SPARK_CLUSTER_HOST:7077" src/simple_app.py

