IP-SR(8)								     Linux								      IP-SR(8)

NAME
       ip-sr - IPv6 Segment Routing management

SYNOPSIS
       ip sr  { COMMAND | help }

       ip sr hmac show

       ip sr hmac set KEYID ALGO

       ip sr tunsrc show

       ip sr tunsrc set ADDRESS

DESCRIPTION
       The ip sr command is used to configure IPv6 Segment Routing (SRv6) internal parameters.

       Those parameters include the mapping between an HMAC key ID and its associated hashing algorithm and secret, and the IPv6 address to use as source for
       encapsulated packets.

       The ip sr hmac set command prompts for a passphrase that will be used as the HMAC secret for the corresponding key ID. A blank passphrase removes the
       mapping.	 The currently supported algorithms for ALGO are sha1 and sha256.

       If the tunnel source is set to the address :: (which is the default), then an address of the egress interface will be selected. As this operation may
       hinder performances, it is recommended to set a non-default address.

EXAMPLES
   Configure an HMAC mapping for key ID 42 and hashing algorithm SHA-256
       # ip sr hmac set 42 sha256

   Set the tunnel source address to 2001:db8::1
       # ip sr tunsrc set 2001:db8::1

SEE ALSO
       ip-route(8)

AUTHOR
       David Lebrun <david.lebrun@uclouvain.be>

iproute2								  14 Apr 2017								      IP-SR(8)
