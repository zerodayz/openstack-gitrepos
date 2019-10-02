#!/usr/bin/python
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import requests
import os

TEMPLATE = "https://opendev.org/%s.git\n"

# only return projects starting with openstack
CONFIG = ("https://review.openstack.org:443/projects/?p=openstack")


def find_integrated_gate_projects():
    r = requests.get(CONFIG)
    # strip off first few chars because 'the JSON response body starts with a
    # magic prefix line that must be stripped before feeding the rest of the
    # response body to a JSON parser'
    # https://review.openstack.org/Documentation/rest-api.html
    gerrit_projects = json.loads(r.text[4:])

    # Ignore openstack-attic
    orgs = ['openstack/', 'openstack-infra/', 'openstack-dev/']
    blacklist = ['openstack/openstack']

    projects = []
    for project in gerrit_projects:
        if any(project.startswith(org) for org in orgs):
            if project not in blacklist:
                projects.append(project)
    return projects


def gen_gitrepos(projects):
    projects = sorted(projects)
    if os.path.exists('gitrepos'):
       os.rename('gitrepos', 'gitrepos-old')
    with open("gitrepos", 'w') as f:
        for p in projects:
            ns, name = p.split('/')
            f.write(TEMPLATE % (p))


def main():
    projects = find_integrated_gate_projects()
    gen_gitrepos(projects)


if __name__ == '__main__':
    main()
