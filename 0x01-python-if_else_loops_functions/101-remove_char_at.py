#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        # If the index n is out of range, return the original string
        return str
    else:
        # Otherwise, return a new string with the character at index n removed
        return str[:n] + str[n+1:]

