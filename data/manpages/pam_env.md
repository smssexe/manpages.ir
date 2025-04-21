PAM_ENV(8)							       Linux-PAM Manual								    PAM_ENV(8)

NAME
       pam_env - PAM module to set/unset environment variables

SYNOPSIS

       pam_env.so [debug] [conffile=conf-file] [envfile=env-file] [readenv=0|1] [user_envfile=env-file] [user_readenv=0|1]

DESCRIPTION
       The pam_env PAM module allows the (un)setting of environment variables. Supported is the use of previously set environment variables as well as
       PAM_ITEMs such as PAM_RHOST.

       By default rules for (un)setting of variables are taken from the config file /etc/security/pam_env.conf. An alternate file can be specified with the
       conffile option.

       Second a file (/etc/environment by default) with simple KEY=VAL pairs on separate lines will be read. With the envfile option an alternate file can be
       specified. And with the readenv option this can be completely disabled.

       Third it will read a user configuration file ($HOME/.pam_environment by default). The default file can be changed with the user_envfile option and it
       can be turned on and off with the user_readenv option.

       Since setting of PAM environment variables can have side effects to other modules, this module should be the last one on the stack.

OPTIONS
       conffile=/path/to/pam_env.conf
	   Indicate an alternative pam_env.conf style configuration file to override the default. This can be useful when different services need different
	   environments.

       debug
	   A lot of debug information is printed with syslog(3).

       envfile=/path/to/environment
	   Indicate an alternative environment file to override the default. The syntax are simple KEY=VAL pairs on separate lines. The export instruction can
	   be specified for bash compatibility, but will be ignored. This can be useful when different services need different environments.

       readenv=0|1
	   Turns on or off the reading of the file specified by envfile (0 is off, 1 is on). By default this option is on.

       user_envfile=filename
	   Indicate an alternative .pam_environment file to override the default.The syntax is the same as for /etc/security/pam_env.conf. The filename is
	   relative to the user home directory. This can be useful when different services need different environments.

       user_readenv=0|1
	   Turns on or off the reading of the user specific environment file. 0 is off, 1 is on. By default this option is off as user supplied environment
	   variables in the PAM environment could affect behavior of subsequent modules in the stack without the consent of the system administrator.

	   Due to problematic security this functionality is deprecated since the 1.5.0 version and will be removed completely at some point in the future.

MODULE TYPES PROVIDED
       The auth and session module types are provided.

RETURN VALUES
       PAM_ABORT
	   Not all relevant data or options could be gotten.

       PAM_BUF_ERR
	   Memory buffer error.

       PAM_IGNORE
	   No pam_env.conf and environment file was found.

       PAM_SUCCESS
	   Environment variables were set.

FILES
       /etc/security/pam_env.conf
	   Default configuration file

       /etc/environment
	   Default environment file

       $HOME/.pam_environment
	   User specific environment file

SEE ALSO
       pam_env.conf(5), pam.d(5), pam(7), environ(7).

AUTHOR
       pam_env was written by Dave Kinchlea <kinch@kinch.ark.com>.

Linux-PAM								  09/13/2023								    PAM_ENV(8)
