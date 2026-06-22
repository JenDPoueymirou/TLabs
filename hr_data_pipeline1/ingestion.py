def load_file(filepath):
    """
    Load a raw heart-rate file and return a list of decoded lines.
    """
    raw_lines = []

    with open(filepath, "rb") as f:
        for line in f:
            decoded = line.decode("utf-8").strip()
            raw_lines.append(decoded)

    return raw_lines
