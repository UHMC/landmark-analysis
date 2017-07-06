#!/bin/bash
sudo apt install python-pip
pip install virtualenv
virtualenv .
source bin/activate
pip install tensorflow
pip install pillow
pip install lxml
pip install jupyter
pip install matplotlib
pip install ipython
cd models
sudo apt-get install protobuf-compiler
protoc object_detection/protos/*.proto --python_out=.
export PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/slim
python object_detection/builders/model_builder_test.py
jupyter notebook object_detection/object_detection_tutorial.ipynb
