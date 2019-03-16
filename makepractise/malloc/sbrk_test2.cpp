#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/resource.h>
 
 
int main(void)
{
    void *tret;
    char *pmem;
    pmem = (char *)malloc(32);
    if (pmem == NULL) {
        perror("malloc");
        exit (EXIT_FAILURE);
    }

    printf ("pmem:%p\n", pmem);

    tret = sbrk(0);
    if (tret != (void *)-1)
        printf ("heap size on each load: %lu\n", (long)tret - (long)pmem);
    return 0;
}

// #sysctl - w kernel / randomize_va_space = 0
