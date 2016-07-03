#!/bin/bash

git_dir=/Users/jayson/Documents/git
my_dir=$git_dir/kundouzhishou
gs_dir=$git_dir/goodsure_python
rm -rf $my_dir/goodsure.log
cd $gs_dir
python goodsure.py -w 40 -m 15000 -s > $my_dir/goodsure.log
