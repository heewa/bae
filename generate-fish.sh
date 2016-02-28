#!/bin/bash

./generate.py | sed -r -s "s/^(E_.*)=(.*)$/set \1 \2/g"
