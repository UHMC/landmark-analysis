# object-analysis
#### Introduction
This project’s aim is to conceptualize and implement an open-source, simple, and extensible framework for continuous image analysis using the [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/object_detection).
#### System Requirements
* [Ubuntu Linux ver. 16.04](https://www.ubuntu.com/download/desktop)
#### Dependencies
The setup script should take care of any dependencies automatically; however, it should be noted that these packages will be installed on your system if all goes well:
* `mysql-server`
* `git` (if not installed already)
* `protobuf-compiler`
* `python-pip`
  * `tensorflow`
  * `pillow`
  * `lxml`
  * `jupyter`
  * `matplotlib`
  * `ipython`
  * `mysql-connector=2.1.4`
  * `jsonpickle`
  * `exifread`
#### File hierarchy
The setup script will create a folder structure used by the database and the ongoing processesing scripts.
* /srv/ObjectDB
  * /EXIF
  * /odapi_output
  * /unprocessed
  * /processed

All folders will be owned by the mysql usergroup and the current user will be added to the `mysql` group.
#### Visual diagram
![Project Schema](/Resources/diagram.png?raw=true)
#### Screenshots
![What's the difference](/Resources/screenshot1.png)
#### Credits
* [Google's TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/object_detection)
  * "Speed/accuracy trade-offs for modern convolutional object detectors."
Huang J, Rathod V, Sun C, Zhu M, Korattikara A, Fathi A, Fischer I, Wojna Z,
Song Y, Guadarrama S, Murphy K, CVPR 2017
* [Mario Canul](mailto:mcanul@hawaii.edu) - Undergraduate Cybersecurity Researcher
* [Saxon Knight](mailto:knight7@hawaii.edu) - Undergraduate Cybersecurity Researcher
