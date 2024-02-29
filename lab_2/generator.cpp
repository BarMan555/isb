#include <iostream>
#include <random>
#include <array>

#define SIZE 128

void generator()
{
    // Генератор случайных чисел
    std::random_device rd;
    std::mt19937 gen(rd());

    // Генерация 128 битовой псевдослучайной последовательности
    std::array<bool, SIZE> randomBits;
    for (int i = 0; i < 128; ++i) 
    {
        randomBits[i] = gen() % 2;
        std::cout << randomBits[i];
    }
}

int main() {
    generator();    
    return 0;
}
