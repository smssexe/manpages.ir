make-bcache(8)							    System Manager's Manual							make-bcache(8)

NAME
       make-bcache - create a cache device

SYNOPSIS
       make-bcache [ -U UUID ] [ -b bucket-size ] device

OPTIONS
       -C     Create a cache

       -B     Create a backing device (kernel functionality not yet implemented)

       -U UUID
	      Create a cache device with the specified UUID

       -b bucket-size
	      Specifies	 the  bucket size. Allocation is done in terms of buckets, and cache hits are counted per bucket; thus a smaller bucket size will give
	      better cache utilization, but poorer write performance. The bucket size is intended to be equal to the size of your SSD's	 erase	blocks,	 which
	      seems to be 128k-512k for most SSDs. Must be a power of two; accepts human readable units. Defaults to 128k.

																		make-bcache(8)
