# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:17:03 2019

@author: Guojian Wang
"""

import os
import re
from setuptools import setup, find_packages


def read(filename):
    f = open(filename)
    r = f.read()
    f.close()
    return r

ver = re.compile("__version__ = \"(.*?)\"")
#m = read(os.path.join(os.path.dirname(os.path.abspath(__file__)), "refann", "__init__.py"))
#m = read(os.path.join(os.path.dirname(__file__), "refann", "__init__.py"))
m = read(os.path.join(os.getcwd(), "coplot", "__init__.py"))
version = ver.findall(m)[0]



setup(
    name = "coplot",
    version = version,
    keywords = ("pip", "plot"),
    description = "A personal plotting library that commonly used in the research of cosmology and astrophysics.",
    long_description = "",
    license = "MIT",

    url = "",
    author = "Guojian Wang",
    author_email = "gjwang@mail.bnu.edu.cn",

#    packages = find_packages(),
    packages = ["coplot", "examples/contour_1D", "examples/contour_2D", "examples/contour_triangle"],
    include_package_data = True,
    data_files = ["examples/README.txt",
                  "examples/contour_1D/README.txt",
                  "examples/contour_2D/README.txt",
                  "examples/contour_triangle/README.txt",
                  ],
    platforms = "any",
    install_requires = []
)

