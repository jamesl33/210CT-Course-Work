CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o queen.o

task3 : $(objects)
	$(CXX) $(CXXFLAGS) -o task3 $(objects)

main.o : main.cpp queen.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

queen.o : queen.cpp queen.hpp
	$(CXX) $(CXXFLAGS) -c queen.cpp

.PHONY : clean
clean :
	$(RM) task3 $(objects)
