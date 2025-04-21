proc_filesystems(5)						      File Formats Manual						   proc_filesystems(5)

NAME
       /proc/filesystems - supported filesystems

DESCRIPTION
       /proc/filesystems
	      A text listing of the filesystems which are supported by the kernel, namely filesystems which were compiled into the kernel or whose kernel mod‐
	      ules  are currently loaded.  (See also filesystems(5).)  If a filesystem is marked with "nodev", this means that it does not require a block de‐
	      vice to be mounted (e.g., virtual filesystem, network filesystem).

	      Incidentally, this file may be used by mount(8) when no filesystem is specified and it didn't manage to determine	 the  filesystem  type.	  Then
	      filesystems contained in this file are tried (excepted those that are marked with "nodev").

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							   proc_filesystems(5)
