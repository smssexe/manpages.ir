UPDATE-CA-CERTIFICATES(8)					    System Manager's Manual					     UPDATE-CA-CERTIFICATES(8)

NAME
       update-ca-certificates - update /etc/ssl/certs and ca-certificates.crt

SYNOPSIS
       update-ca-certificates [options]

DESCRIPTION
       This manual page documents briefly the update-ca-certificates command.

       update-ca-certificates  is  a program that manages the collection of TLS certificates for the local machine and generates ca-certificates.crt.  ca-cer‐
       tificates.crt is a single-file of concatenated certificates.  The collection of individual certificates is stored at /etc/ssl/certs.

       The program reads the configuration file /etc/ca-certificates.conf. Each line gives a pathname of a  CA	certificate  under  /usr/share/ca-certificates
       that  should be trusted. Lines that begin with "#" are comment lines and thus ignored.  Lines that begin with "!" are deselected, causing the deactiva‐
       tion of the CA certificate in question.

       Certificates must be in PEM format and have a .crt extension in order to be included by update-ca-certificates. Furthermore, all	 certificates  with  a
       .crt extension found below /usr/local/share/ca-certificates are also included and implicitly trusted.

       To add one or more certificates to the machine, copy the certificates in PEM format with the *.crt extension to /usr/local/share/ca-certificates. There
       should  be one certificate per file, and not multiple certificates in a single file. Then run update-ca-certificates to merge the new certificates into
       the existing machine store at /etc/ssl/certs.

       Before terminating, update-ca-certificates invokes run-parts on /etc/ca-certificates/update.d and calls each hook with a list  of  certificates:	 those
       added are prefixed with a +, those removed are prefixed with a -.

OPTIONS
       A summary of options is included below.

       -h, --help
	      Show summary of options.

       -v, --verbose
	      Be verbose. Output openssl rehash.

       -f, --fresh
	      Fresh updates.  Remove symlinks in /etc/ssl/certs directory.

       --certsconf
	      Change the configuration file. By default, the file /etc/ca-certificates.conf is used.

       --certsdir
	      Change the certificate directory. By default, the directory /usr/share/ca-certificates is used.

       --localcertsdir
	      Change the local certificate directory. By default, the directory /usr/local/share/ca-certificates is used.

       --etccertsdir
	      Change the /etc certificate directory. By default, the directory /etc/ssl/certs is used.

       FILES

       /etc/ca-certificates.conf
	      A configuration file.

       /etc/ssl/certs/ca-certificates.crt
	      A single-file version of CA certificates. This holds all CA certificates that were activated in /etc/ca-certificates.conf.

       /usr/share/ca-certificates
	      Directory of CA certificates provided by the distribution.

       /usr/local/share/ca-certificates
	      Directory of local CA certificates, with .crt extension, provided by the user.

SEE ALSO
       openssl(1)

AUTHOR
       This manual page was written by Fumitoshi UKAI <ukai@debian.or.jp>, for the Debian project (but may be used by others).

									 20 April 2003						     UPDATE-CA-CERTIFICATES(8)
