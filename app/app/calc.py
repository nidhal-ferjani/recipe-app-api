"""
Calculator functions
"""


def add(*args):
    """
    :param args: *args
    :return: results.
    """
    som = 0
    for ele in args:
        som = som + ele
    return som
