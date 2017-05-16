#include <iostream>
#include <vector>
#include <caffe/net.hpp>
using namespace std;
using namespace caffe;
int main(int argc, char const *argv[])
{
    std::string proto("deploy.prototxt");
    Net<float> nn(proto, caffe::TEST);
    vector<string> bn = nn.blob_names();
    for( int i =0; i< bn.size(); ++i)
    {
        std::cout <<"Blob #" <<i << " : " << bn[i] << std::endl;
    }
    std::cout << "###### Layer name #####" <<std::endl;
    vector<string> ln = nn.layer_names();
    for (int i = 0; i < ln.size(); ++i)
    {
        std::cout << "Layer #" <<i << " : " << ln[i] << std::endl;
    }
    return 0;
}
