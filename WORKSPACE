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
workspace(name = "io_mattmoor_rules_godep")

# For our go_image test.
git_repository(
    name = "io_bazel_rules_go",
    commit = "4be196cc186da9dd396d5a45a3a7f343b6abe2b0",
    remote = "https://github.com/bazelbuild/rules_go.git",
)

load("@io_bazel_rules_go//go:def.bzl", "go_repositories")

go_repositories()

load("@io_mattmoor_rules_godep//:def.bzl", "godep_import")

godep_import(
    name = "k8s_sample_apiserver",
    godeps = "//testdata:k8s-sample-apiserver.json",
)

# TODO(mattmoor): Enable this, if we want to fetch the Go libs.
load("@k8s_sample_apiserver//:godep.bzl", "godep_restore")
godep_restore()
