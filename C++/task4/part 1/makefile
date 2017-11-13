CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o

task4p1 : $(objects)
	$(CXX) $(CXXFLAGS) -o task4p1 $(objects)

main.o : main.cpp ../../catch.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

.PHONY : clean
clean :
	$(RM) task4p1 $(objects)
