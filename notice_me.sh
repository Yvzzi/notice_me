#!/bin/bash
USAGE="Usage: $0 on | off | set-sendkey"
if [[ $# -eq 0 ]]; then
    echo $USAGE
    exit 1
fi
curr_path=$(dirname $(readlink -f "$0"))
cd $curr_path
tabjob="* * * * * python "$curr_path"/notice_me.py"
if [[ "$1" == "on" ]]; then
    (crontab -l | grep -v "$tabjob"; echo "$tabjob") | crontab - > /dev/null 2>&1
    sed -i -e 's#^\s*USER\s*=\s*.*#USER = "'$(whoami)'"#' \
        -e 's#^\s*BJOB_PATH\s*=\s*.*#BJOB_PATH = "'$(which bjobs)'"#' \
        -e 's#^\s*LSF_ENVDIR\s*=\s*.*#LSF_ENVDIR = "'$(echo $LSF_ENVDIR)'"#' \
        -e 's#^\s*LSF_BINDIR\s*=\s*.*#LSF_BINDIR = "'$(echo $LSF_BINDIR)'"#' \
        -e 's#^\s*LSF_LIBDIR\s*=\s*.*#LSF_LIBDIR = "'$(echo $LSF_LIBDIR)'"#' \
        -e 's#^\s*LSF_SERVERDIR\s*=\s*.*#LSF_SERVERDIR = "'$(echo $LSF_SERVERDIR)'"#' notice_me.py
elif [[ "$1" == "off" ]]; then
    (crontab -l | grep -v "$tabjob") | crontab - > /dev/null 2>&1
elif [[ "$1" == "set-sendkey" ]]; then
    while true; do
        echo "Please input you SENDKEY"
        read send_key
        echo "You SENDKEY is "$send_key", is it correct? (y/n)"
        read ans
        if [[ "$ans" == "y" ]]; then
            break
        fi
    done
    sed -i -e 's#^\s*SENDKEY\s*=\s*.*#SENDKEY = "'$send_key'"#' notice_me.py
else
    echo $USAGE
fi
unset tabjob curr_path ans send_key USAGE
