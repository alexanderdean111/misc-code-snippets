#!/bin/bash

pathToThisScript="$(readlink -f "${BASH_SOURCE}")"
parentDirectory="$(dirname $pathToThisScript)"

echo "Path to this script:             ${pathToThisScript}"
echo "Parent directory of this script: ${parentDirectory}"
