#!/bin/bash

# update before installs
sudo apt update

# MySQL installation
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password toor'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password toor'
sudo apt-get -y install mysql-server

# database creation and user addition
mysql -u root -ptoor << EOF
CREATE DATABASE ObjectDB
USE ObjectDB
CREATE TABLE images(id INT unsigned NOT NULL AUTO_INCREMENT, path VARCHAR(2048), exif TEXT, odapi_output TEXT, PRIMARY KEY (id));
CREATE USER 'machine'@'localhost'IDENTIFIED BY 'learning'
GRANT ALL PRIVILEGES ON *.* TO 'machine'@'localhost' WITH GRANT OPTION
EOF

# set up database folders
sudo mkdir /srv/ObjectDB
sudo gpasswd -a $USER mysql
sudo mkdir /srv/ObjectDB/EXIF
sudo mkdir /srv/ObjectDB/odapi_output
sudo mkdir /srv/ObjectDB/unprocessed
sudo mkdir /srv/ObjectDB/processed
sudo chown mysql:mysql -R /srv/ObjectDB/
sudo chmod ug+rw -R /srv/ObjectDB/

# get pip
sudo apt install python-pip -y

# set up python virtual environment
sudo pip install virtualenv
virtualenv .
source bin/activate

# install python dependencies
pip install tensorflow
pip install pillow
pip install lxml
pip install jupyter
pip install matplotlib
pip install ipython
pip install mysql-connector==2.1.4
pip install jsonpickle
pip install exifread

# get git
sudo apt install git -y

# clone tensorflow/models repository
git clone https://github.com/tensorflow/models.git
cd models

# get protobuf compiler
sudo apt install protobuf-compiler -y

# compile the protobuf libraries and add to python path
protoc object_detection/protos/*.proto --python_out=.
export PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/slim

# add __init__.py to models directory to allow imports in odapi_adapter.py from root directory
touch __init__.py

# run tests
python object_detection/builders/model_builder_test.py

# run object_detection_tutorial (commented out for only dependency setup)
#jupyter notebook object_detection/object_detection_tutorial.ipynb
