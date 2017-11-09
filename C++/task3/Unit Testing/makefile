CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o cube.o

Units : $(objects)
	$(CXX) $(CXXFLAGS) -o Units $(objects)

main.o : main.cpp ../stacking.cpp ../cube.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

cube.o : ../cube.cpp ../cube.hpp
	$(CXX) $(CXXFLAGS) -c ../cube.cpp

.PHONY : clean
clean :
	$(RM) Units $(objects)
