UNSQUASHFS(1)								 User Commands								 UNSQUASHFS(1)

NAME
       unsquashfs - tool to uncompress, extract and list squashfs filesystems

SYNOPSIS
       unsquashfs [OPTIONS] FILESYSTEM [files to extract or exclude (with -excludes) or cat (with -cat )]

DESCRIPTION
       Squashfs is a highly compressed read-only filesystem for Linux.	It uses either gzip/xz/lzo/lz4/zstd compression to compress both files, inodes and di‐
       rectories.   Inodes in the system are very small and all blocks are packed to minimise data overhead. Block sizes greater than 4K are supported up to a
       maximum of 1Mbytes (default block size 128K).

       Squashfs is intended for general read-only filesystem use, for archival use (i.e. in cases where a .tar.gz file may be used), and in constrained	 block
       device/memory systems (e.g. embedded systems) where low overhead is needed.

OPTIONS
   Filesystem extraction (filtering) options:
       -d PATHNAME, -dest PATHNAME
	      extract to PATHNAME, default "squashfs-root". This option also sets the prefix used when listing the filesystem.

       -max LEVELS, -max-depth LEVELS
	      descend at most LEVELS of directories when extracting.

       -excludes
	      treat files on command line as exclude files.

       -ex, -exclude-list
	      list of files to be excluded, terminated with ; e.g. file1 file2 ;.

       -extract-file FILE
	      list of directories or files to extract. One per line.

       -exclude-file FILE
	      list of directories or files to exclude. One per line.

       -match abort if any extract file does not match on anything, and can not be resolved.  Implies -missing-symlinks and -no-wildcards.

       -follow, -follow-symlinks
	      follow symlinks in extract files, and add all files/symlinks needed to resolve extract file. Implies -no-wildcards.

       -missing, -missing-symlinks
	      Unsquashfs will abort if any symlink can't be resolved in -follow-symlinks.

       -no-wild, -no-wildcards
	      do not use wildcard matching in extract and exclude names.

       -r, -regex
	      treat extract names as POSIX regular expressions rather than use the default shell wildcard expansion (globbing).

       -all TIME, -all-time TIME
	      set  all	file  timestamps  to TIME, rather than the time stored in the filesystem inode.	 TIME can be an unsigned 32-bit int indicating seconds
	      since the epoch (1970-01-01) or a string value which is passed to the "date" command to parse. Any string value which the	 date  command	recog‐
	      nises can be used such as "now", "last week", or "Wed Feb 15 21:02:39 GMT 2023".

       -cat   cat the files on the command line to stdout.

       -f, -force
	      if file already exists then overwrite.

       -pf FILE
	      output a pseudo file equivalent of the input Squashfs filesystem, use - for stdout.

   Filesystem information and listing options:
       -s, -stat
	      display filesystem superblock information.

       -max LEVELS, -max-depth LEVELS
	      descend at most LEVELS of directories when listing.

       -i, -info
	      print files as they are extracted.

       -li, -linfo
	      print files as they are extracted with file attributes (like ls -l output).

       -l, -ls
	      list filesystem, but do not extract files.

       -ll, -lls
	      list filesystem with file attributes (like ls -l output), but do not extract files.

       -lln, -llnumeric
	      same as -lls but with numeric uids and gids.

       -lc    list filesystem concisely, displaying only files and empty directories.  Do not extract files.

       -llc   list filesystem concisely with file attributes, displaying only files and empty directories. Do not extract files.

       -full, -full-precision
	      use full precision when displaying times including seconds.  Use with -linfo, -lls, -lln and -llc.

       -UTC   use UTC rather than local time zone when displaying time.

       -mkfs-time
	      display filesystem superblock time, which is an unsigned 32-bit int representing the time in seconds since the epoch (1970-01-01).

   Filesystem extended attribute (xattrs) options:
       -no, -no-xattrs
	      do not extract xattrs in file system.

       -x, -xattrs
	      extract xattrs in file system (default).

       -xattrs-exclude REGEX
	      exclude  any  xattr names matching REGEX. REGEX is a POSIX regular expression, e.g. -xattrs-exclude '^user.' excludes xattrs from the user name‐
	      space.

       -xattrs-include REGEX
	      include any xattr names matching REGEX. REGEX is a POSIX regular expression, e.g. -xattrs-include '^user.' includes xattrs from the  user	 name‐
	      space.

   Unsquashfs runtime options:
       -v, -version
	      print version, licence and copyright information.

       -p NUMBER, -processors NUMBER
	      use NUMBER processors.  By default will use the number of processors available.

       -q, -quiet
	      no verbose output.

       -n, -no-progress
	      do not display the progress bar.

       -percentage
	      display a percentage rather than the full progress bar.  Can be used with dialog --gauge etc.

       -ig, -ignore-errors
	      treat errors writing files to output as non-fatal.

       -st, -strict-errors
	      treat all errors as fatal.

       -no-exit, -no-exit-code
	      do not set exit code (to nonzero) on non-fatal errors.

       -da SIZE, -data-queue SIZE
	      set data queue to SIZE Mbytes.  Default 256 Mbytes.

       -fr SIZE, -frag-queue SIZE
	      set fragment queue to SIZE Mbytes.  Default 256 Mbytes.

   Miscellaneous options:
       -h, -help
	      output this options text to stdout.

       -o BYTES, -offset BYTES
	      skip  BYTES  at  start of FILESYSTEM.  Optionally a suffix of K, M or G can be given to specify Kbytes, Mbytes or Gbytes respectively (default 0
	      bytes).

       -fstime
	      synonym for -mkfs-time.

       -e, -ef EXTRACT FILE
	      synonym for -extract-file.

       -exc, -excf EXCLUDE FILE
	      synonym for -exclude-file.

       -L     synonym for -follow-symlinks.

       -pseudo-file FILE
	      alternative name for -pf.

DECOMPRESSORS AVAILABLE
       gzip, lzo, lz4, xz, zstd, lzma

EXIT STATUS
       0      The filesystem listed or extracted OK.

       1      FATAL errors occurred, e.g. filesystem corruption, I/O errors. Unsquashfs did not continue and aborted.

       2      Non-fatal errors occurred, e.g. no support for XATTRs, Symbolic links in output filesystem or couldn't write permissions to  output  filesystem.
	      Unsquashfs continued and did not abort.

       See -ignore-errors, -strict-errors and -no-exit-code options for how they affect the exit status.

EXAMPLES
       unsquashfs IMAGE.SQFS
	      Extract IMAGE.SQFS to "squashfs-root" in the current working directory.

       unsquashfs -d output IMAGE.SQFS
	      Extract IMAGE.SQFS to "output" in the current working directory.

       unsquashfs -d . IMAGE.SQFS
	      Extract IMAGE.SQFS to current working directory.

       unsquashfs -linfo IMAGE.SQFS
	      Output a listing of IMAGE.SQFS with file attributes to stdout, while extracting the filesystem to "squashfs-root".

       unsquashfs -lls IMAGE.SQFS
	      Output  a listing of IMAGE.SQFS with file attributes to stdout, but do not extract the filesystem.  The listing will be prefixed with "squashfs-
	      root".

       unsquashfs -d "" -lls IMAGE.SQFS
	      Output a listing of IMAGE.SQFS with file attributes to stdout, but do not extract the  filesystem.   The	listing	 will  not  be	prefixed  with
	      "squashfs-root".

       unsquashfs IMAGE.SQFS fs/squashfs
	      Extract only the "fs/squashfs" directory.

       unsquashfs IMAGE.SQFS "[Tt]est/example*"
	      Extract all files beginning with "example" inside top level directories called "Test" or "test".

       unsquashfs -excludes IMAGE.SQFS "test/*data*.gz"
	      This  will extract everything except for files that match *data*.gz in the test directory.  The -excludes option tells Unsquashfs to exclude the
	      files on the command line rather than extract them.

       unsquashfs -excludes IMAGE.SQFS "... *.gz"
	      This will extract everything except for files that match *.gz anywhere in the image.   The "..." means this  is  a  non-anchored	exclude	 which
	      matches anywhere.

       unsquashfs -ex "test/*data*.gz" ; IMAGE.SQFS test
	      This  uses  both	extract	 and exclude options, to tell Unsquashfs to only extract the "test" directory, and to exclude any files within it that
	      match *data*.gz.

       unsquashfs -ex "... *.gz" IMAGE.SQFS test
	      This uses both extract and exclude options, to tell Unsquashfs to only extract the "test" directory, and to exclude  files  which	 match	"*.gz"
	      anywhere within "test" directory or sub-directories.

       unsquashfs -dest output -max-depth 2 IMAGE.SQFS
	      Extract only the top two levels of IMAGE.SQFS to "output" directory.

       unsquashfs -max-depth 2 IMAGE.SQFS "test/*.gz"
	      Only extract the gzipped files in the test directory.

       unsquashfs -llc -max-depth 2 IMAGE.SQFS "test/*.gz"
	      Output a listing of the gzipped files in the test directory to stdout, but do not extract them.

       unsquashfs -no-xattrs IMAGE.SQFS
	      Do not extract any extended attributes.  Any extended attributes in the filesystem will be ignored.

       unsquashfs -xattrs-include "^user." IMAGE.SQFS
	      Filter the extended attributes and only extract extended attributes in the user namespace from the Squashfs filesystem.

       unsquashfs -xattrs-exclude "^user." IMAGE.SQFS
	      Filter the extended attributes and do not extract any extended attributes in the user namespace from the Squashfs filesystem.

       Note:  when  passing  wildcarded	 names	to  Unsquashfs, they should be quoted (as in the above examples), to ensure that they are not processed by the
       shell.

AUTHOR
       Written by Phillip Lougher <phillip@squashfs.org.uk>

COPYRIGHT
       Copyright © 2023 Phillip Lougher <phillip@squashfs.org.uk>

       This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License  as  published	 by  the  Free
       Software Foundation; either version 2, or (at your option) any later version.

       This  program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FIT‐
       NESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

SEE ALSO
       mksquashfs(1), sqfstar(1), sqfscat(1)

       The README for the Squashfs-tools 4.6.1 release, describing the new features  can  be  read  here  https://github.com/plougher/squashfs-tools/blob/mas‐
       ter/README-4.6.1

       The Squashfs-tools USAGE guide can be read here https://github.com/plougher/squashfs-tools/blob/master/USAGE-4.6

unsquashfs version 4.6.1						  April 2024								 UNSQUASHFS(1)
