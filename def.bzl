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
"""Import Godeps.json into Bazel."""

def _godep_import_impl(repository_ctx):
  """Core implementation of godep_import."""

  # Add an empty top-level BUILD file.
  # This is because Bazel requires BUILD files along all paths accessed
  # via //this/sort/of:path and we wouldn't be able to load our generated
  # requirements.bzl without it.
  repository_ctx.file("BUILD", 'exports_files(["godep.bzl"])')

  # To see the output, pass: quiet=False
  result = repository_ctx.execute([
    "python", repository_ctx.path(repository_ctx.attr._script),
    "--godeps", repository_ctx.path(repository_ctx.attr.godeps),
    "--output", repository_ctx.path("godep.bzl"),
  ])

  if result.return_code:
    fail("pip_import failed: %s (%s)" % (result.stdout, result.stderr))


godep_import = repository_rule(
    attrs = {
        "godeps": attr.label(
            allow_files = [".json"],
            mandatory = True,
            single_file = True,
        ),
        "_script": attr.label(
            executable = True,
            default = Label("//:translate.py"),
            cfg = "host",
        ),
    },
    implementation = _godep_import_impl,
)
