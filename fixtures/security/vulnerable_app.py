import os
import subprocess
import yaml


def unsafe_eval(expression):
    """Fixture for security scanners. Do not copy into production code."""
    return eval(expression)


def load_untrusted_yaml(payload):
    """Fixture that should be flagged by security analysis."""
    return yaml.load(payload)


def run_user_command(command):
    """Fixture for command execution risk checks."""
    return subprocess.check_output(command, shell=True, cwd=os.getcwd())
