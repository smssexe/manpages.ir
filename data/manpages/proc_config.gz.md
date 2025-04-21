proc_config.gz(5)						      File Formats Manual						     proc_config.gz(5)

NAME
       /proc/config.gz - kernel build configuration

DESCRIPTION
       /proc/config.gz (since Linux 2.6)
	      This  file  exposes the configuration options that were used to build the currently running kernel, in the same format as they would be shown in
	      the .config file that resulted when configuring the kernel (using make xconfig, make config, or similar).	 The  file  contents  are  compressed;
	      view or search them using zcat(1) and zgrep(1).  As long as no changes have been made to the following file, the contents of /proc/config.gz are
	      the same as those provided by:

		  cat /lib/modules/$(uname -r)/build/.config

	      /proc/config.gz is provided only if the kernel is configured with CONFIG_IKCONFIG_PROC.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							     proc_config.gz(5)
