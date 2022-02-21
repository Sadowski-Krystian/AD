package main.java.Calculator;

public class Main {
    public static void main(String[] args) {
        Calculator c = new Calculator();
        System.out.println(c.sum(10, 20));
        System.out.println(c.subtract(10, 20));
        System.out.println(c.multiply(10, 20));
        System.out.println(c.divide(10, 20));
    }
}
