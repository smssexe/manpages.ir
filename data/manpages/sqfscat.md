SQFSCAT(1)								 User Commands								    SQFSCAT(1)

NAME
       sqfscat - tool to cat files from a squashfs filesystem to stdout

SYNOPSIS
       sqfscat [OPTIONS] FILESYSTEM [list of files to cat to stdout]

DESCRIPTION
       Squashfs is a highly compressed read-only filesystem for Linux.	It uses either gzip/xz/lzo/lz4/zstd compression to compress both files, inodes and di‐
       rectories.   Inodes in the system are very small and all blocks are packed to minimise data overhead. Block sizes greater than 4K are supported up to a
       maximum of 1Mbytes (default block size 128K).

       Squashfs is intended for general read-only filesystem use, for archival use (i.e. in cases where a .tar.gz file may be used), and in constrained	 block
       device/memory systems (e.g. embedded systems) where low overhead is needed.

OPTIONS
       -v, -version
	      print version, licence and copyright information.

       -p NUMBER, -processors NUMBER
	      use NUMBER processors.  By default will use the number of processors available.

       -o BYTES, -offset BYTES
	      skip  BYTES  at  start  of FILESYSTEM. Optionally a suffix of K, M or G can be given to specify Kbytes, Mbytes or Gbytes respectively (default 0
	      bytes).

       -ig, -ignore-errors
	      treat errors writing files to stdout as non-fatal.

       -st, -strict-errors
	      treat all errors as fatal.

       -no-exit, -no-exit-code
	      don't set exit code (to nonzero) on non-fatal errors.

       -da SIZE, -data-queue SIZE
	      set data queue to SIZE Mbytes.  Default 256 Mbytes.

       -fr SIZE, -frag-queue SIZE
	      set fragment queue to SIZE Mbytes.  Default 256 Mbytes.

       -no-wild, -no-wildcards
	      do not use wildcard matching in filenames.

       -r, -regex
	      treat filenames as POSIX regular expressions rather than use the default shell wildcard expansion (globbing).

       -h, -help
	      output options text to stdout.

DECOMPRESSORS AVAILABLE
       gzip, lzo, lz4, xz, zstd, lzma

EXIT STATUS
       0      The file or files were output to stdout OK.

       1      FATAL errors occurred, e.g. filesystem corruption, I/O errors. Sqfscat did not continue and aborted.

       2      Non-fatal errors occurred, e.g. not a regular file, or failed to resolve pathname.  Sqfscat continued and did not abort.

       See -ignore-errors, -strict-errors and -no-exit-code options for how they affect the exit status.

EXAMPLES
       sqfscat IMAGE.SQFS hello
	      Output the contents of "hello" to stdout.

       sqfscat IMAGE.SQFS hello world
	      Output the contents of "hello" and then "world" to stdout.

       sqfscat IMAGE.SQFS "*.[ch]"
	      Output the contents of all the files in the root directory that match the wildcard *.[ch], to stdout, e.g.  hello.c, hello.h, world.c, world.h.

       Note: when passing wildcarded names to Sqfscat, they should be quoted (as in the above examples), to ensure that they are not processed by the shell.

AUTHOR
       Written by Phillip Lougher <phillip@squashfs.org.uk>

COPYRIGHT
       Copyright © 2023 Phillip Lougher <phillip@squashfs.org.uk>

       This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License  as  published	 by  the  Free
       Software Foundation; either version 2, or (at your option) any later version.

       This  program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FIT‐
       NESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

SEE ALSO
       mksquashfs(1), unsquashfs(1), sqfstar(1)

       The README for the Squashfs-tools 4.6.1 release, describing the new features  can  be  read  here  https://github.com/plougher/squashfs-tools/blob/mas‐
       ter/README-4.6.1

       The Squashfs-tools USAGE guide can be read here https://github.com/plougher/squashfs-tools/blob/master/USAGE-4.6

sqfscat version 4.6.1							  April 2024								    SQFSCAT(1)
