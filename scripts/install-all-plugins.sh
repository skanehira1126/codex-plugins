#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/.." && pwd)"
marketplace_file="${repo_root}/.agents/plugins/marketplace.json"
dry_run=false

case "${1:-}" in
  "") ;;
  --dry-run) dry_run=true ;;
  -h|--help)
    printf 'Usage: %s [--dry-run]\n' "${0##*/}"
    exit 0
    ;;
  *)
    printf 'Unknown option: %s\n' "$1" >&2
    printf 'Usage: %s [--dry-run]\n' "${0##*/}" >&2
    exit 2
    ;;
esac

if [[ ! -f "${marketplace_file}" ]]; then
  printf 'Marketplace file not found: %s\n' "${marketplace_file}" >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  printf 'python3 is required to read %s\n' "${marketplace_file}" >&2
  exit 1
fi

if [[ "${dry_run}" == false ]] && ! command -v codex >/dev/null 2>&1; then
  printf 'codex is required to install plugins.\n' >&2
  exit 1
fi

marketplace_name="$(python3 -c '
import json
import sys

with open(sys.argv[1], encoding="utf-8") as marketplace:
    data = json.load(marketplace)

name = data.get("name")
if not isinstance(name, str) or not name:
    raise SystemExit("marketplace name is missing or invalid")
print(name)
' "${marketplace_file}")"

plugin_names="$(python3 -c '
import json
import sys

with open(sys.argv[1], encoding="utf-8") as marketplace:
    data = json.load(marketplace)

plugins = data.get("plugins")
if not isinstance(plugins, list) or not plugins:
    raise SystemExit("marketplace plugins are missing or empty")

for plugin in plugins:
    name = plugin.get("name") if isinstance(plugin, dict) else None
    if not isinstance(name, str) or not name:
        raise SystemExit("plugin name is missing or invalid")
    print(name)
' "${marketplace_file}")"

while IFS= read -r plugin_name; do
  plugin_ref="${plugin_name}@${marketplace_name}"
  if [[ "${dry_run}" == true ]]; then
    printf 'codex plugin add %s\n' "${plugin_ref}"
  else
    codex plugin add "${plugin_ref}"
  fi
done <<< "${plugin_names}"
