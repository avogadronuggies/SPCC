import java.util.*;

class Triple {
    String op, arg1, arg2;

    public Triple(String op, String arg1, String arg2) {
        this.op = op; this.arg1 = arg1; this.arg2 = arg2;
    }

    @Override
    public String toString() {
        return "(" + op + ", " + arg1 + ", " + arg2 + ")";
    }
}

public class Triplee {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Triple> triples = new ArrayList<>();
        Map<String, String> resultToIndex = new HashMap<>();
        System.out.println("Enter 3-address code (e.g., x = a + b). Blank line to finish:");

        for (int index = 0;; index++) {
            String line = sc.nextLine().trim();
            if (line.isEmpty()) break;

            String[] parts = line.split("\\s*=\\s*");
            if (parts.length != 2 || parts[1].split("\\s+").length != 3) {
                System.out.println("Invalid format. Skipping: " + line);
                continue;
            }

            String[] rhs = parts[1].split("\\s+");
            triples.add(new Triple(rhs[1], resolve(rhs[0], resultToIndex), resolve(rhs[2], resultToIndex)));
            resultToIndex.put(parts[0].trim(), "(" + index + ")");
        }

        System.out.println("\nTriples Representation:");
        for (int i = 0; i < triples.size(); i++) System.out.println("[" + i + "] " + triples.get(i));
        sc.close();
    }

    private static String resolve(String operand, Map<String, String> map) {
        return map.getOrDefault(operand, operand);
    }
}
