# Copyright 2022 The CLU Authors.
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

"""setup.py for Common Loop Utils.

Install for development:

  pip intall -e . .[tests]
"""

from setuptools import find_packages
from setuptools import setup

tests_require = [
    "pytest",
    "torch>=1.2.0",
]
pytorch_require = [
    "torch>=1.2.0",
]

setup(
    name="clu",
    version="0.0.7",
    description=("Set of libraries for ML training loops in JAX."),
    author="Common Loop Utils Authors",
    author_email="no-reply@google.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="http://github.com/google/CommonLoopUtils",
    license="Apache 2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "absl-py",
        "etils[epath]",
        "flax",
        "jax",
        "jaxlib",
        "ml_collections",
        "numpy",
        "packaging",
        "tensorflow_datasets",
        "typing_extensions",
    ] + (["tensorflow-macos"] if "darwin" == sys.platform else ["tensorflow-cpu"]),
    tests_require=tests_require,
    extras_require=dict(test=tests_require, pytorch=pytorch_require),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="JAX machine learning",
)
