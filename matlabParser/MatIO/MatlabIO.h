#ifndef MATLAB_INTERNAL_H
#define MATLAB_INTERNAL_H

#include <iostream>
#include <cstdint>
#include <list>
#include <fstream>
#include <sstream>

namespace Matlab
{
	namespace __internal
	{
        struct Exception : public std::exception
        {
            std::string _msg;
            Exception(std::string s) : _msg(s) { }
            ~Exception() throw() { }
            const char* what() const throw() { return _msg.c_str(); }
        };

		struct _data_type_base
		{
			virtual const std::list<_data_type_base*>& nodes() const
			{
				return children;
			}
			virtual std::ostream& operator>>(std::ostream& src) = 0;
			virtual ~_data_type_base() { }
			virtual const std::string to_string(bool cast = false) const
			{
				return "";
			}
			virtual const std::int32_t mft() const = 0;
			static const std::int32_t MFT = 0xFF;
		protected:
			std::list<_data_type_base*> children;
		};

		template<class T, std::int32_t _MFT>
		struct _basic_type : public _data_type_base
		{
			_basic_type(char* start, int len);
			std::ostream& operator>>(std::ostream& src);

			T* get() const;
			const std::uint32_t len() const;
			const std::int32_t mft() const;
			const std::string to_string(bool cast = false) const;

			static const std::int32_t MFT = _MFT;
		private:
			T* val;
			std::uint32_t length;
		};

		struct _root : public _data_type_base
		{
			const std::int32_t mft() const;
			static const std::int32_t MFT = 0x00;

			_root(char* start, int len);

			std::ostream& operator>>(std::ostream& src);

		};

		struct _compressed_type : public _data_type_base
		{
			static const std::int32_t MFT = 0x0F;
			_compressed_type(char* start, int len);
			~_compressed_type();

			std::ostream& operator>>(std::ostream& src);
			const std::int32_t mft() const;
		private:
			std::uint32_t compressed_data_len;
			std::size_t uncompressed_data_len;
			char* compressed_data;
			char* uncompressed_data;
		};
	}

	namespace DataTypes
	{
		typedef __internal::_basic_type<std::int8_t, 0x01> miINT8;
		typedef __internal::_basic_type<std::uint8_t, 0x02> miUINT8;
		typedef __internal::_basic_type<std::int16_t, 0x03> miINT16;
		typedef __internal::_basic_type<std::uint16_t, 0x04> miUINT16;
		typedef __internal::_basic_type<std::int32_t, 0x05> miINT32;
		typedef __internal::_basic_type<std::uint32_t, 0x06> miUINT32;
		typedef __internal::_basic_type<float, 0x07> miSINGLE;
		typedef __internal::_basic_type<double, 0x09> miDOUBLE;
		typedef __internal::_basic_type<std::int64_t, 0x0C> miINT64;
		typedef __internal::_basic_type<std::uint64_t, 0x0D> miUINT64;
		typedef __internal::_compressed_type miCOMPRESSED;
		typedef __internal::_basic_type<std::int8_t, 0x10> miUTF8;
		typedef __internal::_basic_type<std::int16_t, 0x11> miUTF16;
		typedef __internal::_basic_type<std::int32_t, 0x12> miUTF32;
	}
	namespace ArrayTypes
	{
		typedef __internal::_basic_type<char, 0x04> mxCHAR_CLASS;
		typedef __internal::_basic_type<double, 0x06> mxDOUBLE_CLASS;
		typedef __internal::_basic_type<float, 0x07> mxSINGLE_CLASS;
		typedef __internal::_basic_type<std::int8_t, 0x08> mxINT8_CLASS;
		typedef __internal::_basic_type<std::uint8_t, 0x09> mxUINT8_CLASS;
		typedef __internal::_basic_type<std::int16_t, 0x0A> mxINT16_CLASS;
		typedef __internal::_basic_type<std::uint16_t, 0x0B> mxUINT16_CLASS;
		typedef __internal::_basic_type<std::int32_t, 0x0C> mxINT32_CLASS;
		typedef __internal::_basic_type<std::uint32_t, 0x0D> mxUINT32_CLASS;
		typedef __internal::_basic_type<std::int64_t, 0x0E> mxINT64_CLASS;
		typedef __internal::_basic_type<std::uint64_t, 0x0F> mxUINT64_CLASS;
	}

	namespace __internal
	{
		struct _matlab_array : public _data_type_base
		{
			static const std::int32_t MFT = 0x0E;
			DataTypes::miUINT32* flags;
			DataTypes::miINT32* dimensions;
			DataTypes::miINT8* name;

			_matlab_array(char* start, int len);

			std::ostream& operator>>(std::ostream& src);
			~_matlab_array();
			const std::int32_t mft() const;
		private:
			template<class T>
			char* read_single_primitive(char* src, T** dest);
		};


		struct _file
		{
			const std::list<_matlab_array*>& matricies() const;
			
			const std::string& description() const;
			const std::list<_data_type_base*>& nodes() const;
			_file(std::string file_name);
			~_file();
		private:
			void _rec_find_mat(_data_type_base* cur);

			_root* root;
			std::string _desc;
			char* _subs_offset;
			char* _flag_version;
			char* _end_indicator;
			char* _data;
			bool _new;
			std::size_t _tot_len;
			std::list<_matlab_array*> _matricies;
		};

	}

	namespace DataTypes
	{
		typedef __internal::_matlab_array miMATRIX;
	}

	/*
		Classes exposed to users:
	*/

	typedef __internal::_file				File;
	typedef __internal::_data_type_base		Object;
	typedef __internal::_root				ElementContainer;
	typedef __internal::_compressed_type	CompressedNode;
	typedef __internal::_matlab_array		Matrix;
}

#endif
