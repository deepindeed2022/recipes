#! Makefile
all: result.tar.gz

result.tar.gz:
	./run && tar -zcvf result.tar.gz result || echo "compile error"

clean:
	rm -rf result
	rm -f result.tar.gz
	rm -rf src/*.pyc
	rm -rf src/*.log