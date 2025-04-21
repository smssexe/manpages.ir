Basic classifier in tc(8)						     Linux						     Basic classifier in tc(8)

NAME
       basic - basic traffic control filter

SYNOPSIS
       tc filter ... basic [ match EMATCH_TREE ] [ action ACTION_SPEC ] [ classid CLASSID ]

DESCRIPTION
       The basic filter allows one to classify packets using the extended match infrastructure.

OPTIONS
       action ACTION_SPEC
	      Apply an action from the generic actions framework on matching packets.

       classid CLASSID
	      Push matching packets into the class identified by CLASSID.

       match EMATCH_TREE
	      Match packets using the extended match infrastructure. See tc-ematch(8) for a detailed description of the allowed syntax in EMATCH_TREE.

SEE ALSO
       tc(8), tc-ematch(8)

iproute2								  21 Oct 2015						     Basic classifier in tc(8)
