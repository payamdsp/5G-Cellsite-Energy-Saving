from pyspark.sql import SparkSession, functions as F

def main():
    spark = SparkSession.builder.appName("CellFeatureEngineering").getOrCreate()
    df = spark.read.json("s3://your-bucket/raw_data/")
    features = df.groupBy("cell_id").agg(
        F.avg("traffic_load").alias("avg_traffic"),
        F.max("user_count").alias("peak_users"),
        F.stddev("biometric_pattern").alias("bio_var"),
        F.first("MCC").alias("MCC"),
        F.first("MNC").alias("MNC"),
        F.first("gNodeB_id").alias("gNodeB_id")
    )
    features.write.parquet("s3://your-bucket/features/", mode="overwrite")
    spark.stop()
if __name__ == "__main__":
    main()