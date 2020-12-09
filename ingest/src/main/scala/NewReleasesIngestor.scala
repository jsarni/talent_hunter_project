class NewReleasesIngestor(spark: SparkSession) {

  def ingest(): Unit = {
    spark.read.csv()
  }
}

object NewReleasesIngestor {
  def apply(spark: SparkSession): NewReleasesIngestor = new NewReleasesIngestor(spark)

  val NEW_RELEASES8LAKE_FILE = ""
}
