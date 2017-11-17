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

import os
import unittest

def TestData(name):
  with open(os.path.join(os.environ['TEST_SRCDIR'], name), 'r') as f:
    return f.read()

class TranslateTest(unittest.TestCase):

  def test_k8s_sample_apiserver(self):
      td = TestData('k8s_sample_apiserver/godep.bzl')
      self.assertTrue('com_github_PuerkitoBio_purell' in td)


if __name__ == '__main__':
  unittest.main()
