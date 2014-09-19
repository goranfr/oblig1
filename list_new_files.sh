if [ "$#" -ne 2 ]; then echo "Usage: $0 dir days"; exit; fi;

find $1 -ctime -$2 -type f -exec du -h {} \; | sort -h
