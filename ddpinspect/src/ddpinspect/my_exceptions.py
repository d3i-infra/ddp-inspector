"""
Custom exceptions used by these modules
"""


class ObjectIsNotADict(Exception):
    """
    If object is not a dict raise this exception
    """


class FileNotFoundInZipError(Exception):
    """
    The File you are looking for is not present in a zipfile
    """
