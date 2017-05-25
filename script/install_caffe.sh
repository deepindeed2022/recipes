#!/bin/sh
# CAFFE INSTALLATION: http://caffe.berkeleyvision.org/installation.html
set -e

if [ "$1" == "prepare" ];then
  # Keep Ubuntu or Debian up to date
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get dist-upgrade
  sudo apt-get autoremove
  
  # DEPENDENCIES
  sudo apt-get -y install libopenblas-dev
  sudo apt-get -y install libboost-all-dev
  sudo apt-get -y install libprotobuf-dev protobuf-compiler
  sudo apt-get -y install libgoogle-glog-dev
  sudo apt-get -y install libgflags-dev
  sudo apt-get -y install libhdf5-dev
  
  # OPTIONAL DEPENDENCIES
  # Install OpenCV (http://milq.github.io/install-opencv-ubuntu-debian).
  sudo apt-get -y install liblmdb-dev
  sudo apt-get -y install libleveldb-dev
  sudo apt-get -y install libsnappy-dev
  
  # INTERFACES (Python 3)
  sudo apt-get install python3-dev python3-numpy libboost-python-dev
fi
HAVE_CONFIG=0
if [ ! -d "caffe" ];then
  	# CLONING AND COMPILING
  	git clone https://github.com/BVLC/caffe.git
	HAVE_CONFIG=1
fi
cd caffe
if [ $HAVE_CONFIG -eq 1 ];then
	cp Makefile.config.example Makefile.config
	# CPU_ONLY := 1
	# OPENCV_VERSION := 3
	# BLAS := open
	# BLAS_LIB := /usr/lib/openblas-base
	# MATLAB_DIR := /opt/MATLAB/R2015a
	
	# INSTALL OPENCV 3 with -DWITH_GDAL=OFF!!! Error OpenCV 3 with GDAL.
	
	# If have occur "hdf5.h" not found:
	# http://stackoverflow.com/questions/37007495/caffe-didnt-see-hdf5-h-when-compiling
	# add INCLUDE_DIR+= /usr/include/hdf5/serial
        # add LIBARAIES+=/usr/lib/x86_64-linux-gnu/hdf5/serial
	sudo vi Makefile.config
fi
# If occur error:
#
# src/caffe/test/test_hdf5data_layer.cpp:4:18: fatal error: hdf5.h: No such file or directory
# compilation terminated.
# Makefile:575: recipe for target '.build_release/src/caffe/test/test_hdf5data_layer.o' failed
# make: *** [.build_release/src/caffe/test/test_hdf5data_layer.o] Error 1
# make: *** Waiting for unfinished jobs....
# More issues:  https://github.com/BVLC/caffe/issues/3530

# cp Makefile.config.example Makefile.config
# Adjust Makefile.config (for example, if using Anaconda Python)
make all -j8
make test -j8
make runtest
#
# make all matcaffe
# make mattest
