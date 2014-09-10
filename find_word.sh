for f in $(find $1)
do
	if [ -f $f ]; then
		match=$(cat $f | grep $2)
		if [ -n "$match" ]; then
			echo $f
		fi
	fi
done

