class Solution1 {
    public List<String> generateParenthesis(int n) {
        List<String> allStr = new ArrayList<String>();
        gP(n, n, new char[2 * n], allStr);
        return allStr;

    }

    public void gP(int a, int b, char[] str, List<String> allStr) {
        if (a == 0) {
            while (b > 0) {
                str[str.length - b] = ')';
                b--;
            }

            allStr.add(String.valueOf(str));
        } else {
            int n = str.length - (a + b);
            if (a < b) {
                str[n] = '(';
                gP(a - 1, b, str, allStr);
                str[n] = ')';
                gP(a, b - 1, str, allStr);
            } else {
                str[n] = '(';
                gP(a - 1, b, str, allStr);
            }
        }
    }
}