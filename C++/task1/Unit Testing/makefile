CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o

Units : $(objects)
	$(CXX) $(CXXFLAGS) -o Units $(objects)

main.o : main.cpp ../../catch.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

.PHONY : clean
clean :
	$(RM) Units $(objects)
