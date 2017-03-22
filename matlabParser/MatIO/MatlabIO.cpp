
#ifdef _MSC_VER
#include <stdio.h>
#include <tchar.h>
#else
#include <string>
#include <exception>
#endif

#include "MatlabIO.h"
#include "tinyfl.h"

using namespace Matlab;

////////////////////////////////////
//             _root              //
////////////////////////////////////
__internal::_root::_root(char* start, int len)
{
	char* cur_point = start;

	char* data_loc;
	std::uint32_t data_type_id;
	std::uint32_t data_len;

	while (cur_point < start + len)
	{
		if (*(cur_point + 2) == 0 && *(cur_point + 3) == 0)
		{
			// regular data format
			data_loc = cur_point + 8;
			data_len = *(reinterpret_cast<std::uint32_t*>(cur_point + 4));
			data_type_id = *(reinterpret_cast<std::uint32_t*>(cur_point));
		}
		else
		{
			// compressed data format
			data_loc = cur_point + 4;
			std::int16_t len_t = *(reinterpret_cast<std::uint16_t*>(cur_point + 2));
			std::int16_t typeid_t = *(reinterpret_cast<std::uint16_t*>(cur_point));
			data_len = len_t;
			data_type_id = typeid_t;
		}

		switch (data_type_id)
		{
		case DataTypes::miCOMPRESSED::MFT:
			children.push_back(new DataTypes::miCOMPRESSED(data_loc, data_len));
			break;
		case DataTypes::miDOUBLE::MFT:
			children.push_back(new DataTypes::miDOUBLE(data_loc, data_len));
			break;
		case DataTypes::miINT16::MFT:
			children.push_back(new DataTypes::miINT16(data_loc, data_len));
			break;
		case DataTypes::miINT32::MFT:
			children.push_back(new DataTypes::miINT32(data_loc, data_len));
			break;
		case DataTypes::miINT64::MFT:
			children.push_back(new DataTypes::miINT64(data_loc, data_len));
			break;
		case DataTypes::miINT8::MFT:
			children.push_back(new DataTypes::miINT8(data_loc, data_len));
			break;
		case DataTypes::miSINGLE::MFT:
			children.push_back(new DataTypes::miSINGLE(data_loc, data_len));
			break;
		case DataTypes::miUINT16::MFT:
			children.push_back(new DataTypes::miUINT16(data_loc, data_len));
			break;
		case DataTypes::miUINT32::MFT:
			children.push_back(new DataTypes::miUINT32(data_loc, data_len));
			break;
		case DataTypes::miUINT64::MFT:
			children.push_back(new DataTypes::miUINT64(data_loc, data_len));
			break;
		case DataTypes::miUINT8::MFT:
			children.push_back(new DataTypes::miUINT8(data_loc, data_len));
			break;
		case DataTypes::miUTF16::MFT:
			children.push_back(new DataTypes::miUTF16(data_loc, data_len));
			break;
		case DataTypes::miUTF32::MFT:
			children.push_back(new DataTypes::miUTF32(data_loc, data_len));
			break;
		case DataTypes::miUTF8::MFT:
			children.push_back(new DataTypes::miUTF8(data_loc, data_len));
			break;
		case DataTypes::miMATRIX::MFT:
			children.push_back(new DataTypes::miMATRIX(data_loc, data_len));
			break;
		default:
			std::cout << "UNSUPPORTED DATA TYPE IN MATLAB FILE: " << data_type_id << std::endl;
			break;
		}

		cur_point = data_loc + data_len;
	}
}

const std::int32_t __internal::_root::mft() const
{
	return 0x00;
}

std::ostream& __internal::_root::operator>>(std::ostream& src)
{
	// todo...
	return src;
}

////////////////////////////////////
//       _compressed_type         //
////////////////////////////////////
__internal::_compressed_type::_compressed_type(char* start, int len)
{
	compressed_data = start;
	compressed_data_len = len;

	void* uncomp = tinfl_decompress_mem_to_heap((void*)compressed_data,
		compressed_data_len,
		&uncompressed_data_len,
		TINFL_FLAG_PARSE_ZLIB_HEADER);

	if (uncomp == 0)
		throw Exception("unable to deflate compressed variable in matlab file");

	uncompressed_data = reinterpret_cast<char*>(uncomp);

	// todo:
	// call to deflate()

	_root* ch = new _root(uncompressed_data, uncompressed_data_len);
	children.push_back(ch);
}

__internal::_compressed_type::~_compressed_type()
{
	delete[] uncompressed_data;
}

std::ostream& __internal::_compressed_type::operator>>(std::ostream& src)
{
	// todo...
	return src;
}

const std::int32_t __internal::_compressed_type::mft() const
{
	return 0x0F;
}

////////////////////////////////////
//         _matlab_array          //
////////////////////////////////////
__internal::_matlab_array::_matlab_array(char* start, int len)
{
	char* ptr = start;
	ptr = read_single_primitive(ptr, &flags);
	ptr = read_single_primitive(ptr, &dimensions);
	ptr = read_single_primitive(ptr, &name);

	std::uint8_t flag_type = *(reinterpret_cast<std::uint8_t*>(flags->get() + 3));

	char* data_loc;
	std::uint32_t data_type_id;
	std::uint32_t data_len;

	while (ptr < start + len)
	{
		if (*(ptr + 2) == 0 && *(ptr + 3) == 0)
		{
			// regular data format
			data_loc = ptr + 8;
			data_len = *(reinterpret_cast<std::uint32_t*>(ptr + 4));
			data_type_id = *(reinterpret_cast<std::uint32_t*>(ptr));
		}
		else
		{
			// compressed data format
			data_loc = ptr + 4;
			std::int16_t len_t = *(reinterpret_cast<std::uint16_t*>(ptr + 2));
			std::int16_t typeid_t = *(reinterpret_cast<std::uint16_t*>(ptr));
			data_len = len_t;
			data_type_id = typeid_t;
		}

		switch (data_type_id)
		{
		case DataTypes::miCOMPRESSED::MFT:
			children.push_back(new DataTypes::miCOMPRESSED(data_loc, data_len));
			break;
		case DataTypes::miDOUBLE::MFT:
			children.push_back(new DataTypes::miDOUBLE(data_loc, data_len));
			break;
		case DataTypes::miINT16::MFT:
			children.push_back(new DataTypes::miINT16(data_loc, data_len));
			break;
		case DataTypes::miINT32::MFT:
			children.push_back(new DataTypes::miINT32(data_loc, data_len));
			break;
		case DataTypes::miINT64::MFT:
			children.push_back(new DataTypes::miINT64(data_loc, data_len));
			break;
		case DataTypes::miINT8::MFT:
			children.push_back(new DataTypes::miINT8(data_loc, data_len));
			break;
		case DataTypes::miSINGLE::MFT:
			children.push_back(new DataTypes::miSINGLE(data_loc, data_len));
			break;
		case DataTypes::miUINT16::MFT:
			children.push_back(new DataTypes::miUINT16(data_loc, data_len));
			break;
		case DataTypes::miUINT32::MFT:
			children.push_back(new DataTypes::miUINT32(data_loc, data_len));
			break;
		case DataTypes::miUINT64::MFT:
			children.push_back(new DataTypes::miUINT64(data_loc, data_len));
			break;
		case DataTypes::miUINT8::MFT:
			children.push_back(new DataTypes::miUINT8(data_loc, data_len));
			break;
		case DataTypes::miUTF16::MFT:
			children.push_back(new DataTypes::miUTF16(data_loc, data_len));
			break;
		case DataTypes::miUTF32::MFT:
			children.push_back(new DataTypes::miUTF32(data_loc, data_len));
			break;
		case DataTypes::miUTF8::MFT:
			children.push_back(new DataTypes::miUTF8(data_loc, data_len));
			break;
		case DataTypes::miMATRIX::MFT:
			children.push_back(new DataTypes::miMATRIX(data_loc, data_len));
			break;
		case 0x0:
			break;
		default:
			// std::cout << "WARNING: Unsupported data type in Matlab File (ignoring): " << data_type_id << std::endl;
			break;
		}

		ptr = data_loc + data_len;
	}

	
}

template<class T>
char* __internal::_matlab_array::read_single_primitive(char* src, T** dest)
{
	char* data_loc;
	std::uint32_t data_type_id;
	std::uint32_t data_len;
	if (*(src + 2) == 0 && *(src + 3) == 0)
	{
		// regular data format
		data_loc = src + 8;
		data_len = *(reinterpret_cast<std::uint32_t*>(src + 4));
		data_type_id = *(reinterpret_cast<std::uint32_t*>(src));
	}
	else
	{
		// compressed data format
		data_loc = src + 4;
		std::int16_t len_t = *(reinterpret_cast<std::uint16_t*>(src));
		std::int16_t typeid_t = *(reinterpret_cast<std::uint16_t*>(src + 2));
		data_len = len_t;
		data_type_id = typeid_t;
	}
	*dest = new T(data_loc, data_len);

	std::size_t padding_bts = 0;
	if ((data_loc + data_len - src) % 8 != 0)
		padding_bts = 8 - ((data_loc + data_len - src) % 8);

	return data_loc + data_len + padding_bts;
}

__internal::_matlab_array::~_matlab_array()
{
	delete flags;
    delete dimensions;
    delete name;
}

const std::int32_t __internal::_matlab_array::mft() const
{
	return 0x0E;
}

std::ostream& __internal::_matlab_array::operator>>(std::ostream& src)
{
	// todo...
	return src;
}

////////////////////////////////////
//             _file              //
////////////////////////////////////
__internal::_file::_file(std::string file_name)
{
	std::ifstream file(file_name, std::ifstream::binary);

	file.seekg(0, file.end);
	std::streamoff length = file.tellg();

	file.seekg(0, file.beg);

	_tot_len = static_cast<std::size_t>(length);

	_data = new char[_tot_len];
	file.read(_data, _tot_len);

	std::stringstream header_stream;
	for (int i = 0; i < 116; ++i)
		header_stream << _data[i];
	_desc = header_stream.str();

	// trim padding at the end
	_desc = _desc.erase(_desc.find_last_not_of(' ') + 1);

	_subs_offset = _data + 116;
	_flag_version = _subs_offset + 8;
	_end_indicator = _flag_version + 2;

	// todo: proper endian handling...
	if (_end_indicator[0] != 'I')
		throw Exception("endian check failed!");

	root = new _root(_end_indicator + 2, _tot_len - 128);

	_rec_find_mat(root);

}

__internal::_file::~_file()
{
	delete[] _data;
}

const std::list<__internal::_data_type_base*>& __internal::_file::nodes() const
{
	return root->nodes();
}

const std::string& __internal::_file::description() const
{
	return _desc;
}

const std::list<__internal::_matlab_array*>& __internal::_file::matricies() const
{
	return _matricies;
}

void __internal::_file::_rec_find_mat(_data_type_base* cur)
{
	if (cur->mft() == __internal::_matlab_array::MFT)
		_matricies.push_back(dynamic_cast<_matlab_array*>(cur));

	for (_data_type_base* child : cur->nodes())
		_rec_find_mat(child);
}

////////////////////////////////////
//         _basic_type            //
////////////////////////////////////

template<class T, std::int32_t _MFT>
__internal::_basic_type<T, _MFT>::_basic_type(char* start, int len)
{
	val = reinterpret_cast<T*>(start);
	length = len / sizeof(T);
}

template<class T, std::int32_t _MFT>
std::ostream& __internal::_basic_type<T, _MFT>::operator>>(std::ostream& src)
{
	src << MFT;
	src << length;
	for (std::uint32_t i = 0; i < length; ++i)
		src << val[i];
	return src;
}

template<class T, std::int32_t _MFT>
T* __internal::_basic_type<T, _MFT>::get() const
{
	return val;
}

template<class T, std::int32_t _MFT>
const std::uint32_t __internal::_basic_type<T, _MFT>::len() const
{
	return length;
}

template<class T, std::int32_t _MFT>
const std::int32_t __internal::_basic_type<T, _MFT>::mft() const
{
	return _MFT;
}

template<class T, std::int32_t _MFT>
const std::string __internal::_basic_type<T, _MFT>::to_string(bool cast) const
{
	std::stringstream ss;
	for (std::uint32_t i = 0; i < length; ++i)
	if (cast)
		ss << std::to_string(val[i]) << " ";
	else
		ss << val[i];
	return ss.str();
}
