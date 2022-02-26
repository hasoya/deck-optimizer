"""This module includes all custom warnings and error classes used across dopt."""


class DoptException(Exception):
    """Base class of all custom exceptions in dopt."""


class SettingsNotSetError(DoptException):
    """Exception class to raise if Searcher is used before search."""


class NoDeckError(DoptException):
    """Exception class to raise if no deck is created."""
