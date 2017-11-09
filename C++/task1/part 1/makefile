CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o

task1 : $(objects)
	$(CXX) $(CXXFLAGS) -o task1 $(objects)

main.o : main.cpp factorial.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp

.PHONY : clean
clean :
	$(RM) task1 $(objects)
