def slugify(value):
    """Convert a label into a URL-ish slug."""
    return "-".join(value.strip().lower().split())


def normalize_csv_name(value):
    """Normalize a CSV column name."""
    return "_".join(value.replace(",", " ").strip().lower().split())
