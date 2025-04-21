erofs(5)							      File Formats Manual							      erofs(5)

NAME
       erofs - the Enhanced Read-Only File System

DESCRIPTION
       erofs is a create-once read-only filesystem, with support for compression and a multi-device backing store.

       There are two inode formats:

       •  32-byte compact with 16-bit UID/GID, 32-bit file size, and no file times
       •  64-byte extended with 32-bit UID/GID, 64-bit file size, and a modification time (st_mtim).

   Mount options
       user_xattr
       nouser_xattr
	      Controls whether user extended attributes are exposed.  Defaults to yes.

       acl
       noacl  Controls whether POSIX acl(5)s are exposed.  Defaults to yes.

       cache_strategy=disabled|readahead|readaround
	      Cache allocation for compressed files: never, if reading from start of file, regardless of position.  Defaults to readaround.

       dax
       dax=always|never
	      Direct  Access  control.	 If  always  and  the  source device supports DAX, uncompressed non-inlined files will be read directly, without going
	      through the page cache.  dax is a synonym for always.  Defaults to unset, which is equivalent to never.

       device=blobdev
	      Add extra device holding some of the data.  Must be given as many times and in the same order as --blobdev was to mkfs.erofs(1).

       domain_id=did
       fsid=id
	      Control CacheFiles on-demand read support.  To be documented.

VERSIONS
       erofs images are versioned through the use of feature flags; these are listed in the -E section of mkfs.erofs(1),

CONFIGURATION
       Linux must be configured with the CONFIG_EROFS_FS option to mount EROFS filesystems.  There are sub-configuration items that restrict the  availability
       of some of the parameters above.

SEE ALSO
       mkfs.erofs(1), fsck.erofs(1), dump.erofs(1)

       Documentation/filesystems/erofs.txt in the Linux source.

Linux man-pages 6.7							  2023-10-31								      erofs(5)
