#!/usr/bin/env bash

if [ -z "$SPARK_HOME" ]; then
  echo "SPARK_HOME is not set. Please set it to your Spark installation directory."
  exit 1
fi

SERVER=$(ipconfig getIfAddr en0)

$SPARK_HOME/bin/spark-submit \
  --deploy-mode client \
  --master "local[*]" src/simple_app.py

