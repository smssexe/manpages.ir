OPENSSL-PASSWD(1SSL)							    OpenSSL							  OPENSSL-PASSWD(1SSL)

NAME
       openssl-passwd - compute password hashes

SYNOPSIS
       openssl passwd [-help] [-1] [-apr1] [-aixmd5] [-5] [-6] [-salt string] [-in file] [-stdin] [-noverify] [-quiet] [-table] [-reverse] [-rand files]
       [-writerand file] [-provider name] [-provider-path path] [-propquery propq] [password]

DESCRIPTION
       This command computes the hash of a password typed at run-time or the hash of each password in a list.  The password list is taken from the named file
       for option -in, from stdin for option -stdin, or from the command line, or from the terminal otherwise.

OPTIONS
       -help
	   Print out a usage message.

       -1  Use the MD5 based BSD password algorithm 1 (default).

       -apr1
	   Use the apr1 algorithm (Apache variant of the BSD algorithm).

       -aixmd5
	   Use the AIX MD5 algorithm (AIX variant of the BSD algorithm).

       -5
       -6  Use the SHA256 / SHA512 based algorithms defined by Ulrich Drepper.	See <https://www.akkadia.org/drepper/SHA-crypt.txt>.

       -salt string
	   Use the specified salt.  When reading a password from the terminal, this implies -noverify.

       -in file
	   Read passwords from file.

       -stdin
	   Read passwords from stdin.

       -noverify
	   Don't verify when reading a password from the terminal.

       -quiet
	   Don't output warnings when passwords given at the command line are truncated.

       -table
	   In the output list, prepend the cleartext password and a TAB character to each password hash.

       -reverse
	   When the -table option is used, reverse the order of cleartext and hash.

       -rand files, -writerand file
	   See "Random State Options" in openssl(1) for details.

       -provider name
       -provider-path path
       -propquery propq
	   See "Provider Options" in openssl(1), provider(7), and property(7).

EXAMPLES
	 % openssl passwd -1 -salt xxxxxxxx password
	 $1$xxxxxxxx$UYCIxa628.9qXjpQCjM4a.

	 % openssl passwd -apr1 -salt xxxxxxxx password
	 $apr1$xxxxxxxx$dxHfLAsjHkDRmG83UXe8K0

	 % openssl passwd -aixmd5 -salt xxxxxxxx password
	 xxxxxxxx$8Oaipk/GPKhC64w/YVeFD/

HISTORY
       The -crypt option was removed in OpenSSL 3.0.

COPYRIGHT
       Copyright 2000-2021 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							  OPENSSL-PASSWD(1SSL)
