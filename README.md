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

 #### File Hierarchy
The setup script will create the following folder structure used by the database and the ongoing processing scripts:
 * /srv/ObjectDB
   * /EXIF
   * /odapi_output
   * /unprocessed
   * /processed

  All folders are owned by the mysql usergroup, and the current user at setup time will be added to the `mysql` group.

#### Demo Instructions
 1. Install Git if necessary:  
    `$ sudo apt install git -y`
 2. Clone the repository:  
    `$ git clone https://github.com/UHMC/object-analysis.git`
 3. Change directory into the project folder:  
    `$ cd object-analysis`
 4. Run the setup script:  
    `$ ./setup_ubuntu1604.sh`
 5. Add demo images to unprocessed folder:  
    `$ cp Resources/demo-images/* /srv/ObjectDB/unprocessed/`
 6. Wait.

#### Visual Diagram
![Project Schema](/Resources/diagram.png?raw=true)
#### Screenshots
![Screenshot](/Resources/screenshot2.png)
![Output](/Resources/screenshot3.png)
#### Credits
* [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/object_detection)
  * "Speed/accuracy trade-offs for modern convolutional object detectors."
Huang J, Rathod V, Sun C, Zhu M, Korattikara A, Fathi A, Fischer I, Wojna Z,
Song Y, Guadarrama S, Murphy K, CVPR 2017
* [Mario Canul](mailto:mcanul@hawaii.edu) - Undergraduate Cybersecurity Researcher
* [Saxon Knight](mailto:knight7@hawaii.edu) - Undergraduate Cybersecurity Researcher
