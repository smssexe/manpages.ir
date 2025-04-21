Traffic control index filter(8)						     Linux					       Traffic control index filter(8)

NAME
       tcindex - traffic control index filter

SYNOPSIS
       tc filter ... tcindex [ hash SIZE ] [ mask MASK ] [ shift SHIFT ] [ pass_on | fall_through ] [ classid CLASSID ] [ action ACTION_SPEC ]

DESCRIPTION
       This filter allows one to match packets based on their tcindex field value, i.e. the combination of the DSCP and ECN fields as present in IPv4 and IPv6
       headers.

OPTIONS
       action ACTION_SPEC
	      Apply an action from the generic actions framework on matching packets.

       classid CLASSID
	      Push matching packets into the class identified by CLASSID.

       hash SIZE
	      Hash table size in entries to use. Defaults to 64.

       mask MASK
	      An optional bitmask to binary AND to the packet's tcindex field before use.

       shift SHIFT
	      The number of bits to right-shift a packet's tcindex value before use. If a mask has been set, masking is done before shifting.

       pass_on
	      If this flag is set, failure to find a class for the resulting ID will make the filter fail and lead to the next filter being consulted.

       fall_through
	      This  is	the opposite of pass_on and the default. The filter will classify the packet even if there is no class present for the resulting class
	      ID.

SEE ALSO
       tc(8)

iproute2								  21 Oct 2015					       Traffic control index filter(8)
