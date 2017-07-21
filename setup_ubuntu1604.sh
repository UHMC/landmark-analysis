#!/bin/bash
# update before installs
sudo apt update
# get pip
sudo apt install python-pip -y
# set up python virtual environment
pip install virtualenv
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
# run tests
python object_detection/builders/model_builder_test.py
# run object_detection_tutorial (commented out for only dependency setup)
#jupyter notebook object_detection/object_detection_tutorial.ipynb
