#!/bin/bash
rm -rf /srv/ObjectDB/processed/*
rm -rf /srv/ObjectDB/unprocessed/*
rm -rf /srv/ObjectDB/EXIF/*
mysql -u machine -plearning << EOF
USE ObjectDB
TRUNCATE image
EOF
