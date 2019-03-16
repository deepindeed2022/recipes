#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/resource.h>
 
 
int bssvar;    //声明一个未定义的变量，它会放在 bss segment 中
 
int main(void)
{
	char *pmem;
	long heap_gap_bss;
	printf ("end of bss section:%p\n", (long)&bssvar + 4);
 
	pmem = (char *)malloc(32);          //从堆中分配一块内存区，一般从堆的开始处获取
	if (pmem == NULL) {
		perror("malloc");
		exit (EXIT_FAILURE);
	}
	printf ("pmem:%p\n", pmem);
 
	//计算堆的开始地址和 bss segment 结束处得空隙大小，注意每次加载程序时这个空隙都是变化的，但是在同一次加载中它不会改变
	heap_gap_bss = (long)pmem - (long)&bssvar - 4;          
	printf ("1-gap between heap and bss:%lu\n", heap_gap_bss);
	free (pmem);   //释放内存，归还给堆


	sbrk(32);        // 调整 program break 位置(假设现在不知道这个位置在堆头还是堆尾)
	pmem = (char *)malloc(32);   //再一次获取内存区
	if (pmem == NULL) {
			perror("malloc");
			exit (EXIT_FAILURE);
	}
	printf ("pmem:%p\n", pmem);   //检查和第一次获取的内存区的起始地址是否一样
	heap_gap_bss = (long)pmem - (long)&bssvar - 4;  //计算调整 program break 后的空隙
	printf ("2-gap between heap and bss:%lu\n", heap_gap_bss);
	free(pmem);   //释放
	return 0;
}
