echo Deleting...
count=0
for f in $(find $1)
do
  size=$(stat -c%s "$f")
  if [ "$size" -gt $(($2*1000)) ]; then
    echo $f
    rm -f $f
    count=$(($count+1))
  fi
done
if [ "$count" -eq 0 ]; then
  echo No files larger than "$2"KB
fi