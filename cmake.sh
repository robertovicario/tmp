#!/bin/bash

# Ensure script has executable permissions:
# chmod +x cmake.sh

if [ -d "build" ]; then
    rm -r build
fi

cmake -B build -GNinja
