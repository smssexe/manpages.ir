OPENSSL-LIST(1SSL)							    OpenSSL							    OPENSSL-LIST(1SSL)

NAME
       openssl-list - list algorithms and features

SYNOPSIS
       openssl list [-help] [-verbose] [-select name] [-1] [-commands] [-standard-commands] [-digest-algorithms] [-digest-commands] [-kdf-algorithms]
       [-mac-algorithms] [-random-instances] [-random-generators] [-cipher-algorithms] [-cipher-commands] [-encoders] [-decoders] [-key-managers]
       [-key-exchange-algorithms] [-kem-algorithms] [-signature-algorithms] [-asymcipher-algorithms] [-public-key-algorithms] [-public-key-methods]
       [-store-loaders] [-providers] [-engines] [-disabled] [-objects] [-options command] [-provider name] [-provider-path path] [-propquery propq]

DESCRIPTION
       This command is used to generate list of algorithms or disabled features.

OPTIONS
       -help
	   Display a usage message.

       -verbose
	   Displays extra information.	The options below where verbosity applies say a bit more about what that means.

       -select name
	   Only list algorithms that match this name.

       -1  List the commands, digest-commands, or cipher-commands in a single column.  If used, this option must be given first.

       -commands
	   Display a list of standard commands.

       -standard-commands
	   List of standard commands.

       -digest-commands
	   This option is deprecated. Use digest-algorithms instead.

	   Display a list of message digest commands, which are typically used as input to the openssl-dgst(1) or openssl-speed(1) commands.

       -cipher-commands
	   This option is deprecated. Use cipher-algorithms instead.

	   Display a list of cipher commands, which are typically used as input to the openssl-enc(1) or openssl-speed(1) commands.

       -cipher-algorithms, -digest-algorithms, -kdf-algorithms, -mac-algorithms,
	   Display a list of symmetric cipher, digest, kdf and mac algorithms.	See "Display of algorithm names" for a description of how names are displayed.

	   In verbose mode, the algorithms provided by a provider will get additional information on what parameters each implementation supports.

       -random-instances
	   List the primary, public and private random number generator details.

       -random-generators
	   Display a list of random number generators.	See "Display of algorithm names" for a description of how names are displayed.

       -encoders
	   Display a list of encoders.	See "Display of algorithm names" for a description of how names are displayed.

	   In verbose mode, the algorithms provided by a provider will get additional information on what parameters each implementation supports.

       -decoders
	   Display a list of decoders.	See "Display of algorithm names" for a description of how names are displayed.

	   In verbose mode, the algorithms provided by a provider will get additional information on what parameters each implementation supports.

       -public-key-algorithms
	   Display  a  list  of	 public	 key  algorithms,  with each algorithm as a block of multiple lines, all but the first are indented.  The options key-
	   exchange-algorithms, kem-algorithms, signature-algorithms, and asymcipher-algorithms will display similar info.

       -public-key-methods
	   Display a list of public key methods.

       -key-managers
	   Display a list of key managers.

       -key-exchange-algorithms
	   Display a list of key exchange algorithms.

       -kem-algorithms
	   Display a list of key encapsulation algorithms.

       -signature-algorithms
	   Display a list of signature algorithms.

       -asymcipher-algorithms
	   Display a list of asymmetric cipher algorithms.

       -store-loaders
	   Display a list of store loaders.

       -providers
	   Display a list of all loaded providers with their names, version and status.

	   In verbose mode, the full version and all provider parameters will additionally be displayed.

       -engines
	   This option is deprecated.

	   Display a list of loaded engines.

       -disabled
	   Display a list of disabled features, those that were compiled out of the installation.

       -objects
	   Display a list of built in objects, i.e. OIDs with names.  They're listed in	 the  format  described	 in  "ASN1  Object  Configuration  Module"  in
	   config(5).

       -options command
	   Output  a  two-column  list	of  the	 options  accepted  by the specified command.  The first is the option name, and the second is a one-character
	   indication of what type of parameter it takes, if any.  This is an internal option, used for checking that the documentation is complete.

       -provider name
       -provider-path path
       -propquery propq
	   See "Provider Options" in openssl(1), provider(7), and property(7).

   Display of algorithm names
       Algorithm names may be displayed in one of two manners:

       Legacy implementations
	   Legacy implementations will simply display the main name of the algorithm on a line of its own, or in the form "<foo " bar>> to show that "foo"  is
	   an alias for the main name, "bar"

       Provided implementations
	   Implementations from a provider are displayed like this if the implementation is labeled with a single name:

	    foo @ bar

	   or like this if it's labeled with multiple names:

	    { foo1, foo2 } @bar

	   In both cases, "bar" is the name of the provider.

HISTORY
       The -engines, -digest-commands, and -cipher-commands options were deprecated in OpenSSL 3.0.

COPYRIGHT
       Copyright 2016-2022 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							    OPENSSL-LIST(1SSL)
