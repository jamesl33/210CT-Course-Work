CXX=g++
RM=rm -f
objects = main.o cube.o

task4 : $(objects)
	$(CXX) -o task4 $(objects)

main.o : main.cpp ../catch.hpp cube.hpp
	$(CXX) -c main.cpp

cube.o : cube.cpp cube.hpp
	$(CXX) -c cube.cpp

.PHONY : clean
clean :
	$(RM) task4 $(objects)
