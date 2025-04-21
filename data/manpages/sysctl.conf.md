SYSCTL.CONF(5)								 File Formats								SYSCTL.CONF(5)

NAME
       sysctl.conf - sysctl preload/configuration file

DESCRIPTION
       sysctl.conf is a simple file containing sysctl values to be read in and set by sysctl.  The syntax is simply as follows:

	      # comment
	      ; comment

	      token = value

       Note  that blank lines are ignored, and whitespace before and after a token or value is ignored, although a value can contain whitespace within.	 Lines
       which begin with a # or ; are considered comments and ignored.

       If a line begins with a single -, any attempts to set the value that fail will be ignored.

NOTES
       As the /etc/sysctl.conf file is used to override default kernel parameter values, only a small number of parameters is predefined  in  the  file.   Use
       /sbin/sysctl -a or follow sysctl(8) to list all possible parameters. The description of individual parameters can be found in the kernel documentation.

       Maximum supported line length of the value is 4096 characters due to a limitation of /proc entries in Linux kernel.

EXAMPLE
	      # sysctl.conf sample
	      #
		kernel.domainname = example.com
	      ; this one has a space which will be written to the sysctl!
		kernel.modprobe = /sbin/mod probe

FILES
       /etc/sysctl.d/*.conf
       /run/sysctl.d/*.conf
       /usr/local/lib/sysctl.d/*.conf
       /usr/lib/sysctl.d/*.conf
       /lib/sysctl.d/*.conf
       /etc/sysctl.conf

       The paths where sysctl preload files usually exist.  See also sysctl option --system.

SEE ALSO
       sysctl(8)

AUTHOR
       George Staikos

REPORTING BUGS
       Please send bug reports to procps@freelists.org

procps-ng								  2021-09-15								SYSCTL.CONF(5)
