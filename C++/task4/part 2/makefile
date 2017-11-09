CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o

task5p2 : $(objects)
	$(CXX) $(CXXFLAGS) -o task5p2 $(objects)

main.o : main.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp

.PHONY : clean
clean :
	$(RM) task5p2 $(objects)
