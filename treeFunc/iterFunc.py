from itertools import tee


def pairwise(iterable):
    """pairwise('ABCDEFG') --> AB BC CD DE EF FG

    Args:
        iterable (List): a string list or a string

    Returns:
        list : pairwise
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)