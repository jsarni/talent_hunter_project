#!/bin/sh

# Get property from properties file

getProperty(){
  grep "^$2=" "$1" | cut -d'=' -f2
}

# Get current dir
DIR="$(pwd)"

PROPERTIES_FILE="$DIR/../properties/ingest.properties"

OOZIE_CLIENT="d271ee89-3c06-4d40-b9d6-d3c1d65feb57.priv.instances.scw.cloud:11000"
OOZIE="http://${OOZIE_CLIENT}/oozie"
OOZIE_COORD_NAME="SPOTIFY_INGEST_COORD_TALENTHUNTER"

START_DATE="2020-12-04T06:00+0100"
END_DATE="2021-03-01T06:00+0100"

## Kill previous coordinator
oozie jobs --oozie ${OOZIE} -jobtype coordinator -filter name=${OOZIE_COORD_NAME} -kill

## Run coordinator

oozie job --oozie ${OOZIE} -config ${PROPERTIES_FILE} -run start_date=$START_DATE