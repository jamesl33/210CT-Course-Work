CXX=g++
RM=rm -f
objects = main.o

task5p2 : $(objects)
	$(CXX) -o task5p2 $(objects)

main.o : main.cpp ../../catch.hpp
	$(CXX) -c main.cpp

.PHONY : clean
clean :
	$(RM) task5p2 $(objects)
