#include <iostream>

long factorial(long n) {
        /*
             input:
             long n: number which you want the factorial of
             output:
             long: returns n!
             */
        if (n == 0) {
                return 1;
        } else {
                return n * factorial(n - 1);
        }
}

bool test_if_divides(int a, int b) {
        /*
             input:
             int a: number we calculate the factorial of and then is tested if divides by 'b' equally
             int b: a!' is divided by this number
             output:
             bool: boolean representing whether '(a! / b) == 0'
             */
        if (factorial(a) % b) {
                std::cout << b << " does not divide by " << a << "!" << std::endl;
                return false;
        } else {
                std::cout << b << " does divide by " << a << "!" << std::endl;
                return true;
        }
}
