"""Simple include directives.

This script allows you to write markdown like this:

    [include]: # (some/cool/file.py)
    ```python
    ```

The [include] directive is abusing markdown's footnote syntax, so it
won't be visible when the markdown is rendered.

Then you can run this script, and the markdown will be replaced with
this:

    [include]: # (some/cool/file.py)
    ```python
    here's the content from some/cool/file.py
    ```
"""

import glob
import os
import re


_INCLUDE_REGEX = (
    r'^\[include\]: # \((.*)\)\n'
    r'```.*\n'
    r'([\S\s]*?)'
    r'```$'
)


def replacer(match):
    path = match.group(1).replace('/', os.sep)
    with open(path, 'r') as file:
        file_content = file.read()

    if match.group(2) == file_content:
        # it's already ok
        return match.group(0)

    # there's probably a better way to replace just one group
    start = match.start(2) - match.start(0)
    end = match.end(2) - match.start(0)
    return match.group(0)[:start] + file_content + match.group(0)[end:]


def main():
    for filename in glob.glob('*.md'):
        with open(filename, 'r') as file:
            current = file.read()

        fixed = re.sub(_INCLUDE_REGEX, replacer, current, flags=re.MULTILINE)
        if current == fixed:
            print("Already OK:", filename)
        else:
            print("Updating", filename, "...")
            with open(filename, 'w') as f:
                f.write(fixed)
            print("  done.")


main()
