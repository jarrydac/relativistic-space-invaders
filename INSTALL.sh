#!/bin/sh
git clone --depth 1 --branch v0.0.3-alpha https://github.com/jarrydac/gl_relativity.git
cd gl_relativity
make
python setup.py build_ext --inplace
cd ..
ln -s gl_relativity/libgl_relativity.so ./
ln -s gl_relativity/gl_relativity_py ./