SBKEYSYNC(1)								 User Commands								  SBKEYSYNC(1)

NAME
       sbkeysync - UEFI secure boot key synchronization tool

SYNOPSIS
       sbkeysync [options]

DESCRIPTION
       Update EFI key databases from the filesystem

OPTIONS
       --efivars-path <dir>
	      Path to efivars mountpoint (or regular directory for testing)

       --verbose
	      Print verbose progress information

       --dry-run
	      Don't update firmware key databases

       --pk   Set PK

       --keystore <dir>
	      Read keys from <dir>/{db,dbx,KEK}/* (can be specified multiple times, first dir takes precedence)

       --no-default-keystores
	      Don't read keys from the default

	      keystore dirs

sbkeysync 0.9.4								  April 2024								  SBKEYSYNC(1)
