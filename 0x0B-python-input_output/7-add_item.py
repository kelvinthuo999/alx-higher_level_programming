#!/usr/bin/python3
""" function to add all arguments """
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_arguments_to_list():
    # Check if "add_item.json" file exists and load its content if it does
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    # Add command-line arguments to the list
    for arg in sys.argv[1:]:
        items.append(arg)
    # Save the updated list to "add_item.json"
    save_to_json_file(items, "add_item.json")
