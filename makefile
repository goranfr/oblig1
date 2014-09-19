
all: clean python

python: generate_file_tree.py
	./generate_file_tree.py -s 199 -v -d 5 test/ 4 4

.PHONY: all clean

clean:
	rm -rf test/
