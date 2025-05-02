#!/bin/bash

output_dir="all_man_pages_md"
log_file="$output_dir/errors.log"

mkdir -p "$output_dir"
> "$log_file"

echo "[*] Extracting all man pages..."

man -k . | awk '{print $1 "|" $2}' | sort -u | while IFS="|" read -r name section; do
    clean_section=$(echo "$section" | tr -d '()')
    section_dir="$output_dir/man$clean_section"
    mkdir -p "$section_dir"
    output_file="$section_dir/$name.md"

    echo "[+] Saving $name (section $clean_section)..."

    if man "$clean_section" "$name" > /dev/null 2>&1; then
        {
            echo "# $name (man $clean_section)"
            echo
            man "$clean_section" "$name" | col -b
        } > "$output_file"
    else
        echo "$name ($clean_section)" >> "$log_file"
        echo "[!] Failed to process $name ($clean_section)" >&2
    fi
done

echo "[✓] Done. Markdown files saved in '$output_dir'"
echo "[i] Errors (if any) logged in '$log_file'"
