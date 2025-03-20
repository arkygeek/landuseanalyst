#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple script to inspect crop XML files.
"""

import sys
import os
import xml.etree.ElementTree as ET
from la.lib.lautils import LaMessageBus

MESSAGE_BUS = LaMessageBus()

def inspect_crop_xml(filepath):
    """Inspect a crop XML file and print its contents."""
    MESSAGE_BUS.debug(f"Inspecting crop XML file: {filepath}")

    try:
        # Parse the XML file
        tree = ET.parse(filepath)
        root = tree.getroot()

        # Print basic info
        MESSAGE_BUS.debug(f"Root tag: {root.tag}")
        MESSAGE_BUS.debug(f"Root attributes: {root.attrib}")

        # Print all child elements
        MESSAGE_BUS.debug("\nChild elements:")
        for child in root:
            MESSAGE_BUS.debug(f"{child.tag}: {child.text}")

        # Look specifically for cropYield
        crop_yield_elem = root.find("cropYield")
        if crop_yield_elem is not None:
            MESSAGE_BUS.debug(f"\nFound cropYield element: {crop_yield_elem.text} (type: {type(crop_yield_elem.text)})")
            if crop_yield_elem.text is not None:
                try:
                    yield_value = int(crop_yield_elem.text)
                    MESSAGE_BUS.debug(f"cropYield as int: {yield_value}")
                except (ValueError, TypeError) as e:
                    MESSAGE_BUS.debug(f"Error converting cropYield to int: {str(e)}")
            else:
                MESSAGE_BUS.debug("cropYield element's text is None")
        else:
            MESSAGE_BUS.debug("\ncropYield element not found!")

    except Exception as e:
        MESSAGE_BUS.debug(f"Error parsing XML: {str(e)}")
        import traceback
        MESSAGE_BUS.debug(traceback.format_exc())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        MESSAGE_BUS.debug("Usage: python inspect_crop_xml.py <path-to-xml-file>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        MESSAGE_BUS.debug(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    inspect_crop_xml(filepath)
