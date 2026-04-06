#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SRC_DIR="$ROOT_DIR/java/src/main/java"
BUILD_DIR="$ROOT_DIR/build/java"
CLASS_DIR="$BUILD_DIR/classes"
DIST_DIR="$ROOT_DIR/dist"
MANIFEST_FILE="$BUILD_DIR/MANIFEST.MF"

rm -rf "$BUILD_DIR"
mkdir -p "$CLASS_DIR" "$DIST_DIR"

find "$SRC_DIR" -name '*.java' -print0 | xargs -0 javac -d "$CLASS_DIR"

cat > "$MANIFEST_FILE" <<MANIFEST
Main-Class: com.dynamicsell.DynamicSellCli
MANIFEST

jar cfm "$DIST_DIR/dynamicsell.jar" "$MANIFEST_FILE" -C "$CLASS_DIR" .

echo "Built $DIST_DIR/dynamicsell.jar"
