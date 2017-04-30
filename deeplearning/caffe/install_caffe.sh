#!/bin/sh
sudo apt-get install -y libopenblas-dev
sudo apt-get install -y libboost-all-dev
sudo apt-get install -y libprotobuf-dev protobuf-compiler
sudo apt-get install -y libgoogle-glog-dev
sudo apt-get install -y libgflags-dev
sudo apt-get install -y libhdf5-dev

# OPTIONAL DEPENDENCIES
# Install OpenCV (http://milq.github.io/install-opencv-ubuntu-debian).
sudo apt-get install -y liblmdb-dev
sudo apt-get install -y libleveldb-dev
sudo apt-get install -y libsnappy-dev

# INTERFACES (Python 3)
sudo apt-get install -y python3-dev python3-numpy libboost-python-dev
source install_opencv.sh
# CLONING AND COMPILING
git clone https://github.com/BVLC/caffe.git
cd caffe

# cp Makefile.config.example Makefile.config
# Adjust Makefile.config (for example, if using Anaconda Python)
# make all -j8
# make test -j8
# make runtest
#
# make all matcaffe
# make mattest
# 
# PERSONAL NOTES AND PERSONAL CONFIGURATION
# CPU_ONLY := 1
# OPENCV_VERSION := 3
# BLAS := open
# BLAS_LIB := /usr/lib/openblas-base
# MATLAB_DIR := /opt/MATLAB/R2015a

# INSTALL OPENCV 3 with -DWITH_GDAL=OFF!!! Error OpenCV 3 with GDAL.

# If have occur "hdf5.h" not found:
# http://stackoverflow.com/questions/37007495/caffe-didnt-see-hdf5-h-when-compiling
