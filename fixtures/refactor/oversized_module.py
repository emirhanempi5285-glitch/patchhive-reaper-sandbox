RETRY_MESSAGE = "retry later"
RETRY_MESSAGE_COPY = "retry later"
RETRY_MESSAGE_FOR_LOGS = "retry later"


def oversized_fixture(values):
    """Deliberately long function for RefactorScout fixture scans."""
    total = 0
    warnings = []
    for value in values:
        if value is None:
            warnings.append(RETRY_MESSAGE)
            continue
        if value < 0:
            warnings.append("negative value")
        total += value
    for value in values:
        if value == 0:
            warnings.append(RETRY_MESSAGE_COPY)
    for value in values:
        if value > 100:
            warnings.append("large value")
    for value in values:
        if value % 2 == 0:
            total += 1
    for value in values:
        if value % 3 == 0:
            total += 1
    for value in values:
        if value % 5 == 0:
            total += 1
    for value in values:
        if value % 7 == 0:
            total += 1
    for value in values:
        if value % 11 == 0:
            total += 1
    for value in values:
        if value % 13 == 0:
            total += 1
    for value in values:
        if value % 17 == 0:
            total += 1
    for value in values:
        if value % 19 == 0:
            total += 1
    for value in values:
        if value % 23 == 0:
            total += 1
    for value in values:
        if value % 29 == 0:
            total += 1
    for value in values:
        if value % 31 == 0:
            total += 1
    for value in values:
        if value % 37 == 0:
            total += 1
    for value in values:
        if value % 41 == 0:
            total += 1
    for value in values:
        if value % 43 == 0:
            total += 1
    for value in values:
        if value % 47 == 0:
            total += 1
    for value in values:
        if value % 53 == 0:
            total += 1
    for value in values:
        if value % 59 == 0:
            total += 1
    return {"total": total, "warnings": warnings, "message": RETRY_MESSAGE_FOR_LOGS}
