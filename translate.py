# Copyright 2017 The Bazel Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import json

parser = argparse.ArgumentParser(
    description='Import Godeps.json into Skylark.')

parser.add_argument('--godeps', action='store',
                    help=('The path to Godeps.json.'))

parser.add_argument('--output', action='store',
                    help=('The name of the file into which '
                          'to write the Skylark library.'))


def main():
  args = parser.parse_args()
  with open(args.godeps, 'r') as f:
    raw_content = f.read()
  content = json.loads(raw_content)

  def go_name(dep):
    parts = dep['ImportPath'].split('/')
    domain_parts = parts[0].split('.')
    other_parts = parts[1:]
    return '_'.join(list(reversed(domain_parts)) + other_parts)

  def go_repository(dep):
    return """
  go_repository(
      name = "{name}",
      importpath = "{importpath}",
      commit = "{commit}",
  )""".format(
    name = go_name(dep),
    importpath = dep['ImportPath'],
    commit = dep['Rev'])

  repos = map(go_repository, content.get('Deps'))
  with open(args.output, 'w') as f:
    f.write('{load}\ndef godep_restore():\n{repos}'.format(
      load = 'load("@io_bazel_rules_go//go:def.bzl", "go_repository")',
      repos = '\n'.join(repos) or 'pass'))

if __name__ == '__main__':
  main()
