package main.java.Calculator;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    private static Calculator c;
    static void setUp(){
        c = new Calculator();
    }

    @org.junit.jupiter.api.Test
    void sum() {

        assertEquals( 0, c.sum(10, 20));
    }

    @org.junit.jupiter.api.Test
    void subtract() {

        assertEquals( -10, c.subtract(10, 20));

    }

    @Test
    void multiply() {
    }

    @Test
    void divide() {
    }
}