
all: clean python

python: generate_file_tree.py
	./generate_file_tree.py -s 1 -v -d 2 test/ 2 2

.PHONY: all clean

clean:
	rm -rf test/
