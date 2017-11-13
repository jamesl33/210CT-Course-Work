CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o cube.o

task3 : $(objects)
	$(CXX) $(CXXFLAGS) -o task3 $(objects)

main.o : main.cpp ../catch.hpp cube.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

cube.o : cube.cpp cube.hpp
	$(CXX) $(CXXFLAGS) -c cube.cpp

.PHONY : clean
clean :
	$(RM) task3 $(objects)
