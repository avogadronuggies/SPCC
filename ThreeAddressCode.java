import java.util.Scanner;

public class ThreeAddressCode {
    static int tempCount = 1;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter expression (e.g., x = (a + b) * (c - d)):");
        String input = sc.nextLine().replaceAll(" ", "");
        sc.close();
        if (!input.contains("=")) {
            System.out.println("Invalid input. Expected an assignment.");
            return;
        }

        String[] parts = input.split("=");
        String target = parts[0];
        String expr = parts[1];

        String tac = generateTAC(expr, target);
        System.out.println("\nThree Address Code:");
        System.out.println(tac);
    }

    static String generateTAC(String expr, String target) {
        // Handle expressions like (a+b)*(c-d)
        if (expr.startsWith("(") && expr.contains(")*(") && expr.endsWith(")")) {
            int mid = expr.indexOf(")*(");
            String left = expr.substring(1, mid);  // skip first '('
            String right = expr.substring(mid + 3, expr.length() - 1); // skip ")*(" and last ')'

            String t1 = "t" + tempCount++;
            String t2 = "t" + tempCount++;

            StringBuilder sb = new StringBuilder();
            sb.append(t1).append(" = ").append(left).append("\n");
            sb.append(t2).append(" = ").append(right).append("\n");
            sb.append(target).append(" = ").append(t1).append(" * ").append(t2);
            return sb.toString();
        }

        return "Unsupported or malformed expression.";
    }
}
