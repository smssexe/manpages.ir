GIT-UPDATE-SERVER-INFO(1)						  Git Manual						     GIT-UPDATE-SERVER-INFO(1)

NAME
       git-update-server-info - Update auxiliary info file to help dumb servers

SYNOPSIS
       git update-server-info [-f | --force]

DESCRIPTION
       A dumb server that does not do on-the-fly pack generations must have some auxiliary information files in $GIT_DIR/info and $GIT_OBJECT_DIRECTORY/info
       directories to help clients discover what references and packs the server has. This command generates such auxiliary files.

OPTIONS
       -f, --force
	   Update the info files from scratch.

OUTPUT
       Currently the command updates the following files. Please see gitrepository-layout(5) for a description of what they are for:

       •   objects/info/packs

       •   info/refs

GIT
       Part of the git(1) suite

Git 2.43.0								  01/13/2025						     GIT-UPDATE-SERVER-INFO(1)
