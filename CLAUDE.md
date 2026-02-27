# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Example Apache Spark 4.0 jobs written in Python (PySpark). Two execution modes: local spark-submit and Spark Connect (client-server).

## Prerequisites

- Python 3
- Apache Spark 4.0.0 installed with `SPARK_HOME` and `PATH` configured

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally via spark-submit
$SPARK_HOME/bin/spark-submit --master "local[*]" src/simple_app.py

# Run via Spark Connect (requires running Connect server)
$SPARK_HOME/sbin/start-connect-server.sh   # start server first
python3 src/spark_connect_app.py
```

## Architecture

- `src/simple_app.py` — Standalone Spark job submitted via `spark-submit`. Reads `$SPARK_HOME/README.md` and counts lines containing 'a' and 'b'.
- `src/spark_connect_app.py` — Connects to a Spark Connect server on `sc://localhost:15002`. Creates a sample DataFrame and displays it.
- `submit-to-local-spark.sh` / `submit-using-spark-connect.sh` — Shell wrappers for the two execution modes.
