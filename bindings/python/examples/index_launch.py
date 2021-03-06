#!/usr/bin/env python

# Copyright 2019 Stanford University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

import legion
from legion import task

@task
def hi(i):
    print("hello %s" % i)
    return i

@task
def main():
    futures = []
    for i in legion.IndexLaunch(10):
        futures.append(hi(i))
    for i, future in enumerate(futures):
        print("got %s" % future.get())
        assert int(future.get()) == i

    # Same in 2 dimensions.
    futures = []
    for point in legion.IndexLaunch([3, 3]):
        futures.append(hi(point))
    for i, point in enumerate(legion.Domain.create([3, 3])):
        assert futures[i].get() == point

if __name__ == '__legion_main__':
    main()
