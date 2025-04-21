PAM_ECHO(8)							       Linux-PAM Manual								   PAM_ECHO(8)

NAME
       pam_echo - PAM module for printing text messages

SYNOPSIS

       pam_echo.so [file=/path/message]

DESCRIPTION
       The pam_echo PAM module is for printing text messages to inform user about special things. Sequences starting with the % character are interpreted in
       the following way:

       %H
	   The name of the remote host (PAM_RHOST).

       %h
	   The name of the local host.

       %s
	   The service name (PAM_SERVICE).

       %t
	   The name of the controlling terminal (PAM_TTY).

       %U
	   The remote user name (PAM_RUSER).

       %u
	   The local user name (PAM_USER).

       All other sequences beginning with % expands to the characters following the % character.

OPTIONS
       file=/path/message
	   The content of the file /path/message will be printed with the PAM conversion function as PAM_TEXT_INFO.

MODULE TYPES PROVIDED
       All module types (auth, account, password and session) are provided.

RETURN VALUES
       PAM_BUF_ERR
	   Memory buffer error.

       PAM_SUCCESS
	   Message was successful printed.

       PAM_IGNORE
	   PAM_SILENT flag was given or message file does not exist, no message printed.

EXAMPLES
       For an example of the use of this module, we show how it may be used to print information about good passwords:

	   password optional pam_echo.so file=/usr/share/doc/good-password.txt
	   password required pam_unix.so

SEE ALSO
       pam.conf(8), pam.d(5), pam(7)

AUTHOR
       Thorsten Kukuk <kukuk@thkukuk.de>

Linux-PAM								  05/07/2023								   PAM_ECHO(8)
