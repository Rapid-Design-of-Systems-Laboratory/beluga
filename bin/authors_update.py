#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A tool to generate AUTHORS. We started tracking authors before moving
to git, so we have to do some manual rearrangement of the git history
authors in order to get the order in AUTHORS. bin/mailmap_update.py
should be run before committing the results.

Note: Shamelessly taken from github.com/sympy/sympy
"""

from __future__ import unicode_literals
from __future__ import print_function

import codecs
import sys
import os

from subprocess import run, PIPE
from distutils.version import LooseVersion
from collections import defaultdict, OrderedDict

from sympy.utilities.misc import filldedent

if sys.version_info < (3, 6):
    sys.exit("This script requires Python 3.6 or newer")


def red(text):
    return "\033[31m%s\033[0m" % text


def yellow(text):
    return "\033[33m%s\033[0m" % text


def green(text):
    return "\033[32m%s\033[0m" % text


# put sympy on the path
mailmap_update_path = os.path.abspath(__file__)
mailmap_update_dir = os.path.dirname(mailmap_update_path)
sympy_top = os.path.split(mailmap_update_dir)[0]
sympy_dir = os.path.join(sympy_top, 'sympy')
if os.path.isdir(sympy_dir):
    sys.path.insert(0, sympy_top)

minimal = '1.8.4.2'
git_ver = run(['git', '--version'], stdout=PIPE, encoding='utf-8').stdout[12:]
if LooseVersion(git_ver) < LooseVersion(minimal):
    print(yellow("Please use a git version >= %s" % minimal))


def author_name(line):
    assert line.count("<") == line.count(">") == 1
    assert line.endswith(">")
    return line.split("<", 1)[0].strip()


def move(l, i1, i2, who):
    x = l.pop(i1)
    # this will fail if the .mailmap is not right
    assert who == author_name(x), \
        '%s was not found at line %i' % (who, i1)
    l.insert(i2, x)


# find who git knows ahout
git_command = ["git", "log", "--topo-order", "--reverse", "--format=%aN <%aE>"]
git_people = run(git_command, stdout=PIPE, encoding='utf-8').stdout.strip().split("\n")

# remove duplicates, keeping the original order
git_people = list(OrderedDict.fromkeys(git_people))

try:
    git_people.remove('jsDelivr Bot <contact@jsdelivr.com>')
    git_people.insert(5, '*Kshitij Mall')
except AssertionError as message:
    print(red(message))
    sys.exit(1)

# define new lines for the file

header = filldedent("""
    All people who contributed to beluga by sending at least a patch or
    more (in the order of the date of their first contribution), except
    those who explicitly didn't want to be mentioned. People with a * next
    to their names are not found in the metadata of the git history. This
    file is generated automatically by running `./bin/authors_update.py`.
    """).lstrip()
fmt = """There are a total of {authors_count} authors."""
header_extra = fmt.format(authors_count=len(git_people))
lines = header.splitlines()
lines.append('')
lines.append(header_extra)
lines.append('')
lines.extend(git_people)

# compare to old lines and stop if no changes were made

old_lines = codecs.open(os.path.realpath(os.path.join(
        __file__, os.path.pardir, os.path.pardir, "AUTHORS")),
        "r", "utf-8").read().splitlines()
if old_lines == lines:
    sys.exit(green('No changes made to AUTHORS.'))

# check for new additions
new_authors = []
for i in sorted(set(lines) - set(old_lines)):
    try:
        author_name(i)
        new_authors.append(i)
    except AssertionError:
        continue

# write the new file
with codecs.open(os.path.realpath(os.path.join(
        __file__, os.path.pardir, os.path.pardir, "AUTHORS")),
        "w", "utf-8") as fd:
    fd.write('\n'.join(lines))
    fd.write('\n')

# warn about additions
if new_authors:
    print(yellow(filldedent("""
        The following authors were added to AUTHORS.
        If mailmap_update.py has already been run and
        each author appears as desired and is not a
        duplicate of some other author, then the
        changes can be committed. Otherwise, see
        .mailmap for instructions on how to change
        an author's entry.""")))
    print()
    for i in sorted(new_authors, key=lambda x: x.lower()):
        print('\t%s' % i)
