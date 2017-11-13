CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o queen.o

task2 : $(objects)
	$(CXX) $(CXXFLAGS) -o task2 $(objects)

main.o : main.cpp queen.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

queen.o : queen.cpp queen.hpp
	$(CXX) $(CXXFLAGS) -c queen.cpp

.PHONY : clean
clean :
	$(RM) task2 $(objects)
