DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-push - Upload an image to a registry

SYNOPSIS
       docker push [OPTIONS] NAME[:TAG]

DESCRIPTION
       Alias for docker image push.

OPTIONS
       -a, --all-tags[=false]	   Push all tags of an image to the repository

       --disable-content-trust[=true]	   Skip image signing

       -h, --help[=false]      help for push

       --platform=""	  Push a platform-specific manifest as a single-platform image to the registry.	 Image index won't be pushed, meaning that other mani‐
       fests, including attestations won't be preserved.  'os[/arch[/variant]]': Explicit platform (eg. linux/amd64)

       -q, --quiet[=false]	Suppress verbose output

SEE ALSO
       docker(1)

Docker Community							   Mar 2025								     DOCKER(1)
