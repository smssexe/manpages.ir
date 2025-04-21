OPENSSL-PRIME(1SSL)							    OpenSSL							   OPENSSL-PRIME(1SSL)

NAME
       openssl-prime - compute prime numbers

SYNOPSIS
       openssl prime [-help] [-hex] [-generate] [-bits num] [-safe] [-provider name] [-provider-path path] [-propquery propq] [-checks num] [number ...]

DESCRIPTION
       This command checks if the specified numbers are prime.

       If no numbers are given on the command line, the -generate flag should be used to generate primes according to the requirements specified by the rest
       of the flags.

OPTIONS
       -help
	   Display an option summary.

       -hex
	   Generate hex output.

       -generate
	   Generate a prime number.

       -bits num
	   Generate a prime with num bits.

       -safe
	   When used with -generate, generates a "safe" prime. If the number generated is n, then check that "(n-1)/2" is also prime.

       -provider name
       -provider-path path
       -propquery propq
	   See "Provider Options" in openssl(1), provider(7), and property(7).

       -checks num
	   This parameter is ignored.

COPYRIGHT
       Copyright 2017-2020 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							   OPENSSL-PRIME(1SSL)
