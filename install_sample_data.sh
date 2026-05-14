#!/usr/bin/env bash
# Copies the bundled sample data into ~/.landuseAnalyst/ so the plugin has
# animals, crops, and their parameters available when it starts.
#
# Usage:
#   ./install_sample_data.sh           # skip files that already exist
#   ./install_sample_data.sh --force   # overwrite existing files
#
# The app reads XML profiles from these four directories:
#   ~/.landuseAnalyst/animalProfiles/
#   ~/.landuseAnalyst/cropProfiles/
#   ~/.landuseAnalyst/animalParameterProfiles/
#   ~/.landuseAnalyst/cropParameterProfiles/
#
# Sample images are copied to:
#   ~/.landuseAnalyst/images/

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="$SCRIPT_DIR/testData"
INSTALL_DIR="$HOME/.landuseAnalyst"

FORCE=0
if [[ "${1:-}" == "--force" ]]; then
    FORCE=1
fi

if [[ ! -d "$DATA_DIR" ]]; then
    echo "ERROR: Sample data directory not found: $DATA_DIR" >&2
    exit 1
fi

SUBDIRS=(
    animalProfiles
    cropProfiles
    animalParameterProfiles
    cropParameterProfiles
    images
)

for subdir in "${SUBDIRS[@]}"; do
    src="$DATA_DIR/$subdir"
    dst="$INSTALL_DIR/$subdir"

    mkdir -p "$dst"

    if [[ ! -d "$src" ]]; then
        echo "  (skipping $subdir — not found in testData/)"
        continue
    fi

    count=0
    for f in "$src"/*; do
        [[ -f "$f" ]] || continue
        dest_file="$dst/$(basename "$f")"
        if [[ $FORCE -eq 1 || ! -e "$dest_file" ]]; then
            cp "$f" "$dest_file"
            (( count++ )) || true
        fi
    done

    total=$(ls "$src" | wc -l)
    echo "  $subdir: copied $count / $total files -> $dst"
done

echo ""
echo "Done. Run QGIS and enable the Landuse Analyst plugin to see the data."
echo "If animals or crops are still missing, check: $INSTALL_DIR"
