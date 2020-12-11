#!/bin/sh

# Get property from properties file

getProperty(){
  grep "^$2=" "$1" | cut -d'=' -f2
}

# Get current dir
DIR = "$(pwd)"

PROPERTIES_FILE = "$DIR/../properties/ingest.properties"

OOZIE_CLIENT = $(getProperty "$PROPERTIES_FILE" "oozie_client")
OOZIE="http://$OOZIE_OOZIE_CLIENT/oozie"
OOZIE_COORD_NAME = $(getProperty "$PROPERTIES_FILE" "oozie_coordinator_name")

START_DATE = $(getProperty "$PROPERTIES_FILE" "start_date")
END_DATE = $(getProperty "$PROPERTIES_FILE" "end_date")

## Kill previous coordinator
oozie jobs --oozie ${OOZIE} -jobtype coordinator -filter name=${OOZIE_COORD_NAME} -kill

## Run coordinator

oozie job --oozie ${OOZIE} -config ${PROPERTIES_FILE} -run start_date=$START_DATE