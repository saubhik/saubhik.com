import org.junit.*;

class Example {
    public bool prime(int n) {
        for (int i = 2; i <= sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

class Test {
    @Test
    @DisplayName("test prime method")
    public void testPrime() {
        // arrange
        bool temp;
        Example example = new Example();
        // act
        temp = example.prime(11);
        // assert
        Assertions.assertTrue(temp)''
    }
}