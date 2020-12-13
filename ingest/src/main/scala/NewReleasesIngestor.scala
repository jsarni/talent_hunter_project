import NewReleasesIngestor.{NEW_RELEASE_FILE, SPOTIFY_PLAYLIST_FILE, SPOTIFY_ROOT_FILE}
import org.apache.spark.sql.SparkSession
import org.elasticsearch.spark._
import org.elasticsearch.spark.sql.sparkDatasetFunctions




class NewReleasesIngestor(spark: SparkSession) {

  def ingest(collectDate : String): Unit = {
    val newRelease = spark.read.option("header",true).csv(s"$SPOTIFY_ROOT_FILE/$collectDate/$NEW_RELEASE_FILE")
    val spotifyPlaylist = spark.read.option("header",true).csv(s"$SPOTIFY_ROOT_FILE/$collectDate/$SPOTIFY_PLAYLIST_FILE")

    newRelease.write.mode("overwrite").saveAsTable("talent_hunter.spotify_new_releases_tmp")
    spotifyPlaylist.write.mode("overwrite").saveAsTable("talent_hunter.spotify_playlists_tmp")

    spark.sql("INSERT INTO talent_hunter.spotify_new_releases  SELECT * FROM talent_hunter.spotify_new_releases_tmp")
    spark.sql("INSERT INTO talent_hunter.spotify_playlists  SELECT * FROM talent_hunter.spotify_playlists_tmp")


    //newRelease.saveToEs("spotify/newreleases")

  }
}

object NewReleasesIngestor {
  def apply(spark: SparkSession): NewReleasesIngestor = new NewReleasesIngestor(spark)

  val NEW_RELEASE_FILE =  "new_release.csv"
  val SPOTIFY_PLAYLIST_FILE  = "spotify_playlist.csv"
  val SPOTIFY_ROOT_FILE = "hdfs:///user/talenthunter/lake/spotify"
}
