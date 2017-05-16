#! Makefile

PROJECT := protobuftest

BUILD_DIR := $(pwd)
INCLUDE_DIR := /usr/local/include/ 
LIBRARIES := /usr/local/lib/
CXXFLAGS := -lprotobuf -pthread # `pkg-config --cflags --libs protobuf`
UNAME := $(shell uname -s)

ifeq ($(UNAME),Linux)
	LINUX :=1	
endif

ifeq ($(LINUX),1)
	CXX ?= /usr/bin/g++
	GCCVERSION := $(shell $(CXX) -dumpversion | cut -f1,2 -d.)
endif

SOURCES := main.cpp \
			

PROTO_SRC := $(wildcard *.proto)
PROTO_SRC := $(addprefix $(PROJECT_DIR),$(PROTO_SRC))
PROTO_GEN_HEADER := $(patsubst %.proto, %.pb.h,$(PROTO_SRC))
PROTO_GEN_CC := $(patsubst %.proto, %.pb.cc,$(PROTO_SRC))

OBJECTS := $(patsubst %.cpp, %.o, $(SOURCES))
OBJECTS += 

# $(info $(PROTO_GEN_CC))
# $(info $(PROTO_GEN_HEADER))

all: $(OBJECTS)

$(OBJECTS): main.cpp $(PROTO_GEN_CC)
	$(CXX) $< $(PROTO_GEN_CC) -I $(INCLUDE_DIR) -L $(LIBRARIES) $(CXXFLAGS) -o $@

#%.pb.o: $(PROTO_GEN_CC) $(PROTO_GEN_HEADER)
#	@ echo CXX $<
#	$(CXX) $< $(CXXFLAGS) -c -o $@ 2> $@.$(WARNS_EXT) \
#               || (cat $@.$(WARNS_EXT); exit 1)
#

$(PROTO_GEN_CC) $(PROTO_GEN_HEADER): $(PROTO_SRC)
	echo PROTOC $<
	echo "Generating protobuf headers and cc files"
	protoc --cpp_out=. $<

clean:
	rm -f *.o
	rm -f *.pb.h *.pb.cc
