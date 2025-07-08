## Spark Python Example

This repo contains example Spark jobs in Python.

## Requirements

Python 3

Install Python dependencies

```bash
pip install -r requirements.txt
```

## Installing Spark

```bash
curl -LO https://dlcdn.apache.org/spark/spark-4.0.0/spark-4.0.0-bin-hadoop3-connect.tgz && tar xvf spark-4.0.0-bin-hadoop3-connect.tgz
```

Ensure SPARK_HOME env variable is pointing to the extracted directory. Run this in your
shell or set this in your `~/.bashrc` or `~/.zshrc`:

```
export SPARK_HOME=<path-to>/spark-4.0.0-bin-hadoop3-connect
export PATH="$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH"
```

## Submitting Job

##### Submitting Job Locally

```bash
$SPARK_HOME/bin/spark-submit --master "local[*]" src/simple_app.py
```

##### Submitting Job Using Spark Connect

First ensure the Spark Connect server is up and running

```bash
$SPARK_HOME/sbin/start-connect-server.sh
```

Verify if you can reach http://localhost:4040

Run the standalone app to submit the job:

```bash
python3 src/spark_connect_app.py
```

You should see something like so

```bash
+---+---+-------+----------+-------------------+
|  a|  b|      c|         d|                  e|
+---+---+-------+----------+-------------------+
|  1|2.0|string1|2000-01-01|2000-01-01 12:00:00|
|  2|3.0|string2|2000-02-01|2000-01-02 12:00:00|
|  4|5.0|string3|2000-03-01|2000-01-03 12:00:00|
+---+---+-------+----------+-------------------+
```

##### Submitting Job To A Standalone Cluster

Ensure the Spark standalone cluster is up and running. You need to start a master and at least one worker node.
We will just use the local machine as the master and worker node for this example.

Start the master:

```bash
$SPARK_HOME/sbin/start-master.sh
```

Verify you can reach the Spark master UI at http://localhost:8080. You can also find the URL of the master which you
will use in starting a worker.

Start a worker:

```bash
$SPARK_HOME/sbin/start-worker.sh <master-url>
```

Verify from the master UI that worker has joined. You should see the worker listed under the "Workers" section.

Submit the job to the cluster:

```bash
MASTER_URL="spark://$(ipconfig getIfAddr en0):7077"
$SPARK_HOME/bin/spark-submit --deploy-mode client --master $MASTER_URL src/simple_app.py
```

Note that cluster mode is not supported in Python ( at least at the time of this writing)

