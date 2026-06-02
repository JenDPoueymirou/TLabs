def clean_records(raw_lines):
    cleaned = []

    for line in raw_lines:
        line = line.strip()              # remove whitespace

        if line == "":                   # skip blank lines
            continue

        if line.upper() == "NO DATA":    # skip NO DATA lines
            continue

        if not line.isdigit():           # skip anything non-numeric
            continue

        value = int(line)

        if 30 <= value <= 250:           # keep realistic heart-rate values
            cleaned.append(value)

    return cleaned
