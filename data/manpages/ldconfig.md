ldconfig(8)							    System Manager's Manual							   ldconfig(8)

NAME
       ldconfig - configure dynamic linker run-time bindings

SYNOPSIS
       /sbin/ldconfig [-nNvVX] [-C cache] [-f conf] [-r root] directory ...

       /sbin/ldconfig -l [-v] library ...

       /sbin/ldconfig -p

DESCRIPTION
       ldconfig	 creates the necessary links and cache to the most recent shared libraries found in the directories specified on the command line, in the file
       /etc/ld.so.conf, and in the trusted directories, /lib and /usr/lib.  On some 64-bit architectures such as x86-64, /lib and /usr/lib are the trusted di‐
       rectories for 32-bit libraries, while /lib64 and /usr/lib64 are used for 64-bit libraries.

       The cache is used by the run-time linker, ld.so or ld-linux.so.	ldconfig checks the header and filenames of the libraries it encounters when determin‐
       ing which versions should have their links updated.  ldconfig should normally be run by the superuser as it may require write permission on  some  root
       owned directories and files.

       ldconfig will look only at files that are named lib*.so* (for regular shared objects) or ld-*.so* (for the dynamic loader itself).  Other files will be
       ignored.	 Also, ldconfig expects a certain pattern to how the symbolic links are set up, like this example, where the middle file (libfoo.so.1 here) is
       the SONAME for the library:

	   libfoo.so -> libfoo.so.1 -> libfoo.so.1.12

       Failure to follow this pattern may result in compatibility issues after an upgrade.

OPTIONS
       --format=fmt
       -c fmt (Since glibc 2.2) Use cache format fmt, which is one of old, new, or compat.  Since glibc 2.32, the default is new.  Before that, it was compat.

       -C cache
	      Use cache instead of /etc/ld.so.cache.

       -f conf
	      Use conf instead of /etc/ld.so.conf.

       --ignore-aux-cache
       -i     (Since glibc 2.7) Ignore auxiliary cache file.

       -l     (Since glibc 2.2) Interpret each operand as a library name and configure its links.  Intended for use only by experts.

       -n     Process  only the directories specified on the command line; don't process the trusted directories, nor those specified in /etc/ld.so.conf.  Im‐
	      plies -N.

       -N     Don't rebuild the cache.	Unless -X is also specified, links are still updated.

       --print-cache
       -p     Print the lists of directories and candidate libraries stored in the current cache.

       -r root
	      Change to and use root as the root directory.

       --verbose
       -v     Verbose mode.  Print current version number, the name of each directory as it is scanned, and any links that are created.	 Overrides quiet mode.

       --version
       -V     Print program version.

       -X     Don't update links.  Unless -N is also specified, the cache is still rebuilt.

FILES
       /lib/ld.so
	      is the run-time linker/loader.
       /etc/ld.so.conf
	      contains a list of directories, one per line, in which to search for libraries.
       /etc/ld.so.cache
	      contains an ordered list of libraries found in the directories specified in /etc/ld.so.conf, as well as those found in the trusted directories.

SEE ALSO
       ldd(1), ld.so(8)

Linux man-pages 6.7							  2023-10-31								   ldconfig(8)
