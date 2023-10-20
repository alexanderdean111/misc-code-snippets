#!/bin/bash

# https://stackoverflow.com/questions/16483119/an-example-of-how-to-use-getopts-in-bash

usage() {
  # print usage message
  cat << EOF

Usage: $0 <options>
  -a: Does 'a' things, no argument
  -b: Does 'b' things, takes argument
  -c: Does 'c' things, no arguments
  -d: Not supported, but will make the script complain
EOF
}

# if no args, print usage and exit
if [[ "$#" -eq 0 ]]; then
  usage
  exit 1;
fi

# parameters a and c have no argument (-a, -c), parameter b (followed by : in OPTSTRING)
# has an argument (-b arg)
# OPTSTRING starting with ':' will supress bash error messages
while getopts ":ab:c" opt; do
  case "$opt" in
    a)
      echo "Got -a"
      echo "OPTARG: ${OPTARG}"
      echo ""
      ;;
    b)
      echo "Got -b"
      echo "OPTARG: ${OPTARG}"
      echo ""
      ;;
    c)
      echo "Got -c"
      echo "OPTARG: ${OPTARG}"
      echo ""
      ;;
    *)
      echo "Got unsupported options"
      usage
      exit 1;
      ;;
  esac
done











