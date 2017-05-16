#! Makefile
CAFFE_ROOT := /home/iscas/IR/caffe

BUILD_DIR := $(pwd)
CXXFLAGS := -lcaffe -lglog -lboost_system -lprotobuf # `pkg-config --cflags --libs protobuf`
UNAME := $(shell uname -s)

INCLUDE_DIR := $(CAFFE_ROOT)/include -I $(CAFFE_ROOT)/build/src/
LIBRARY_DIR := $(CAFFE_ROOT)/build/lib

CPU_ONLY := 1

ifeq ($(UNAME),Linux)
	LINUX := 1	
endif

ifeq ($(LINUX),1)
	CXX ?= /usr/bin/g++
	GCCVERSION := $(shell $(CXX) -dumpversion | cut -f1,2 -d.)
endif
ifeq ($(CPU_ONLY), 1)
	DEFINE_ := CPU_ONLY
endif
ifneq ($(CPU_ONLY), 1)
	DEFINE_ := GPU
endif
SOURCES := net_demo.cpp
			

#OBJECTS := $(patsubst %.cpp, %.o, $(SOURCES))
#OBJECTS += 

# $(info $())
# $(info $())

all: netapp

netapp: $(SOURCES)
	$(CXX) -o netapp $(SOURCES)  -I$(INCLUDE_DIR) -D$(DEFINE_) -L$(LIBRARY_DIR) $(CXXFLAGS)

clean:
	rm -f *.o
	rm -f netapp
