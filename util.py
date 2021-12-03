import sys


def print_line(line: str, continuous: bool = False):
    if continuous:
        print()  # insert new line
    else:
        sys.stdout.write("\r\x1b[2K")  # clear line

    sys.stdout.write(line)
    sys.stdout.flush()


def adaptive_precision(value: float, target_width: int, max_decimal_places: int = 1):
    is_less_than_1 = 0 <= value < 1

    if is_less_than_1:
        target_width += 1  # leading "0" will be removed later

    # iteratively reduce the number of decimals until the target width is achieved
    for num_decimals in range(max_decimal_places, -1, -1):
        output = f"{value:{target_width}.{num_decimals}f}"
        if len(output) <= target_width:
            break

    if is_less_than_1:
        if "0." in output:
            output = output.replace("0.", ".")
        else:
            # rounding caused this number (< 1) to begin with "1."
            # thus being one digit too long currently
            output = f"{value:{target_width}.{num_decimals}f}"

    return output


pass
