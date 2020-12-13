import org.apache.spark.sql.SparkSession



object Main {


  def main(args: Array[String]): Unit = {
    val appName : String =  "INGEST_SPOTIFY"

    implicit val sparkSession: SparkSession =
      SparkSession.builder()
        .appName(appName)
        .config("spark.es.nodes","51.15.248.86")
        .config("spark.spark.es.port","9200")
      	.config("spark.es.index.auto.create" , "true")
      	.config("spark.es.index.read.missing.as.empty" , "true")
      	.config("spark.es.nodes.wan.only" , "true")
        .enableHiveSupport()
        .getOrCreate()


    val collectDate : String = java.time.LocalDate.now.toString
    NewReleasesIngestor(sparkSession).ingest(collectDate)

    sparkSession.stop()
  }
}
