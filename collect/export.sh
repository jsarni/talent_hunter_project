#!/bin/sh

CURRENT_DATE=$(date '+%Y-%m-%d')
CURRENT_FOLDER="/user/talenthunter/lake/spotify/${CURRENT_DATE}"
SRC_FOLDER="/home/talenthunter/spotify"

hdfs dfs -mkdir ${CURRENT_FOLDER}

hdfs dfs -copyFromLocal -f ${SRC_FOLDER}/new_release.csv ${CURRENT_FOLDER}/new_release.csv
hdfs dfs -copyFromLocal -f ${SRC_FOLDER}/spotify_playlist.csv ${CURRENT_FOLDER}/spotify_playlist.csv
hdfs dfs -copyFromLocal -f ${SRC_FOLDER}/top_daily_hits.csv ${CURRENT_FOLDER}/top_daily_hits.csv

