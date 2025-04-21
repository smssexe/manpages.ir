libsasl(5)																	    libsasl(5)

NAME
       libsasl - authentication library

SYNOPSIS
       Cyrus SASL library handling communication between an application and the Cyrus SASL authentication framework.

Description
       This document describes generic configuration options for the Cyrus SASL authentication library libsasl.

       The  library  handles  communication  between  an application and the Cyrus SASL authentication framework. Both exchange information before libsasl can
       start offering authentication services for the application.

       The application, among other data, sends the service_name. The service name is the services name as specified by IANA. SMTP servers, for example,  send
       smtp as service_name. This information is handed over by libsasl e.g. when Kerberos or PAM authentication takes place.

       Configuration options in general are read either from a file or passed by the application using libsasl during library initialization.

File-Based configuration
       When  an	 application  (server) starts, it initializes the libsasl library. The application passes app_name (application name) to the SASL library. Its
       value is used to construct the name of the application specific SASL configuration file. The Cyrus SASL sample-server, for  example,  sends  sample  as
       app_name.  Using this value the SASL library will search the configuration directories for a file named sample.conf and read configuration options from
       it.
	      Note

	      Consult the applications manual to determine what app_name it sends to the Cyrus SASL library.

Application-Based Configuration
       Configuration options for libsasl are written down together with application specific options in the applications configuration file.  The  application
       reads them and passes them over to libsasl when it loads the library.
	      Note

	      An  example  for	application-based  configuration is the Cyrus IMAP server imapd. SASL configuration is written to imapd.conf and passed to the
	      SASL library when the imapd server starts.

Configuration Syntax
       The general format of Cyrus SASL configuration file is as follows:

       Configuration options
	      Configuration options are written each on a single physical line. Parameter and value must be separated by a colon and a single whitespace:

	      parameter: value
	      Important

	      There must be no trailing whitespace after the value or Cyrus SASL will fail to apply the value appropriately!

       Comments, Empty lines and whitespace-only lines
	      Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a ‘#’.

Options
       There are generic options and options specific to the password verification service or auxiliary property plugin chosen by the administrator. Such spe‐
       cific options are documented in manuals listed in libsasl(5).

       The following configuration parameters are generic configuration options:

       authdaemond_path (default: /dev/null)
	      Path to Courier MTA authdaemond's unix socket. Only applicable when pwcheck_method is set to authdaemond.

       auto_transition: (default: no)
	      Automatically transition users to other mechanisms when they do a successful plaintext authentication and if an auxprop plugin is used.
	      Important

	      This option does not apply to the ldapdb(5) plugin. It is a read-only plugin.

	      no     Do not transition users to other mechanisms.

	      noplain
		     Transition users to other mechanisms, but write non-plaintext secrets only.

	      yes    Transition users to other mechanisms.
	      Note

	      The only mechanisms (as currently implemented) which don't use plaintext secrets are OTP and SRP.

       auxprop_plugin: (default: empty)
	      A whitespace-separated list of one or more auxiliary plugins used if the pwcheck_method parameter specifies auxprop as an option.	 Plugins  will
	      be queried in list order. If no plugin is specified, all available plugins will be queried.

	      ldapdb Specify ldapdb to use the Cyrus SASL ldapdb(5) plugin.

	      sasldb Specify sasldb to use the Cyrus SASL sasldb(5) plugin.

	      sql    Specify sql to use the Cyrus SASL sql(5) plugin.

       log_level: (default: 1)
	      Specifies a numeric log level. Available log levels are:

	      0	     Don't log anything

	      1	     Log unusual errors

	      2	     Log all authentication failures

	      3	     Log non-fatal warnings

	      4	     More verbose than 3

	      5	     More verbose than 4

	      6	     Traces of internal protocols

	      7	     Traces of internal protocols, including passwords
	      Important

	      Cyrus  SASL sends log messages to the application that runs it. The application decides if it forwards such messages to the sysklogd(8) service,
	      to which facility they are sent and which priority is given to the message.

       mech_list: (default: empty)
	      The optional mech_list parameter specifies a whitespace-separated list of one or more mechanisms allowed for authentication.

       pwcheck_method: (default: auxprop)
	      A whitespace-separated list of one or more mechanisms. Cyrus SASL provides the following mechanisms:

	      authdaemond
		     Configures Cyrus SASL to contact the Courier MTA authdaemond(8) password verification service for password verification.

	      alwaystrue
		     Lets the pwcheck succeed always.

	      auxprop
		     Cyrus SASL will use its own plugin infrastructure to verify passwords. The auxprop_plugin parameter controls which plugins will be used.

	      pwcheck
		     Verify passwords using the Cyrus SASL pwcheck(8) password verification service. The pwcheck daemon is considered  deprecated  and	should
		     not be used anymore. Use the saslauthd password verification service instead.

	      saslauthd
		     Verify passwords using the Cyrus SASL saslauthd(8) password verification service.

       saslauthd_path: (default: empty)
	      Path to saslauthd(8) run directory (including the /mux named pipe)

See also
       authdaemond(5), ldapdb(5), libsasl(5), saslauthd(8), saslauthd.conf(5), saslpasswd2(5), sasldblistusers2(5), sasldb(5), sql(5)

Author
       This  manual  was  written  for	the Debian distribution because the original program does not have a manual page. Parts of the documentation have been
       taken from the Cyrus SASL's options.html.

	      Patrick Ben Koetter
	      <p@state-of-mind.de>

									 15 April 2022								    libsasl(5)
