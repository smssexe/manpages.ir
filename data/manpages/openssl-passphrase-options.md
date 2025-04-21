OPENSSL-PASSPHRASE-OPTIONS(1SSL)					    OpenSSL					      OPENSSL-PASSPHRASE-OPTIONS(1SSL)

NAME
       openssl-passphrase-options - Pass phrase options

SYNOPSIS
       openssl command [ options ... ] [ parameters ... ]

DESCRIPTION
       Several OpenSSL commands accept password arguments, typically using -passin and -passout for input and output passwords respectively. These allow the
       password to be obtained from a variety of sources. Both of these options take a single argument whose format is described below. If no password
       argument is given and a password is required then the user is prompted to enter one: this will typically be read from the current terminal with echoing
       turned off.

       Note that character encoding may be relevant, please see passphrase-encoding(7).

OPTIONS
   Pass Phrase Option Arguments
       Pass phrase arguments can be formatted as follows.

       pass:password
	   The	actual password is password. Since the password is visible to utilities (like 'ps' under Unix) this form should only be used where security is
	   not important.

       env:var
	   Obtain the password from the environment variable var. Since the environment of other processes is visible on  certain  platforms  (e.g.  ps	 under
	   certain Unix OSes) this option should be used with caution.

       file:pathname
	   The first line of pathname is the password. If the same pathname argument is supplied to -passin and -passout arguments then the first line will be
	   used	 for  the input password and the next line for the output password. pathname need not refer to a regular file: it could for example refer to a
	   device or named pipe.

       fd:number
	   Read the password from the file descriptor number. This can be used to send the data via a pipe for example.

       stdin
	   Read the password from standard input.

COPYRIGHT
       Copyright 2000-2020 The OpenSSL Project Authors. All Rights Reserved.

       Licensed under the Apache License 2.0 (the "License").  You may not use this file except in compliance with the License.	 You can obtain a copy in  the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05					      OPENSSL-PASSPHRASE-OPTIONS(1SSL)
