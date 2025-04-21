#!/bin/bash

OUTPUT_DIR="data/manpages"
mkdir -p "$OUTPUT_DIR"

# Get all man pages list
for cmd in $(man -k . | awk '{print $1}' | sort -u); do
    # Create name of files
    safe_name=$(echo "$cmd" | tr '/' '_')

    #Get man without format
    if man "$cmd" > /dev/null 2>&1; then
        man "$cmd" | col -b > "$OUTPUT_DIR/${safe_name}.md"
        echo "Extracted: $cmd"
    fi
done
