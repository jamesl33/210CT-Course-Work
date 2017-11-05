CXX=g++
CXXFLAGS = --std=c++11
RM=rm -f
objects = main.o lorry.o material.o

Units : $(objects)
	$(CXX) $(CXXFLAGS) $(objects) -o Units

main.o : main.cpp ../../catch.hpp ../material.hpp ../lorry.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

lorry.o : ../lorry.cpp ../lorry.hpp
	$(CXX) $(CXXFLAGS) -c ../lorry.cpp

material.o : ../material.cpp ../material.hpp
	$(CXX) $(CXXFLAGS) -c ../material.cpp

.PHONY : clean
clean :
	$(RM) Units $(objects)
