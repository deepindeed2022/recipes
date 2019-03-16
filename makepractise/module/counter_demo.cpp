#include <iostream>
#include <stdint.h>
#include <boost/noncopyable.hpp>
#include <boost/shared_ptr.hpp>

class Counter: public boost::noncopyable {
public:
	Counter():value_(0){}
	int64_t value() const{return this->value_;}
	int64_t getAnIncrease(){return ++(this->value_);}
private:
	int64_t value_;
	// mutable MutexLock mutex_;
};
int main(int argc, char* argv[]) {
	boost::shared_ptr<Counter> counter = boost::shared_ptr<Counter>(new Counter());
	for(size_t i = 0; i < 100; ++i) {
		std::cout << counter->getAnIncrease() << std::endl;	
	}
	Counter counter2;
	// The following code couldn't compile
	// Counter counter3(counter2);
	
	return 0;
}
