#!/bin/bash
set -e

usage() {
  echo "Usage: $0 [OPTIONS]"
  echo "Options:"
  echo " -h, --help      Display this help message"
  echo " -p, --public    Run the public version with custom emoji"
  echo " -pr, --private  Run the private version with Unicode emoji"
  echo " --pipenv        Run the private version with pipenv"
  echo " --pipenv-public Run the public version with pipenv"
}

# Function to handle options and arguments
handle_options() {
  if [ $# -eq 0 ]; then
    usage
    exit 0
  fi

  while [ $# -gt 0 ]; do
    case $1 in
      -h | --help)
        usage
        exit 0
        ;;
      -p | --public)
        python3 main.py
        exit 0
        ;;
      -pr | --private)
        python3 main_emoji.py
        exit 0
        ;;
      --pipenv)
        pipenv run generic
        exit 0
        ;;
      --pipenv-public)
        pipenv run public
        exit 0
        ;;
      *)
        echo "Invalid option: $1" >&2
        usage
        exit 1
        ;;
    esac
    shift
  done
}

# Main script execution
handle_options "$@"
