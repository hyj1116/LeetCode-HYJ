public class DP_Buttom_UP {
    public int climbStairs(int n) {
        int memo[] = new int[n + 1];
        return helper(0, n, memo);
    }

    public int helper(int i, int n, int memo[]) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        if (memo[i] > 0) {
            return memo[i];
        }
        memo[i] = helper(i + 1, n, memo) + helper(i + 2, n, memo);
        return memo[i];
    }

    public static void main(String[] args) {
        DP_Buttom_UP dButtom_UP = new DP_Buttom_UP();
        System.out.println(dButtom_UP.climbStairs(3));

    }
}