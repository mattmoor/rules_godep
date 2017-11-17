# EXPERIMENTAL Bazel `godep` Rules

## Overview

The intent of these rules is to make it easier for folks to manage importing
external Go dependencies already tracked via godep in Bazel.  They follow a
similar pattern to `rules_python`:
```python
# rules_go must already be imported!
load("@io_mattmoor_rules_godep//:def.bzl", "godep_import")

# This rule translates the specified Godeps.json into
# @my_deps//:godeps.bzl, which itself exposes a godep_restore method.
godep_import(
   name = "my_deps",
   requirements = "//path/to:Godeps.json",
)

# Load the godep_restore symbol for my_deps, and create the dependencies'
# repositories.
load("@my_deps//:godeps.bzl", "godep_restore")

godep_restore()
```