OPENSSL-INFO(1SSL)							    OpenSSL							    OPENSSL-INFO(1SSL)

NAME
       openssl-info - print OpenSSL built-in information

SYNOPSIS
       openssl info [-help] [-configdir] [-enginesdir] [-modulesdir ] [-dsoext] [-dirnamesep] [-listsep] [-seeds] [-cpusettings]

DESCRIPTION
       This command is used to print out information about OpenSSL.  The information is written exactly as it is with no extra text, which makes useful for
       scripts.

       As a consequence, only one item may be chosen for each run of this command.

OPTIONS
       -help
	   Print out a usage message.

       -configdir
	   Outputs the default directory for OpenSSL configuration files.

       -enginesdir
	   Outputs the default directory for OpenSSL engine modules.

       -modulesdir
	   Outputs the default directory for OpenSSL dynamically loadable modules other than engine modules.

       -dsoext
	   Outputs the DSO extension OpenSSL uses.

       -dirnamesep
	   Outputs the separator character between a directory specification and a filename.  Note that on some operating systems, this is not the same as the
	   separator between directory elements.

       -listsep
	   Outputs the OpenSSL list separator character.  This is typically used to construct $PATH ("%PATH%" on Windows) style lists.

       -seeds
	   Outputs the randomness seed sources.

       -cpusettings
	   Outputs the OpenSSL CPU settings info.

HISTORY
       This command was added in OpenSSL 3.0.

COPYRIGHT
       Copyright 2019-2020 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							    OPENSSL-INFO(1SSL)
