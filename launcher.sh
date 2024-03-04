#!/bin/sh
RED=$(tput setaf 1)
NORMAL=$(tput sgr0)


MYVAR=$(dialog --clear \
--title "PythonPortfolio" \
--menu "Choose one of the following programs:" 15 40 4 \
            1 "ProceduralRoomGeneration" \
            2 "RaspberryPiFanControl 2" \
--output-fd 1)
clear
case $MYVAR in
        1)
            echo "Starting... PoceduralRoomGeneration"
            ./ProceduralRoomGeneration/launcher.sh
            ;;
        2)
            echo "${RED}Error${NORMAL}: Sorry, this program cannot be run on this device, refer to the README.md file"
            ;;
esac