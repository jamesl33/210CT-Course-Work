CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o queen.o

Units : $(objects)
	$(CXX) $(CXXFLAGS) -o Units $(objects)

main.o : main.cpp ../queen.hpp ../../catch.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

queen.o : ../queen.cpp ../queen.hpp
	$(CXX) $(CXXFLAGS) -c ../queen.cpp

.PHONY : clean
clean :
	$(RM) Units $(objects)
