spark.conf.set(
    "fs.azure.account.key.carstoragge.dfs.core.windows.net",
    dbutils.secrets.get(scope="car_scope", key="car_storage_key")  
)

df = spark.read.csv(
  "abfss://row@carstoragge.dfs.core.windows.net/car_data.csv",
  header=True,
  inferSchema=True
)
df.show(5)

df_clean = df.dropna(subset=["Price ($)", "Annual Income", "Model"])
df_clean = df_clean.dropDuplicates()


from pyspark.sql.functions import lower, upper, trim

df_clean = df_clean.withColumn("Transmission", lower(trim(df_clean["Transmission"])))
df_clean = df_clean.withColumn("Company", upper(trim(df_clean["Company"])))



from pyspark.sql.functions import year, current_date

df_clean = df_clean.withColumn("CarAge", year(current_date()) - year(df_clean["Date"]))



from pyspark.sql.functions import avg

df_avg_price = df_clean.groupBy("Company").agg(avg("Price ($)").alias("AvgPrice"))
df_avg_price.show()


df_trans = df_clean.groupBy("Transmission").count()
df_trans.show()


df_top = df_clean.orderBy(df_clean["Price ($)"].desc()).limit(10)
df_top.select("Model", "Company", "Price ($)").show()


jdbc_url = "jdbc:sqlserver://carsqlserver.database.windows.net:1433;database=carsalesdb;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;"
db_user = dbutils.secrets.get(scope="car_scope", key="localhost@carsqlserver")
db_password = dbutils.secrets.get(scope="car_scope", key="********")

df_clean.write \
    .format("jdbc") \
    .mode("append") \
    .option("url", jdbc_url) \
    .option("dbtable", "CarSaless") \
    .option("user", db_user) \       
    .option("password", db_password) \ 
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .save()
