CREATE EXTERNAL TABLE talent_hunter.spotify_new_releases (
    release_id      STRING,
    release_name    STRING,
    release_date    STRING,
    release_total_tracks BIGINT,
    release_type STRING,
    release_external_url STRING, 
    release_available_market STRING,
    album_type STRING,
    artist_id STRING,
    collect_date STRING)
STORED BY 'org.elasticsearch.hadoop.hive.EsStorageHandler'
TBLPROPERTIES('es.resource' = 'spotify/newrelease',
'es.index.read.missing.as.empty' = 'true',
'es.nodes' = '51.15.248.86:9200/',
'es.nodes.wan.only' = 'false'); 



CREATE EXTERNAL TABLE talent_hunter.spotify_playlists (
    playlist_id STRING,
    playlist_name STRING,
    playlist_type STRING,
    playlist_collaborative      STRING,
    playlist_description    STRING,
    playlist_public STRING,
    playlist_snapshot_id STRING,
    playlist_tracks_count BIGINT,
    playlist_tracks_url STRING,
    playlist_external_urls    STRING,
    collect_date STRING)
STORED BY 'org.elasticsearch.hadoop.hive.EsStorageHandler'
TBLPROPERTIES('es.resource' = 'spotify/playlists',
'es.index.read.missing.as.empty' = 'true',
'es.nodes' = '51.15.248.86:9200/',
'es.nodes.wan.only' = 'false');

--	ADD JAR hdfs:///user/talenthunter/lake/elasticsearch/elasticsearch-hadoop-7.10.1.jar;

--list jars;