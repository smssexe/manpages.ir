GPG-WKS-CLIENT(1)						     GNU Privacy Guard 2.4						     GPG-WKS-CLIENT(1)

NAME
       gpg-wks-client - Client for the Web Key Service

SYNOPSIS
       gpg-wks-client [options] --supported user-id
       gpg-wks-client [options] --check user-id
       gpg-wks-client [options] --create fingerprint user-id
       gpg-wks-client [options] --receive
       gpg-wks-client [options] --read
       gpg-wks-client [options] --mirror
       gpg-wks-client [options] --install-key
       gpg-wks-client [options] --remove-key
       gpg-wks-client [options] --print-wkd-hash
       gpg-wks-client [options] --print-wkd-url

DESCRIPTION
       The gpg-wks-client is used to send requests to a Web Key Service provider.  This is usually done to upload a key into a Web Key Directory.

       With the --supported command the caller can test whether a site supports the Web Key Service.  The argument is an arbitrary address in the to be tested
       domain.	For  example  ‘foo@example.net’.  The command returns success if the Web Key Service is supported.  The operation is silent; to get diagnostic
       output use the option --verbose.	 See option --with-colons for a variant of this command.

       With the --check command the caller can test whether a key exists for a supplied mail address.  The command returns success if a key is available.

       The --create command is used to send a request for publication in the Web Key Directory.	 The arguments are the fingerprint of the key and the user  id
       to publish.  The output from the command is a properly formatted mail with all standard headers.	 This mail can be fed to sendmail(8) or any other tool
       to actually send that mail.  If sendmail(8) is installed the option --send can be used to directly send the created request.  If the provider request a
       'mailbox-only' user id and no such user id is found, gpg-wks-client will try an additional user id.

       The  --receive and --read commands are used to process confirmation mails as send from the service provider.  The former expects an encrypted MIME mes‐
       sages, the latter an already decrypted MIME message.  The result of these commands are another mail which can be send in the same way as the mail  cre‐
       ated with --create.

       The  command  --install-key manually installs a key into a local directory (see option -C) reflecting the structure of a WKD.  The arguments are a file
       with the keyblock and the user-id to install.  If the first argument resembles a fingerprint the key is taken from the current keyring;	to  force  the
       use  of	a file, prefix the first argument with "./".  If no arguments are given the parameters are read from stdin; the expected format are lines with
       the fingerprint and the mailbox separated by a space.  The command --remove-key removes a key from that directory, its only argument is a user-id.

       The command --mirror is similar to --install-key but takes the keys from the the LDAP server configured for Dirmngr.  If no  arguments  are  given  all
       keys  and user ids are installed.  If arguments are given they are taken as domain names to limit the to be installed keys.  The option --blacklist may
       be used to further limit the to be installed keys.

       The command --print-wkd-hash prints the WKD user-id identifiers and the corresponding mailboxes from the user-ids given on  the	command	 line  or  via
       stdin (one user-id per line).

       The  command --print-wkd-url prints the URLs used to fetch the key for the given user-ids from WKD.  The meanwhile preferred format with sub-domains is
       used here.

OPTIONS
       gpg-wks-client understands these options:

       --send Directly send created mails using the sendmail command.  Requires installation of that command.

       --with-colons
	      This option has currently only an effect on the --supported command.  If it is used all arguments on the command line are taken as domain	 names
	      and  tested  for WKD support.  The output format is one line per domain with colon delimited fields.  The currently specified fields are (future
	      versions may specify additional fields):

	      1 - domain
		     This is the domain name.  Although quoting is not required for valid domain names this field is specified to be quoted in standard C man‐
		     ner.

	      2 - WKD
		     If the value is true the domain supports the Web Key Directory.

	      3 - WKS
		     If the value is true the domain supports the Web Key Service protocol to upload keys to the directory.

	      4 - error-code
		     This may contain an gpg-error code to describe certain failures.  Use ‘gpg-error CODE’ to explain the code.

	      5 - protocol-version
		     The minimum protocol version supported by the server.

	      6 - auth-submit
		     The auth-submit flag from the policy file of the server.

	      7 - mailbox-only
		     The mailbox-only flag from the policy file of the server.

       --output file
       -o     Write the created mail to file instead of stdout.	 Note that the value - for file is the same as writing to stdout.  If this option is used with
	      the --check command and a key was found it is written to the given file.

       --status-fd n
	      Write special status strings to the file descriptor n.  This program returns only the status messages SUCCESS or FAILURE which are helpful  when
	      the caller uses a double fork approach and can't easily get the return code of the process.

       -C dir
       --directory dir
	      Use dir as top level directory for the commands --mirror, --install-key and --remove-key.	 The default is ‘openpgpkey’.

       --blacklist file
	      This  option is used to exclude certain mail addresses from a mirror operation.  The format of file is one mail address (just the addrspec, e.g.
	      "postel@isi.edu") per line.  Empty lines and lines starting with a '#' are ignored.

       --add-revocs
       --no-add-revocs
	      If enabled append revocation certificates for the same addrspec as used in the WKD to the key.  Modern gpg version are able to import and	 apply
	      them  for	 existing keys.	 Note that when used with the --mirror command the revocation are searched in the local keyring and not in an LDAP di‐
	      rectory.	The default is --add-revocs.

       --verbose
	      Enable extra informational output.

       --quiet
	      Disable almost all informational output.

       --version
	      Print version of the program and exit.

       --help Display a brief help page and exit.

EXAMPLES
       To use the services with clients lacking integrated support, the mailcap mechanism can be used.	Simply put:
	 application/vnd.gnupg.wks; \
	   /usr/bin/gpg-wks-client -v --read --send; \
	   needsterminal; \
	   description=WKS message
       into the ‘/etc/mailcap’.	 This assumes that a /usr/lib/sendmail is installed.  With this configuration any real mail programs will  run	gpg-wks-client
       for messages received from a Web Key Service.

SEE ALSO
       gpg-wks-server(1)

GnuPG 2.4.4								  2024-01-25							     GPG-WKS-CLIENT(1)
