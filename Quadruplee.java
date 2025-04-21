import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Quadruple {
    String op;
    String arg1;
    String arg2;
    String result;

    public Quadruple(String op, String arg1, String arg2, String result) {
        this.op = op;
        this.arg1 = arg1;
        this.arg2 = arg2;
        this.result = result;
    }

    @Override
    public String toString() {
        return String.format("| %-5s | %-5s | %-5s | %-6s |", op, arg1, arg2, result);
    }
}

public class Quadruplee {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Quadruple> quadruples = new ArrayList<>();

        System.out.println("Enter three-address code lines (e.g., t1 = a + b).");
        System.out.println("Press Enter on a blank line to stop:");

        while (true) {
            String line = sc.nextLine().trim();
            if (line.isEmpty()) break;

            // Split based on '=' and spaces
            String[] parts = line.split("\\s*=\\s*|\\s+");
            if (parts.length >= 4) {
                String result = parts[0];
                String arg1 = parts[1];
                String op = parts[2];
                String arg2 = parts[3];

                quadruples.add(new Quadruple(op, arg1, arg2, result));
            } else {
                System.out.println("Invalid format. Skipping: " + line);
            }
        }

        // Display quadruples
        System.out.println("\nQuadruples Representation:");
        System.out.println("+-------+-------+-------+--------+");
        System.out.println("| Op    | Arg1  | Arg2  | Result |");
        System.out.println("+-------+-------+-------+--------+");

        for (Quadruple q : quadruples) {
            System.out.println(q);
        }

        System.out.println("+-------+-------+-------+--------+");
        sc.close();
    }
}
