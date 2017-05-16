#! Makefile
BOOST_ROOT := /usr/include/boost
BUILD_DIR := $(pwd)
CXXFLAGS := -lglog -lboost_system # `pkg-config --cflags --libs protobuf`
UNAME := $(shell uname -s)

INCLUDE_DIR := $(BOOST_ROOT)/

ifeq ($(UNAME),Linux)
	LINUX := 1	
endif

ifeq ($(LINUX),1)
	CXX ?= /usr/bin/g++
	GCCVERSION := $(shell $(CXX) -dumpversion | cut -f1,2 -d.)
endif
SOURCES := counter_demo.cpp
#OBJECTS := $(patsubst %.cpp, %.o, $(SOURCES))
# $(info $())

all: boost_test 

boost_test: $(SOURCES)
	$(CXX) -o boost_test $(SOURCES)  -I $(INCLUDE_DIR) -L$(LIBRARY_DIR) $(CXXFLAGS)

clean:
	rm -f *.o
	rm -f boost_test
