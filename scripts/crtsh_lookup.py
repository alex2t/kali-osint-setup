#!/usr/bin/env python3
"""Query crt.sh for subdomains related to a given domain.

This script fetches certificate transparency entries from the free crt.sh
service and extracts unique subdomains for the target domain.
"""

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request


def fetch_crtsh(domain: str) -> list[dict]:
    """Fetch records from crt.sh for the given domain and return JSON data."""
    query = urllib.parse.quote(f"%25{domain}")
    url = f"https://crt.sh/?q={query}&output=json"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        data = response.read().decode(charset)
        return json.loads(data)


def extract_subdomains(records: list[dict], domain: str) -> list[str]:
    """Extract unique subdomains from crt.sh JSON records."""
    subdomains: set[str] = set()
    for entry in records:
        name_value = entry.get("name_value", "")
        for item in name_value.splitlines():
            item = item.strip().lower()
            if item.endswith(f".{domain}") or item == domain:
                subdomains.add(item)
    return sorted(subdomains)


def main() -> int:
    parser = argparse.ArgumentParser(description="List subdomains via crt.sh")
    parser.add_argument("domain", help="Domain to search, e.g. example.com")
    parser.add_argument("-o", "--output", help="Write results to a file")
    args = parser.parse_args()

    try:
        records = fetch_crtsh(args.domain)
    except urllib.error.URLError as exc:
        sys.stderr.write(f"Error fetching data: {exc}\n")
        return 1
    except json.JSONDecodeError as exc:
        sys.stderr.write(f"Invalid JSON response: {exc}\n")
        return 1

    subdomains = extract_subdomains(records, args.domain)

    for sub in subdomains:
        print(sub)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as fh:
                fh.write("\n".join(subdomains))
        except OSError as exc:
            sys.stderr.write(f"Error writing file: {exc}\n")
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
