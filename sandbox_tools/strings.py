def slugify(value):
    """Convert a label into a URL-ish slug."""
    return value.strip().replace(" ", "-")


def normalize_csv_name(value):
    """Normalize a CSV column name."""
    return value.strip().lower()

