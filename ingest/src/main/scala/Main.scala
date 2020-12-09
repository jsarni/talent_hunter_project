

object Main {

  def main(args: Array[String]): Unit = {
    implicit val sparkSession: SparkSession =
      SparkSession.builder()
        .appName("INGEST_SPOTIFY")
        .master("d271ee89-3c06-4d40-b9d6-d3c1d65feb57.priv.instances.scw.cloud")
        .getOrCreate()

    NewReleasesIngestor(sparkSession).ingest()

    sparkSession.stop()
  }
}
