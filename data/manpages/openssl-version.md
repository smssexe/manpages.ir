OPENSSL-VERSION(1SSL)							    OpenSSL							 OPENSSL-VERSION(1SSL)

NAME
       openssl-version - print OpenSSL version information

SYNOPSIS
       openssl version [-help] [-a] [-v] [-b] [-o] [-f] [-p] [-d] [-e] [-m] [-r] [-c]

DESCRIPTION
       This command is used to print out version information about OpenSSL.

OPTIONS
       -help
	   Print out a usage message.

       -a  All information, this is the same as setting all the other flags.

       -v  The current OpenSSL version.

       -b  The date the current version of OpenSSL was built.

       -o  Option information: various options set when the library was built.

       -f  Compilation flags.

       -p  Platform setting.

       -d  OPENSSLDIR setting.

       -e  ENGINESDIR settings.

       -m  MODULESDIR settings.

       -r  The random number generator source settings.

       -c  The OpenSSL CPU settings info.

NOTES
       The output of "openssl version -a" would typically be used when sending in a bug report.

COPYRIGHT
       Copyright 2000-2020 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							 OPENSSL-VERSION(1SSL)
