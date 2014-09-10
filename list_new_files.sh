if [ "$#" -ne 2 ]; then echo "Usage: $0 dir days"; exit; fi;

FILES=$(find $1 -ctime -$2)
for f in $FILES;
do 
  if [ -f $f ]; then
    du -h "$f"
  fi
done
