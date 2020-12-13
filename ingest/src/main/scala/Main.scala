import org.apache.spark
import org.apache.spark.sql.SparkSession
import org.elasticsearch.spark._
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._








object Main {


  def main(args: Array[String]): Unit = {
    val appName : String =  "INGEST_SPOTIFY"

    implicit val sparkSession: SparkSession =
      SparkSession.builder()
        .appName(appName)
        .enableHiveSupport()
        .getOrCreate()

    val conf = new SparkConf().setAppName(appName).setMaster("yarn")
    conf.set("es.index.auto.create", "true")
   // val sc = new SparkContext(conf)



    val collectDate : String = java.time.LocalDate.now.toString
    NewReleasesIngestor(sparkSession).ingest(collectDate)

    sparkSession.stop()
  }
}
