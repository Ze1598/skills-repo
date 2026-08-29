#!/usr/bin/env python3
"""Generate bounded metadata for a Twitter-style screenshot."""

import json
import secrets


def inclusive_random(minimum: int, maximum: int) -> int:
    return minimum + secrets.randbelow(maximum - minimum + 1)


metadata = {
    "hours": inclusive_random(3, 20),
    "views": inclusive_random(3, 137),
}

print(json.dumps(metadata))
