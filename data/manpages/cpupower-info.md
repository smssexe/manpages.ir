CPUPOWER-INFO(1)							cpupower Manual							      CPUPOWER-INFO(1)

NAME
       cpupower-info - Shows processor power related kernel or hardware configurations

SYNOPSIS
       cpupower info [ -b ]

DESCRIPTION
       cpupower info  shows kernel configurations or processor hardware registers affecting processor power saving policies.

       Some  options  are platform wide, some affect single cores. By default values of core zero are displayed only. cpupower --cpu all cpuinfo will show the
       settings of all cores, see cpupower(1) how to choose specific cores.

SEE ALSO
       Options are described in detail in:

       cpupower(1), cpupower-set(1)

									  22/02/2011							      CPUPOWER-INFO(1)
