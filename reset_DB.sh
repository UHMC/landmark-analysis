#!/bin/bash
rm -rf /srv/ObjectDB/processed/*
rm -rf /srv/ObjectDB/unprocessed/*
rm -rf /srv/ObjectDB/EXIF/*
rm -rf /srv/ObjectDB/odapi_output/*
rm -rf /srv/ObjectDB/analysis/*
mysql -u machine -plearning << EOF
USE ObjectDB
TRUNCATE images;
TRUNCATE objects
EOF
