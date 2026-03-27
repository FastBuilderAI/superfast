#!/usr/bin/env python3
import sys
import json
import os
try:
    import fastmemory
except ImportError:
    print("Error: fastmemory package not found. Run 'pip install fastmemory'.")
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: extract_cbfdae.py <markdown_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    with open(filepath, 'r') as f:
        content = f.read()

    try:
        # Extract structured CBFDAE data using fastmemory
        results = fastmemory.process_markdown(content)
        
        # Output as pretty JSON
        print(json.dumps(results, indent=2))
    except Exception as e:
        print(f"Error processing markdown: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
