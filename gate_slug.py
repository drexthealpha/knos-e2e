import re


def gate_slug(s):
    """A URL slug of s (synthetic demo for Knos Gate bounties mode; gated by a workflow_run run)."""
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
