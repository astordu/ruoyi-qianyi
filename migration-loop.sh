#!/usr/bin/env bash
set -euo pipefail

# Python standard library handles JSON, process timeouts and the project lock.
MIGRATION_PROJECT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)
exec python3 "$MIGRATION_PROJECT_DIR/migration/scripts/migration_loop.py" "$@"
