CXX=g++
RM=rm -f
objects = main.o

task1 : $(objects)
	$(CXX) -o task1 $(objects)

main.o : catch.h
	$(CXX) -c main.cpp

.PHONY : clean
clean :
	$(RM) task1 $(objects)