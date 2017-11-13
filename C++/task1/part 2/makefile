CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o lorry.o material.o

task1p2 : $(objects)
	$(CXX) $(CXXFLAGS) $(objects) -o task1p2

main.o : main.cpp material.hpp lorry.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

lorry.o : lorry.cpp lorry.hpp
	$(CXX) $(CXXFLAGS) -c lorry.cpp

material.o : material.cpp material.hpp
	$(CXX) $(CXXFLAGS) -c material.cpp

.PHONY : clean
clean :
	$(RM) task1p2 $(objects)
