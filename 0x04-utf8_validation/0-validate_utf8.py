#!/usr/bin/python3
"""UTF-8 Validation"""
from typing import List

def validUTF8(data: List[int]) -> bool:
	"""
	Determines if a given data set represents a valid UTF-8 encoding
	params:
		data: list of integers
	returns: True if data is valid UTF-8, else False
	"""
