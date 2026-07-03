import pytest

from sandbox_tools.mathy import safe_average
from sandbox_tools.strings import normalize_csv_name, slugify


def test_slugify_lowercases_and_collapses_spaces():
    assert slugify("  Hello   PatchHive  ") == "hello-patchhive"


def test_safe_average_empty_list_returns_zero():
    assert safe_average([]) == 0


def test_normalize_csv_name_replaces_commas():
    assert normalize_csv_name("Total, Cost") == "total_cost"

