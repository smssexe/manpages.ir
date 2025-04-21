SOS_HELP(1)							    General Commands Manual							   SOS_HELP(1)

NAME
       sos_help - get detailed help information on sos commands and components

SYNOPSIS
       sos help TOPIC

DESCRIPTION
       sos  help  is used to retrieve more detailed information on the various SoS commands and components than is directly available in either other manpages
       or --help output.

       This information could for example be investigating a specific plugin to learn more about its purpose, use case, collections, available plugin options,
       edge cases, and more.

       Most aspects of SoS' operation can be investigated this way - the top level functions such as  report, clean, and collect, as well as  constructs  that
       allow those functions to work; e.g. transports within sos collect that define how that function connects to remote nodes.

REQUIRED ARGUMENTS
       TOPIC

       The section or topic to retrieve detailed help information for. TOPIC takes the general
	      form of command.component.entity, with component and entity being optional.

       Top-level command help sections will often direct users to component sections which in turn may point to further entity subsections.

       Some of the more useful or interesting sections are listed below:

	   Topic		     Description

	   report		     The sos report command
	   report.plugins	     Information on what report plugins are
	   report.plugins.$plugin    Information on a specific plugin
	   clean or mask	     The sos clean|mask command
	   collect		     The sos collect command
	   collect.clusters	     How collect enumerates nodes in a cluster
	   policies		     How SoS behaves on different distributions

									Fri Nov 05 2021								   SOS_HELP(1)
