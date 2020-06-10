#!/usr/bin/env python

import os
import shutil

from datadog_checks.dev.subprocess import run_command
from datadog_checks.dev.tooling.config import load_config
from datadog_checks.dev.tooling.commands.console import echo_info, abort, echo_warning

"""
This script will create sequential commits in the integrations-extra repo,
to demonstrate the process of building a new integration called `github_repo`.

It first checks to make sure the "master" branch is not active, then proceeds
to copy and commit the contents of each of the folders in this directory.
"""

config = load_config()
EXTRAS_REPO = config['repos']['extras']
EXTRAS_REPO = os.path.expanduser(EXTRAS_REPO)
SOLUTIONS_DIR = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(EXTRAS_REPO):
    abort(f'Unable to find integrations-extras repo: {EXTRAS_REPO}')


def verify_branch():
    os.chdir(EXTRAS_REPO)
    r = run_command('/usr/local/bin/git branch --show-current', True)
    branch = r.stdout.strip()
    if branch == 'master':
        abort('Change your branch!')


def get_stages():
    stages = [x for x in sorted(os.listdir(SOLUTIONS_DIR)) if x[0].isdigit()]
    return stages


def run_cmd(cmd):
    r = run_command(cmd, True)
    echo_info(f'Command: {cmd}')
    if r.stdout:
        echo_info(f'stdout: {r.stdout}', True)
    if r.stderr:
        echo_warning(f'stderr: {r.stderr}', True)
    echo_info('')


def make_commits():
    os.chdir(EXTRAS_REPO)
    for stage in get_stages():
        base = os.path.join(SOLUTIONS_DIR, stage, 'github_repo')
        shutil.copytree(base, os.path.join(EXTRAS_REPO, 'github_repo'), dirs_exist_ok=True)
        run_cmd('/usr/local/bin/git add github_repo')
        run_cmd(f'/usr/local/bin/git commit --no-gpg-sign -m "github_repo example: {stage}"')


if __name__ == '__main__':
    verify_branch()
    make_commits()
