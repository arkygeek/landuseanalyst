#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple script to inspect crop XML files.
"""

import sys
import os
import xml.etree.ElementTree as ET

def inspect_crop_xml(filepath):
    """Inspect a crop XML file and print its contents."""
    print(f"Inspecting crop XML file: {filepath}")

    try:
        # Parse the XML file
        tree = ET.parse(filepath)
        root = tree.getroot()

        # Print basic info
        print(f"Root tag: {root.tag}")
        print(f"Root attributes: {root.attrib}")

        # Print all child elements
        print("\nChild elements:")
        for child in root:
            print(f"{child.tag}: {child.text}")

        # Look specifically for cropYield
        crop_yield_elem = root.find("cropYield")
        if crop_yield_elem is not None:
            print(f"\nFound cropYield element: {crop_yield_elem.text} (type: {type(crop_yield_elem.text)})")
            if crop_yield_elem.text is not None:
                try:
                    yield_value = int(crop_yield_elem.text)
                    print(f"cropYield as int: {yield_value}")
                except (ValueError, TypeError) as e:
                    print(f"Error converting cropYield to int: {str(e)}")
            else:
                print("cropYield element's text is None")
        else:
            print("\ncropYield element not found!")

    except Exception as e:
        print(f"Error parsing XML: {str(e)}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inspect_crop_xml.py <path-to-xml-file>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    inspect_crop_xml(filepath)
