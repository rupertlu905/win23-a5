objects = main.o addition.o subtraction.o multiplication.o division.o

calculator: $(objects)
	cc -o calculator $^

$(objects): %.o:%.c
	cc -c $< -o $@

.PHONY: clean

clean:
	rm -f calculator $(objects)
