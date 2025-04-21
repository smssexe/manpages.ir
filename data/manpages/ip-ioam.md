IP-IOAM(8)								     Linux								    IP-IOAM(8)

NAME
       ip-ioam - IPv6 In-situ OAM (IOAM)

SYNOPSIS
       ip ioam	{ COMMAND | help }

       ip ioam namespace show

       ip ioam namespace add ID	 [ data DATA32 ]  [ wide DATA64 ]

       ip ioam namespace del ID

       ip ioam schema show

       ip ioam schema add ID DATA

       ip ioam schema del ID

       ip ioam namespace set ID schema	{ ID | none }

DESCRIPTION
       The ip ioam command is used to configure IPv6 In-situ OAM (IOAM6) internal parameters, namely IOAM namespaces and schemas.

       Those parameters also include the mapping between an IOAM namespace and an IOAM schema.

EXAMPLES
   Configure an IOAM namespace (ID = 1) with both data (32 bits) and wide data (64 bits)
       # ip ioam namespace add 1 data 0xdeadbeef wide 0xcafec0caf00dc0de

   Link an existing IOAM schema (ID = 7) to an existing IOAM namespace (ID = 1)
       # ip ioam namespace set 1 schema 7

SEE ALSO
       ip-route(8)

AUTHOR
       Justin Iurman <justin.iurman@uliege.be>

iproute2								  05 Jul 2021								    IP-IOAM(8)
