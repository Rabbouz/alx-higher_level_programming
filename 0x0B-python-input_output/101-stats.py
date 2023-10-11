#!/usr/bin/python3
"""Reading from standard input and computing metrics."""


def print_stats(size, s_codes):
    """Printing accumulated metrics.

    Args:
        size: The accumulated read file size.
        s_codes: The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(s_codes):
        print("{}: {}".format(key, s_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    s_codes = {}
    v_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    counter = 0

    try:
        for line in sys.stdin:
            if counter == 10:
                print_stats(size, s_codes)
                counter = 1
            else:
                counter += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in v_codes:
                    if s_codes.get(line[-2], -1) == -1:
                        s_codes[line[-2]] = 1
                    else:
                        s_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, s_codes)

    except KeyboardInterrupt:
        print_stats(size, s_codes)
        raise
