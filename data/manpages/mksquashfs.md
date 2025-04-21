MKSQUASHFS(1)								 User Commands								 MKSQUASHFS(1)

NAME
       mksquashfs - tool to create and append to squashfs filesystems

SYNOPSIS
       mksquashfs source1 source2 ...  FILESYSTEM [OPTIONS] [-e list of exclude dirs/files]

DESCRIPTION
       Squashfs is a highly compressed read-only filesystem for Linux.	It uses either gzip/xz/lzo/lz4/zstd compression to compress both files, inodes and di‐
       rectories.   Inodes in the system are very small and all blocks are packed to minimise data overhead. Block sizes greater than 4K are supported up to a
       maximum of 1Mbytes (default block size 128K).

       Squashfs is intended for general read-only filesystem use, for archival use (i.e. in cases where a .tar.gz file may be used), and in constrained	 block
       device/memory systems (e.g. embedded systems) where low overhead is needed.

OPTIONS
   Filesystem compression options:
       -b BLOCK_SIZE
	      set data block to BLOCK_SIZE.  Default 128 Kbytes. Optionally a suffix of K or M can be given to specify Kbytes or Mbytes respectively.

       -comp COMP
	      select COMP compression. Compressors available: gzip (default), lzo, lz4, xz, zstd, lzma.

       -noI   do not compress inode table.

       -noId  do not compress the uid/gid table (implied by -noI).

       -noD   do not compress data blocks.

       -noF   do not compress fragment blocks.

       -noX   do not compress extended attributes.

       -no-compression
	      do not compress any of the data or metadata.  This is equivalent to specifying -noI -noD -noF and -noX.

   Filesystem build options:
       -tar   read uncompressed tar file from standard in (stdin).

       -no-strip
	      act like tar, and do not strip leading directories from source files.

       -tarstyle
	      alternative name for -no-strip.

       -cpiostyle
	      act like cpio, and read file pathnames from standard in (stdin).

       -cpiostyle0
	      like -cpiostyle, but filenames are null terminated.  Can be used with find -print0 action.

       -reproducible
	      build filesystems that are reproducible (default).

       -not-reproducible
	      build filesystems that are not reproducible.

       -mkfs-time TIME
	      set  filesystem creation timestamp to TIME. TIME can be an unsigned 32-bit int indicating seconds since the epoch (1970-01-01) or a string value
	      which is passed to the "date" command to parse. Any string value which the date command recognises can be used such as "now",  "last  week",  or
	      "Wed Feb 15 21:02:39 GMT 2023".

       -all-time TIME
	      set  all	file timestamps to TIME. TIME can be an unsigned 32-bit int indicating seconds since the epoch (1970-01-01) or a string value which is
	      passed to the "date" command to parse. Any string value which the date command recognises can be used such as "now", "last week", or "Wed Feb 15
	      21:02:39 GMT 2023".

       -root-time TIME
	      set root directory time to TIME. TIME can be an unsigned 32-bit int indicating seconds since the epoch (1970-01-01) or a string value  which  is
	      passed to the "date" command to parse. Any string value which the date command recognises can be used such as "now", "last week", or "Wed Feb 15
	      21:02:39 GMT 2023".

       -root-mode MODE
	      set root directory permissions to octal MODE.

       -root-uid VALUE
	      set root directory owner to specified VALUE, VALUE can be either an integer uid or user name.

       -root-gid VALUE
	      set root directory group to specified VALUE, VALUE can be either an integer gid or group name.

       -all-root
	      make all files owned by root.

       -force-uid VALUE
	      set all file uids to specified VALUE, VALUE can be either an integer uid or user name.

       -force-gid VALUE
	      set all file gids to specified VALUE, VALUE can be either an integer gid or group name.

       -pseudo-override
	      make pseudo file uids and gids override -all-root, -force-uid and -force-gid options.

       -no-exports
	      do not make filesystem exportable via NFS (-tar default).

       -exports
	      make filesystem exportable via NFS (default).

       -no-sparse
	      do not detect sparse files.

       -no-tailends
	      do not pack tail ends into fragments (default).

       -tailends
	      pack tail ends into fragments.

       -no-fragments
	      do not use fragments.

       -no-duplicates
	      do not perform duplicate checking.

       -no-hardlinks
	      do not hardlink files, instead store duplicates.

       -keep-as-directory
	      if one source directory is specified, create a root directory containing that directory, rather than the contents of the directory.

   Filesystem filter options:
       -p PSEUDO-DEFINITION
	      add pseudo file definition.  The definition should be quoted.

       -pf PSEUDO-FILE
	      add list of pseudo file definitions from PSEUDO-FILE, use - for stdin.  Pseudo file definitions should not be quoted.

       -sort SORT_FILE
	      sort files according to priorities in SORT_FILE.	One file or dir with priority per line.	 Priority -32768 to 32767, default priority 0.

       -ef EXCLUDE_FILE
	      list of exclude dirs/files.  One per line.

       -wildcards
	      allow extended shell wildcards (globbing) to be used in exclude dirs/files.

       -regex allow POSIX regular expressions to be used in exclude dirs/files.

       -max-depth LEVELS
	      descend at most LEVELS of directories when scanning filesystem.

       -one-file-system
	      do not cross filesystem boundaries.  If a directory crosses the boundary, create an empty directory for each mount point.	 If a file crosses the
	      boundary ignore it.

       -one-file-system-x
	      do not cross filesystem boundaries. Like -one-file-system option except directories are also ignored if they cross the boundary.

   Filesystem extended attribute (xattrs) options:
       -no-xattrs
	      do not store extended attributes.

       -xattrs
	      store extended attributes (default).

       -xattrs-exclude REGEX
	      exclude  any xattr names matching REGEX.	REGEX is a POSIX regular expression, e.g. -xattrs-exclude '^user.' excludes xattrs from the user name‐
	      space.

       -xattrs-include REGEX
	      include any xattr names matching REGEX.  REGEX is a POSIX regular expression, e.g. -xattrs-include '^user.' includes xattrs from the user	 name‐
	      space.

       -xattrs-add NAME=VAL
	      add  the xattr NAME with VAL to files.  If an user xattr it will be added to regular files and directories (see man 7 xattr).  Otherwise it will
	      be added to all files.  VAL by default will be treated as binary (i.e. an uninterpreted byte sequence), but it can be prefixed with 0s, where it
	      will be treated as base64 encoded, or prefixed with 0x, where val will be treated as hexidecimal.	 Additionally it can be prefixed with 0t where
	      this encoding is similar to binary encoding, except backslashes are specially treated, and a backslash followed by 3 octal digits can be used to
	      encode any ASCII character, which obviously can be used to encode control codes.	The option can be repeated multiple times to add multiple xat‐
	      trs.

   Mksquashfs runtime options:
       -version
	      print version, licence and copyright message.

       -exit-on-error
	      treat normally ignored errors as fatal.

       -quiet no verbose output.

       -info  print files written to filesystem.

       -no-progress
	      do not display the progress bar.

       -progress
	      display progress bar when using the -info option.

       -percentage
	      display a percentage rather than the full progress bar. Can be used with dialog --gauge etc.

       -throttle PERCENTAGE
	      throttle the I/O input rate by the given percentage. This can be used to reduce the I/O and CPU consumption of Mksquashfs.

       -limit PERCENTAGE
	      limit the I/O input rate to the given percentage. This can be used to reduce the I/O and CPU consumption of Mksquashfs (alternative  to  -throt‐
	      tle).

       -processors NUMBER
	      use NUMBER processors.  By default will use number of processors available.

       -mem SIZE
	      use SIZE physical memory for caches.  Use K, M or G to specify Kbytes, Mbytes or Gbytes respectively.

       -mem-percent PERCENT
	      use PERCENT physical memory for caches.  Default 25%.

       -mem-default
	      print default memory usage in Mbytes.

   Filesystem append options:
       -noappend
	      do not append to existing filesystem.

       -root-becomes NAME
	      when  appending  source  files/directories, make the original root become a subdirectory in the new root called NAME, rather than adding the new
	      source items to the original root.

       -no-recovery
	      do not generate a recovery file.

       -recovery-path NAME
	      use NAME as the directory to store the recovery file.

       -recover NAME
	      recover filesystem data using recovery file NAME.

   Filesystem actions options:
       -action ACTION@EXPRESSION
	      evaluate EXPRESSION on every file, and execute ACTION if it returns TRUE.

       -log-action ACTION@EXPRESSION
	      as above, but log expression evaluation results and actions performed.

       -true-action ACTION@EXPRESSION
	      as above, but only log expressions which return TRUE.

       -false-action ACTION@EXPRESSION
	      as above, but only log expressions which return FALSE.

       -action-file FILE
	      as action, but read actions from FILE.

       -log-action-file FILE
	      as -log-action, but read actions from FILE.

       -true-action-file FILE
	      as -true-action, but read actions from FILE.

       -false-action-file FILE
	      as -false-action, but read actions from FILE.

   Tar file only options:
       -default-mode MODE
	      tar files often do not store permissions for intermediate directories.  This option sets the default directory permissions to octal MODE, rather
	      than 0755. This also sets the root inode mode.

       -default-uid UID
	      tar files often do not store uids for intermediate directories.  This option sets the default directory owner to UID, rather than the user  run‐
	      ning Mksquashfs. This also sets the root inode uid.

       -default-gid GID
	      tar  files  often do not store gids for intermediate directories.	 This option sets the default directory group to GID, rather than the group of
	      the user running Mksquashfs.  This also sets the root inode gid.

       -ignore-zeros
	      allow tar files to be concatenated together and fed to Mksquashfs.  Normally a tarfile has two consecutive 512 byte  blocks  filled  with	 zeros
	      which  means  EOF	 and  Mksquashfs will stop reading after the first tar file on encountering them. This option makes Mksquashfs ignore the zero
	      filled blocks.

   Expert options (these may make the filesystem unmountable):
       -nopad do not pad filesystem to a multiple of 4K.

       -offset OFFSET
	      skip OFFSET bytes at the beginning of FILESYSTEM. Optionally a suffix of K, M or G can be given to specify  Kbytes,  Mbytes  or  Gbytes  respec‐
	      tively. Default 0 bytes.

       -o OFFSET
	      synonym for -offset.

   Miscellaneous options:
       -fstime TIME
	      alternative name for -mkfs-time.

       -always-use-fragments
	      alternative name for -tailends.

       -root-owned
	      alternative name for -all-root.

       -noInodeCompression
	      alternative name for -noI.

       -noIdTableCompression
	      alternative name for -noId.

       -noDataCompression
	      alternative name for -noD.

       -noFragmentCompression
	      alternative name for -noF.

       -noXattrCompression
	      alternative name for -noX.

       -help  output this options text to stdout.

       -h     output this options text to stdout.

       -Xhelp print compressor options for selected compressor.

PSEUDO FILE DEFINITION FORMAT
       -p "filename d mode uid gid"
	      create a directory.

       -p "filename m mode uid gid"
	      modify filename.

       -p "filename b mode uid gid major minor"
	      create a block device.

       -p "filename c mode uid gid major minor"
	      create a character device.

       -p "filename f mode uid gid command"
	      create file from stdout of command.

       -p "filename s mode uid gid symlink"
	      create a symbolic link.

       -p "filename i mode uid gid [s|f]"
	      create a socket (s) or FIFO (f).

       -p "filename x name=val"
	      create an extended attribute.

       -p "filename l linkname"
	      create a hard-link to linkname.

       -p "filename L pseudo_filename"
	      same, but link to pseudo file.

       -p "filename D time mode uid gid"
	      create a directory with timestamp time.

       -p "filename M time mode uid gid"
	      modify a file with timestamp time.

       -p "filename B time mode uid gid major minor"
	      create block device with timestamp time.

       -p "filename C time mode uid gid major minor"
	      create char device with timestamp time.

       -p "filename F time mode uid gid command"
	      create file with timestamp time.

       -p "filename S time mode uid gid symlink"
	      create symlink with timestamp time.

       -p "filename I time mode uid gid [s|f]"
	      create socket/fifo with timestamp time.

COMPRESSORS AVAILABLE AND COMPRESSOR SPECIFIC OPTIONS
   gzip (default):
       -Xcompression-level COMPRESSION-LEVEL
	      COMPRESSION-LEVEL should be 1 .. 9 (default 9).

       -Xwindow-size WINDOW-SIZE
	      WINDOW-SIZE should be 8 .. 15 (default 15).

       -Xstrategy strategy1,strategy2,...,strategyN
	      Compress using strategy1,strategy2,...,strategyN in turn and choose the best compression. Available strategies: default, filtered, huffman_only,
	      run_length_encoded and fixed.

   lzo:
       -Xalgorithm ALGORITHM
	      Where ALGORITHM is one of: lzo1x_1, lzo1x_1_11, lzo1x_1_12, lzo1x_1_15, lzo1x_999 (default).

       -Xcompression-level COMPRESSION-LEVEL
	      COMPRESSION-LEVEL should be 1 .. 9 (default 8) Only applies to lzo1x_999 algorithm.

   lz4:
       -Xhc   Compress using LZ4 High Compression.

   xz:
       -Xbcj filter1,filter2,...,filterN
	      Compress	using  filter1,filter2,...,filterN  in	turn (in addition to no filter), and choose the best compression. Available filters: x86, arm,
	      armthumb, powerpc, sparc, ia64.

       -Xdict-size DICT-SIZE
	      Use DICT-SIZE as the XZ dictionary size.	The dictionary size can be specified as a percentage of the block size, or as an absolute value.   The
	      dictionary  size must be less than or equal to the block size and 8192 bytes or larger.  It must also be storable in the xz header as either 2^n
	      or as 2^n+2^(n+1). Example dict-sizes are 75%, 50%, 37.5%, 25%, or 32K, 16K, 8K etc.

   zstd:
       -Xcompression-level COMPRESSION-LEVEL
	      COMPRESSION-LEVEL should be 1 .. 22 (default 15).

   lzma:
	      (no options) (deprecated - no kernel support)

ENVIRONMENT
       SOURCE_DATE_EPOCH
	      If set, this is used as the filesystem creation timestamp.  Also any file timestamps which  are  after  SOURCE_DATE_EPOCH	 will  be  clamped  to
	      SOURCE_DATE_EPOCH.  See https://reproducible-builds.org/docs/source-date-epoch/ for more information.

EXAMPLES
       mksquashfs DIRECTORY IMAGE.SQFS
	      Create a Squashfs filesystem from the contents of DIRECTORY, writing the output to IMAGE.SQSH.  Mksquashfs will use the default compressor (nor‐
	      mally gzip), and block size of 128 Kbytes.

       mksquashfs DIRECTORY FILE1 FILE2 IMAGE.SQFS
	      Create  a Squashfs filesystem containing DIRECTORY and FILE1 and FILE2.  If multiple sources are specified on the command line they will be com‐
	      bined into a single directory.

       mksquashfs DIRECTORY IMAGE.SQFS -b 1M -comp zstd
	      Use a block size of 1 Mbyte and Zstandard compression to create the filesystem.

       mksquashfs DIRECTORY IMAGE.SQFS -e file1 file2
	      Exclude file1 and file2 from DIRECTORY when creating filesystem.	No wildcard matching of files.

       mksquashfs DIRECTORY IMAGE.SQFS -wildcards -e "*.gz"
	      Exclude anything in DIRECTORY which matches the wildcard pattern "*.gz".

       mksquashfs DIRECTORY IMAGE.SQFS -wildcards -e "... *.gz"
	      Exclude files which match the wildcard pattern "*.gz" anywhere within DIRECTORY and its sub-directories.	The initial "..." indicates the	 wild‐
	      card pattern is "non-anchored" and will match anywhere.

       Note:  when  passing  wildcarded	 names	to  Mksquashfs, they should be quoted (as in the above examples), to ensure that they are not processed by the
       shell.

   Using pseudo file definitions
       mksquashfs DIRECTORY IMAGE.SQFS -p "build_dir d 0644 0 0"
	      Create a directory called "build_dir" in the output filesystem.

       mksquashfs DIRECTORY IMAGE.SQFS -p "version.txt l /tmp/build/version"
	      Create a reference called "version.txt" to a file outside DIRECTORY, which acts as if the file "/tmp/build/version" was  copied  or  hard-linked
	      into DIRECTORY before calling Mksquashfs.

       mksquashfs DIRECTORY IMAGE.SQFS -p "date.txt f 0644 0 0 date"
	      Create a file called "date.txt" which holds the output (stdout) from running the "date" command.

       mksquashfs DIRECTORY IMAGE.SQFS -p "\"hello world\" f 0644 0 0 date"
	      As above, but, showing that filenames can have spaces, if they are quoted.  The quotes need to be blackslashed to protect them from the shell.

       mksquashfs - IMAGE.SQFS -p "input f 0644 root root dd if=/dev/sda1 bs=1024" -p "/ d 0644 0 0"
	      Create a file containing the contents of partition /dev/sda1".  Ordinarily Mksquashfs given a device, fifo, or named socket will place that spe‐
	      cial  file within the Squashfs filesystem, the above allows input from these special files to be captured and placed in the Squashfs filesystem.
	      Note there are no other sources than the pseudo file, and so the command line source is "-".  If there are no other sources than	pseudo	files,
	      the root (/) directory must be defined too, as seen in this example.

       unsquashfs -pf - IMAGE.SQFS | mksquashfs - NEW.SQFS -pf -
	      Transcode	 IMAGE.SQFS  to NEW.SQFS by piping the pseudo file output from Unsquashfs to Mksquashfs using stdout and stdin.	 This can convert from
	      earlier Squashfs filesystems or change compression algorithm, block size etc.  without needing to unpack into an intermediate directory or file.

       Note: pseudo file definitions should be quoted (as in the above examples), to ensure that they are passed to Mksquashfs as a single  argument,  and  to
       ensure that they are not processed by the shell.

   Using extended attribute options
       mksquashfs DIRECTORY IMAGE.SQFS -no-xattrs
	      Do not store any extended attributes in the Squashfs filesystem.	Any extended attributes in the source files will be ignored.

       mksquashfs DIRECTORY IMAGE.SQFS -xattrs-include "^user."
	      Filter the extended attributes in the source files, and only store extended attributes in the user namespace in the Squashfs filesystem.

       mksquashfs DIRECTORY IMAGE.SQFS -xattrs-exclude "^user."
	      Filter the extended attributes in the source files, and don't store any extended attributes in the user namespace in the Squashfs filesystem.

       mksquashfs DIRECTORY IMAGE.SQFS -xattrs-add "user.comment=hello world"
	      Add the extended attribute called "user.comment" with the content "hello world" to all files and directories in the Squashfs filesystem.

       mksquashfs DIRECTORY IMAGE.SQFS -xattrs-add "user.comment=0thello world\012"
	      Add  the	extended attribute called "user.comment" to all files and directories, but in this case the contents of the extended attribute will be
	      "hello world" with a trailing newline character (012 octal).

       mksquashfs DIRECTORY IMAGE.SQFS -xattrs-add "user.comment=0saGVsbG8gd29ybGQ="
	      Add the extended attribute called "user.comment" to all files and directories, where the value is given in base64 encoding, representing	"hello
	      world".

       mksquashfs DIRECTORY IMAGE.SQFS -action "-xattrs-include(^user.) @ type(f)"
	      Filter the extended attributes but only in regular files (type f), and only store extended attributes in the user namespace.

       mksquashfs DIRECTORY IMAGE.SQFS -p "hello_world x user.comment=0tsalve mundi\012"
	      Add  the	extended  attribute  called  "user.comment" to the file called "hello_world", with the contents of the extended attribute being "salve
	      mundi" with a trailing newline character (012 octal).

   Using Actions to not compress, change attributes etc.
       mksquashfs DIRECTORY IMAGE.SQSH -action "uncompressed @ (name(*.jpg) || name(*.mpg) ) || (name(*.img) && filesize(+1G))"
	      Specify that any files matching the wildcards "*.jpg" and "*.mpg" should not be compressed.  Additionally, it also specifies any files  matching
	      the  wildcard "*.img" and are larger than 1 Gigabyte should be uncompressed too.	This shows test operators can be combined with logical expres‐
	      sions.

       mksquashfs DIRECTORY IMAGE.SQSH -action "chmod(o+r)@! perm(o+r)"
	      If any files within DIRECTORY are not readable by "others", then make them readable by others in the Squashfs filesystem.

       mksquashfs DIRECTORY IMAGE.SQSH -action "uid(phillip)@! perm(o+r)"
	      As previous, match on any files which are not readable by "others", but, in this case change the owner of the file to "phillip" in the  Squashfs
	      filesystem.

       mksquashfs DIRECTORY IMAGE.SQSH -action "prune @ type(l) && ! exists"
	      Delete any symbolic link within DIRECTORY which points outside of DIRECTORY, i.e. will be unresolvable in the Squashfs filesystem.

       mksquashfs DIRECTORY IMAGE.SQSH -action "exclude @ depth(3)"
	      Create  a	 Squashfs filesystem containing the two top most levels (contents of DIRECTORY and immediate sub-directories), and exclude anything at
	      level 3 or below.

       mksquashfs DIRECTORY IMAGE.SQFS -action "-xattrs-include(^user.) @ type(f)"
	      Filter the extended attributes but only in regular files (type f), and only store extended attributes in the user namespace.

       Note: actions should be quoted (as in the above examples), to ensure that they are passed to Mksquashfs as a single argument, and to ensure  that  they
       are not processed by the shell.

AUTHOR
       Written by Phillip Lougher <phillip@squashfs.org.uk>

COPYRIGHT
       Copyright © 2023 Phillip Lougher <phillip@squashfs.org.uk>

       This  program  is  free	software;  you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free
       Software Foundation; either version 2, or (at your option) any later version.

       This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or  FIT‐
       NESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

SEE ALSO
       unsquashfs(1), sqfstar(1), sqfscat(1)

       The  README  for	 the  Squashfs-tools  4.6.1 release, describing the new features can be read here https://github.com/plougher/squashfs-tools/blob/mas‐
       ter/README-4.6.1

       The Squashfs-tools USAGE guide can be read here https://github.com/plougher/squashfs-tools/blob/master/USAGE-4.6

       The ACTIONS-README file describing how to use the new actions  feature  can  be	read  here  https://github.com/plougher/squashfs-tools/blob/master/AC‐
       TIONS-README

mksquashfs version 4.6.1						  April 2024								 MKSQUASHFS(1)
