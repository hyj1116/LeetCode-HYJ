public class Add_Binary {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1, j = b.length() - 1, carry = 0;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (i >= 0) {
                int n = a.charAt(i);
                System.out.println("i = " + i);
                System.out.println("n = " + n);
                n = a.charAt(i--);
                System.out.println("i = " + i);
                System.out.println("n = " + n);
                int zero = '0';
                System.out.println("zero = " + zero);
                sum = sum + n - zero;
                System.out.println("sum = " + sum);
            }
            if (j >= 0) {
                System.out.println(b.charAt(j));
                sum += b.charAt(j--) - '0';
            }
            sb.append(sum % 2);
            System.out.println("sb = " + sb);
            carry = sum / 2;
        }
        if (carry != 0)
            sb.append(carry);
        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        Add_Binary ins = new Add_Binary();
        System.out.println(ins.addBinary("1", "11"));
    }
}