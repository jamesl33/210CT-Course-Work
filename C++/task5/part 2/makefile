CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o linked_list.o

task6p2 : $(objects)
	$(CXX) $(CXXFLAGS) $(objects) -o task6p2

main.o : main.cpp linked_list.hpp node.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

linked_list.o : linked_list.cpp linked_list.hpp node.hpp
	$(CXX) $(CXXFLAGS) -c linked_list.cpp

.PHONY : clean
clean :
	$(RM) task6p2 $(objects)
