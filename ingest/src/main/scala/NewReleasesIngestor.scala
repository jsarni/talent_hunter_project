import NewReleasesIngestor.{NEW_RELEASE_FILE, SPOTIFY_PLAYLIST_FILE, SPOTIFY_ROOT_FILE, TOP_DAILY_HITS}
import org.apache.spark.sql.SparkSession
import org.elasticsearch.spark.sql.sparkDatasetFunctions
import org.apache.spark.sql.types.{DateType, IntegerType}




class NewReleasesIngestor(spark: SparkSession) {
  import spark.implicits._
  def ingest(collectDate : String): Unit = {
    val newRelease = spark.read.option("header",true).csv(s"$SPOTIFY_ROOT_FILE/$collectDate/$NEW_RELEASE_FILE")
    val spotifyPlaylist = spark.read.option("header",true).csv(s"$SPOTIFY_ROOT_FILE/$collectDate/$SPOTIFY_PLAYLIST_FILE")
    val topHit =  spark.read.option("header",true).csv(s"$SPOTIFY_ROOT_FILE/$collectDate/$TOP_DAILY_HITS")

    newRelease.write.mode("overwrite").saveAsTable("talent_hunter.spotify_new_releases_tmp")
    spotifyPlaylist.write.mode("overwrite").saveAsTable("talent_hunter.spotify_playlists_tmp")
    topHit.write.mode("overwrite").saveAsTable("talent_hunter.top_daily_hits_tmp")


    val playlists = spotifyPlaylist.withColumn("playlist_tracks_count",'playlist_tracks_count.cast(IntegerType))
                                  .withColumn("collect_date", 'collect_date.cast(DateType))

    val newreleases = newRelease.withColumn("release_date", 'release_date.cast(DateType))
                           .withColumn("release_total_tracks",'release_total_tracks.cast(IntegerType))
                           .withColumn("collect_date", 'collect_date.cast(DateType))

    val topHits =topHit.withColumn("track_added_date",'track_added_date.cast(DateType))
      .withColumn("track_album_date",'track_album_date.cast(DateType))
      .withColumn("collect_date",'collect_date.cast(DateType))
      .withColumn("track_album_total_track",'track_album_total_track.cast(IntegerType))
      .withColumn("track_disc_number",'track_disc_number.cast(IntegerType))
      .withColumn("track_duration",'track_duration.cast(IntegerType))
      .withColumn("track_popularity",'track_popularity.cast(IntegerType))
      .withColumn("track_number",'track_number.cast(IntegerType))
      .withColumn("track_artist_nbr_follow",'track_artist_nbr_follow.cast(IntegerType))
      .withColumn("track_artist_popularity",'track_artist_popularity.cast(IntegerType))

    playlists.saveToEs("playlistsbis")
    newreleases.saveToEs("newreleasesbis")
    topHits.saveToEs("topdailyhits")


  }

}

object NewReleasesIngestor {
  def apply(spark: SparkSession): NewReleasesIngestor = new NewReleasesIngestor(spark)

  val NEW_RELEASE_FILE =  "new_release.csv"
  val SPOTIFY_PLAYLIST_FILE  = "spotify_playlist.csv"
  val TOP_DAILY_HITS  = "top_daily_hits.csv"
  val SPOTIFY_ROOT_FILE = "hdfs:///user/talenthunter/lake/spotify"
}
