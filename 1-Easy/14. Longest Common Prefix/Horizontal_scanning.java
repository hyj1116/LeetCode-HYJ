public class Horizontal_scanning {

    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0)
            return "";
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++)
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty())
                    return "";
            }
        return prefix;
    }

    public static void main(String[] args) {
        String[] strs = { "flower", "flow", "flight" };
        System.out.println(strs[1].indexOf(strs[0]));
        Horizontal_scanning horizontal_scanning = new Horizontal_scanning();
        System.out.println(horizontal_scanning.longestCommonPrefix(strs));
    }
}