if [ "$#" -ne 2 ]; then echo "Usage: $0 f1 f2"; exit; fi;
sort "$1" --output="$2"
