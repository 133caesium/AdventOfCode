import java.util.ArrayList;

public class Day2Java {

    private int depth = 0;
    private int distanceForward = 0;

    public static void main(String[] args){
        Day2Java app = new Day2Java();
        app.run();
    }

    public void run(){
        ReadFile input = new ReadFile();
        input.loadFile();
        ArrayList<String> moveStrings = input.getListOfLines();
        for (String moveString:moveStrings) {
            Move move = new Move(moveString);
            switch (move.getDirection()){
                case UP:
                    depth -= move.getMagnitude();
                    break;
                case DOWN:
                    depth += move.getMagnitude();
                    break;
                case FORWARD:
                    distanceForward += move.getMagnitude();
                    break;
                case BACKWARD:
                    distanceForward -= move.getMagnitude();
                    break;
            }
        }
        StringBuilder output = new StringBuilder("The final location is Distance Forward: ");
        output.append(distanceForward);
        output.append(" and Depth: ");
        output.append(depth);
        output.append("\nGiving an answer of: ");
        output.append((depth*distanceForward));
        System.out.println(output);

    }



}