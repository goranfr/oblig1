FILES=$(find tree/ -ctime $1)
for f in $FILES;
do 
  if [ -f $f ]; then
    du -h "$f"
  fi
done
