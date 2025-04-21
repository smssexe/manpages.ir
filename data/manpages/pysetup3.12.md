PYSETUP3.3(1)								 User Commands								 PYSETUP3.3(1)

NAME
       pysetup3.3 - pysetup tool

SYNOPSIS
       pysetup [options] action [action_options]

DESCRIPTION
   Actions:
	      run:  Run one or several commands metadata: Display the metadata of a project install: Install a project remove: Remove a project search: Search
	      for a project in the indexes list: List installed projects graph: Display a graph create: Create a  project  generate-setup:  Generate  a	 back‐
	      ward-compatible setup.py

       To get more help on an action, use:

	      pysetup action --help

   Global options:
       --verbose (-v)
	      run verbosely (default)

       --quiet (-q)
	      run quietly (turns verbosity off)

       --dry-run (-n)
	      don't actually do anything

       --help (-h)
	      show detailed help message

       --no-user-cfg
	      ignore pydistutils.cfg in your home directory

       --version
	      Display the version

pysetup3.3 3.3								 January 2012								 PYSETUP3.3(1)
