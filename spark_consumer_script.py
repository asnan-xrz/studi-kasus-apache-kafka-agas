from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Inisialisasi Spark
spark = SparkSession.builder \
    .appName("SensorSuhuConsumer") \
    .getOrCreate()

# Membaca data dari Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor-suhu") \
    .load()

# Mengambil nilai dari payload dan mengkonversi ke format yang bisa dibaca
suhu_df = df.selectExpr("CAST(value AS STRING)")

# Menguraikan JSON
suhu_df = suhu_df.selectExpr("json_tuple(value, 'sensor_id', 'suhu') AS (sensor_id, suhu)") \
    .withColumn("suhu", col("suhu").cast("int"))

# Filter suhu di atas 80°C
suhu_warning_df = suhu_df.filter(col("suhu") > 80)

# Tampilkan hasil
query = suhu_warning_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
