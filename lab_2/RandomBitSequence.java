import java.util.Random;

public class RandomBitSequence {
    public static void main(String[] args) {
        Random random = new Random();
        final int SIZE = 128;

        // Генерация 128 битовой последовательности из 0 и 1 с использованием массива boolean
        boolean[] randomBits = new boolean[SIZE];
        for (int i = 0; i < 128; i++) {
            randomBits[i] = random.nextBoolean();
        }

        // Вывод битовой последовательности в консоль
        for (boolean bit : randomBits) {
            System.out.print(bit ? "1" : "0");
        }
        System.out.println();
    }
}