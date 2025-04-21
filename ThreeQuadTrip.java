import java.util.*;

class IntermediateCode {
    String op;
    String arg1;
    String arg2;
    String result;

    public IntermediateCode(String op, String arg1, String arg2, String result) {
        this.op = op;
        this.arg1 = arg1;
        this.arg2 = arg2;
        this.result = result;
    }
}

public class ThreeQuadTrip {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<IntermediateCode> quadruples = new ArrayList<>();
        List<IntermediateCode> triples = new ArrayList<>();
        Map<String, String> resultMap = new HashMap<>();

        System.out.println("Enter three-address code lines (e.g., x = a + b).");
        System.out.println("Press Enter on a blank line to finish input:");

        while (true) {
            String line = sc.nextLine().trim();
            if (line.isEmpty()) break;

            String[] parts = line.split("\\s*=\\s*|\\s+");
            if (parts.length >= 4) {
                String result = parts[0];
                String arg1 = parts[1];
                String op = parts[2];
                String arg2 = parts[3];

                // Add to Quadruples
                quadruples.add(new IntermediateCode(op, arg1, arg2, result));

                // Replace with previous references if available for triples
                if (resultMap.containsKey(arg1)) arg1 = resultMap.get(arg1);
                if (resultMap.containsKey(arg2)) arg2 = resultMap.get(arg2);

                triples.add(new IntermediateCode(op, arg1, arg2, null));
                resultMap.put(result, "(" + (triples.size() - 1) + ")");
            } else {
                System.out.println("Invalid line. Skipping: " + line);
            }
        }

        // Display Quadruples
        System.out.println("\nQuadruples Representation:");
        System.out.println("+-------+-------+-------+--------+");
        System.out.println("| Op    | Arg1  | Arg2  | Result |");
        System.out.println("+-------+-------+-------+--------+");

        for (IntermediateCode q : quadruples) {
            System.out.printf("| %-5s | %-5s | %-5s | %-6s |\n",
                              q.op, q.arg1, q.arg2, q.result);
        }

        System.out.println("+-------+-------+-------+--------+");

        // Display Triples
        System.out.println("\nTriples Representation:");
        System.out.println("+----+-------+-------+-------+");
        System.out.println("| No | Op    | Arg1  | Arg2 |");
        System.out.println("+----+-------+-------+-------+");

        for (int i = 0; i < triples.size(); i++) {
            IntermediateCode t = triples.get(i);
            System.out.printf("| %-2d | %-5s | %-5s | %-5s |\n",
                    i, t.op, t.arg1, t.arg2);
        }
        sc.close();
        System.out.println("+----+-------+-------+-------+");
    }
}

