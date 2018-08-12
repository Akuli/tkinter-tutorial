#!/usr/bin/env python3
"""Automatic manual page links.

This scripts searches for man page links and adds a list of them at the
end of a markdown file, so you can write markdown like this:

    See [the label man page][label(3tk)].
"""

import glob
import re


# these shouldn't conflict with Python code examples because 3tk and
# 3tcl are invalid syntax in Python
# this matches [anything][any_word(3tcl or 3tk)] or just the second [...] part
LINK_REGEX = re.compile(r'(?:\[.*?\])?\[(\w+\(3(?:tk|tcl)\))\]')
LINK_LIST_REGEX = re.compile(
    r'^\[manpage list\]: # \(start\)$' +
    r'[\S\s]*?' +
    r'^\[manpage list\]: # \(end\)$', re.MULTILINE)


# we need a dict because these aren't always SOME_TEMPLATE % manpagename
# this also helps with catching spelling errors because now lable(3tk)
# causes a KeyError
TK_TEMPLATE = 'https://www.tcl.tk/man/tcl/TkCmd/%s.htm'
TCL_TEMPLATE = 'https://www.tcl.tk/man/tcl/TclCmd/%s.htm'
URLS = {
    'ttk_button(3tk)': TK_TEMPLATE % 'ttk_button',
    'grid(3tk)': TK_TEMPLATE % 'grid',
    'ttk_label(3tk)': TK_TEMPLATE % 'ttk_label',
    'pack(3tk)': TK_TEMPLATE % 'pack',
    'place(3tk)': TK_TEMPLATE % 'place',
    'tk_chooseColor(3tk)': TK_TEMPLATE % 'chooseColor',
    'tk_chooseDirectory(3tk)': TK_TEMPLATE % 'chooseDirectory',
    'tk_getOpenFile(3tk)': TK_TEMPLATE % 'getOpenFile',
    'tk_messageBox(3tk)': TK_TEMPLATE % 'messageBox',
    'toplevel(3tk)': TK_TEMPLATE % 'toplevel',
    'wm(3tk)': TK_TEMPLATE % 'wm',
    'after(3tcl)': TCL_TEMPLATE % 'after',
}


def update_manpage_list(old_content):
    links = LINK_REGEX.findall(old_content)
    if not links:
        return old_content

    lines = ['[manpage list]: # (start)']
    for manpage in sorted(set(links)):
        lines.append('[%s]: %s' % (manpage, URLS[manpage]))
    lines.append('[manpage list]: # (end)')
    manpage_list = '\n'.join(lines)

    match = LINK_LIST_REGEX.search(old_content)
    if match is None:
        return old_content + '\n' + manpage_list + '\n'

    start, end = match.span()
    return old_content[:start] + manpage_list + old_content[end:]


def main():
    for filename in glob.iglob('*.md'):
        with open(filename, 'r') as file:
            old_content = file.read()

        new_content = update_manpage_list(old_content)
        if new_content == old_content:
            print("Already OK:", filename)
        else:
            print("Updating", filename, "...")
            with open(filename, 'w') as f:
                f.write(new_content)
            print("  done.")


if __name__ == '__main__':
    main()
