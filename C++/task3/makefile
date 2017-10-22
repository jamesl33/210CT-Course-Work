CXX=g++
RM=rm -f
objects = main.o queen.o

task3 : $(objects)
	$(CXX) -o task3 $(objects)

main.o : main.cpp ../catch.hpp queen.hpp
	$(CXX) -c main.cpp

queen.o : queen.cpp queen.hpp
	$(CXX) -c queen.cpp

.PHONY : clean
clean :
	$(RM) task3 $(objects)
