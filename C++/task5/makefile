CXX=g++
RM=rm -f
objects = main.o

task4 : $(objects)
	$(CXX) -o task4 $(objects)

main.o : main.cpp ../catch.hpp
	$(CXX) -c main.cpp

.PHONY : clean
clean :
	$(RM) task4 $(objects)
