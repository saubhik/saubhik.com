public class PrimitiveTypes {

    /*
    Count the number of bits that are set to 1.
    The time complexity is O(n) where n is the number of bits in x.
    We can improve on this.
    */
    public static short countBits(int x) {
        short numBits = 0;
        while (x != 0) {
            numBits += (x & 1);
            x >>>= 1;
        }
        return numBits;
    }

    /*
    Compute the parity of a very large number of 64-bit words.
    The parity of a word is 1 is the parity of the number of 1s in the word
    Example: parity of 1011 is 1, and of 10001000 is 0.
    */

    /*
    Solution 1 - Brute Force
    Bitwise xor (^) can compute modulo 2.
    Time complexity is O(n), where n is the word size.
    */
    public static short parity1(long x) {
        short result = 0;
        while (x != 0) {
            result ^= (x & 1);
            x >>>= 1;
        }
        return result;
    }

    /*
    We can improve on the above.
    Remember that (x - 1) has 0 in the position of the least significant 1 in x, and 1s after that (if any).
    The previous entries are all same.
    Example:
    x:     ...10000
    x-1:   ...01111

    `x & (x - 1)` will remove only the least significant 1 from x, everything else same.
    
    So the below code has time complexity O(k) where k is the number of bits set to 1 in x.
    */
    public static short parity2(long x) {
        short result = 0;
        while (x != 0) {
            result ^= 1;
            x &= (x - 1);
        }
        return result;
    }

    /*
    But we need to solve the parity problem for a large number of words.
    We will:
    1. process multiple bits at a time
    2. cache results in an array-based lookup table

    We cannot cache parity of all 64-bit words. So we cache parity of all 16-bit words.
    As 2^16 = 65536 is relatively small.
    */
    public static short parity(long x) {
        final int WORD_SIZE = 16;
        final int BIT_MASK = 0xFFFF;
        return (short) (
            precomputedParity[(int)((x >>> (3 * WORD_SIZE)) & BIT_MASK)]
            ^ precomputedParity[(int)((x >>> (2 * WORD_SIZE)) & BIT_MASK)]
            ^ precomputedParity[(int)((x >>> WORD_SIZE) & BIT_MASK)]
            ^ precomputedParity[(int)(x & BIT_MASK)]);
    }

    public static void main(String[] args) {
        // check the functions
        System.out.println(countBits(15));
    }
}