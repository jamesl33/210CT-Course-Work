CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o

task2 : $(objects)
	$(CXX) $(CXXFLAGS) $(objects) -o task2

main.o : main.cpp material.hpp lorry.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

.PHONY : clean
clean :
	$(RM) task2 $(objects)
