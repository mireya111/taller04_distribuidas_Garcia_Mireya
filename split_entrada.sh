#! /usr/bin/bash
mkdir -p splits
split -l 25 -d logs.txt splits/part_ --additional-suffix=.txt