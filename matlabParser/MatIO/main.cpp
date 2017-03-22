
#ifdef _MSC_VER
#include <stdio.h>
#include <tchar.h>
#endif

#include <iostream>

#include "MatlabIO.h"

int main(int argc, char** argv)
{
    std::string filename;
    if (argc > 1)
    {
        filename = argv[1];
    }
    else
    {
		std::cout << "##### PLEASE INPUT A MATLAB FILE FULL PATH ####" << std::endl;
		std::cin >> filename;
        filename = "D://Document//Repo//matlabParser//ceshithree.mat";
    }

    Matlab::File file(filename);

	std::cout << "METADATA:\n\n";
	std::cout << file.description() << std::endl << std::endl;

	std::cout << "============\n\nMATRICIES:\n\n";
	for (Matlab::Matrix* matrix : file.matricies())
	{
		std::cout << "Name: " << matrix->name->to_string() << std::endl;
		std::cout << "--Dimensions: " << matrix->dimensions->to_string() << std::endl;

		int j = 0;

		for (auto child : matrix->nodes())
			std::cout << "--Child " << j++ << ": " << child->to_string(true) << std::endl;
	
		std::cout << std::endl;
	}
		
	std::cout << "============\n";

	std::cin.get();
	system("PAUSE");
	return EXIT_SUCCESS;
}
