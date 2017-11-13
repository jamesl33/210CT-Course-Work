CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o

task4p2 : $(objects)
	$(CXX) $(CXXFLAGS) -o task4p2 $(objects)

main.o : main.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp

.PHONY : clean
clean :
	$(RM) task4p2 $(objects)
