#!/bin/bash


# Colored output functions for logging
log() {
  echo -e "\e[33m[*] $1\e[0m"
}

successLog() {
  echo -e "\e[32m[+] $1\e[0m"
}

errorLog() {
  echo -e "\e[31m[-] $1\e[0m"

}

log "Output from log()"
successLog "Output from successLog()"
errorLog "Output from errorLog()"
