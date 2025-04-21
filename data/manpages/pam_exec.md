PAM_EXEC(8)							       Linux-PAM Manual								   PAM_EXEC(8)

NAME
       pam_exec - PAM module which calls an external command

SYNOPSIS

       pam_exec.so [debug] [expose_authtok] [seteuid] [quiet] [quiet_log] [stdout] [log=file] [type=type] command [...]

DESCRIPTION
       pam_exec is a PAM module that can be used to run an external command.

       The child's environment is set to the current PAM environment list, as returned by pam_getenvlist(3) In addition, the following PAM items are exported
       as environment variables: PAM_RHOST, PAM_RUSER, PAM_SERVICE, PAM_TTY, PAM_USER and PAM_TYPE, which contains one of the module types: account, auth,
       password, open_session and close_session.

       Commands called by pam_exec need to be aware of that the user can have control over the environment.

OPTIONS
       debug
	   Print debug information.

       expose_authtok
	   During authentication the calling command can read the password from stdin(3). Only first PAM_MAX_RESP_SIZE bytes of a password are provided to the
	   command.

       log=file
	   The output of the command is appended to file

       type=type
	   Only run the command if the module type matches the given type.

       stdout
	   Per default the output of the executed command is written to /dev/null. With this option, the stdout output of the executed command is redirected
	   to the calling application. It's in the responsibility of this application what happens with the output. The log option is ignored.

       quiet
	   Per default pam_exec.so will echo the exit status of the external command if it fails. Specifying this option will suppress the message.

       quiet_log
	   Per default pam_exec.so will log the exit status of the external command if it fails. Specifying this option will suppress the log message.

       seteuid
	   Per default pam_exec.so will execute the external command with the real user ID of the calling process. Specifying this option means the command is
	   run with the effective user ID.

MODULE TYPES PROVIDED
       All module types (auth, account, password and session) are provided.

RETURN VALUES
       PAM_SUCCESS
	   The external command was run successfully.

       PAM_BUF_ERR
	   Memory buffer error.

       PAM_CONV_ERR
	   The conversation method supplied by the application failed to obtain the username.

       PAM_INCOMPLETE
	   The conversation method supplied by the application returned PAM_CONV_AGAIN.

       PAM_SERVICE_ERR
	   No argument or a wrong number of arguments were given.

       PAM_SYSTEM_ERR
	   A system error occurred or the command to execute failed.

       PAM_IGNORE
	   pam_setcred was called, which does not execute the command. Or, the value given for the type= parameter did not match the module type.

EXAMPLES
       Add the following line to /etc/pam.d/passwd to rebuild the NIS database after each local password change:

		   password optional pam_exec.so seteuid /usr/bin/make -C /var/yp

       This will execute the command

	   make -C /var/yp

       with effective user ID.

SEE ALSO
       pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_exec was written by Thorsten Kukuk <kukuk@thkukuk.de> and Josh Triplett <josh@joshtriplett.org>.

Linux-PAM								  05/07/2023								   PAM_EXEC(8)
