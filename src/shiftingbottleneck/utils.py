def argmin_kv(d):
    """
    A function that returns the schedule with minimal lateness and the associated lateness.
    """
    return min(d.items(), key=lambda x: x[1])