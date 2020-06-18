# Copyright (c) 2019, UC Berkeley
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import ast
from setuptools import setup
import sys
from os import path

requires = []

setup_requires = ['setuptools >= 30.3.0']
if {'pytest', 'test', 'ptr'}.intersection(sys.argv):
    setup_requires.append('pytest-runner')

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


# Get docstring and version without importing module
with open('tdtax/__init__.py') as f:
    mod = ast.parse(f.read())

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

__doc__ = ast.get_docstring(mod)
print(__doc__)

assignments = [node for node in mod.body if isinstance(node, ast.Assign)]
__version__ = [node.value.s for node in assignments
               if node.targets[0].id == '__version__'][0]

setup(description=__doc__.splitlines()[0],
      version=__version__,
      include_package_data=True,
      long_description=long_description,
      long_description_content_type="text/markdown",
      setup_requires=setup_requires,
      install_requires=requirements,
      package_dir={'tdtax': 'tdtax'},
      package_data={'tdtax': ['viz_template.html']},
      url='https://github.com/profjsb/timedomain-taxonomy'
      )
