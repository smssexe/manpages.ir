LIBAUDIT.CONF(5)						System Administration Utilities						      LIBAUDIT.CONF(5)

NAME
       libaudit.conf - libaudit configuration file

DESCRIPTION
       The  file /etc/libaudit.conf contains configuration information for user space applications that link to libaudit. The applications are responsible for
       querying the settings in this file and obeying the admin's preferences. This file contains one configuration keyword per line, an equal sign, and  then
       followed by appropriate configuration information. The keywords recognized are: failure_action.	These keywords are described below.

       failure_action
	      This  keyword specifies what action the admin wishes a user space application to take when there is a failure to send an audit event to the ker‐
	      nel. The possible values are: IGNORE
	       - meaning do nothing, LOG - write to syslog the inability to send an audit event, and TERMINATE - the user space application should exit.

SEE ALSO
       get_auditfail_action(3).

AUTHOR
       Steve Grubb

Red Hat									   Oct 2009							      LIBAUDIT.CONF(5)
