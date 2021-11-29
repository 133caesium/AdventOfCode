import java.util.ArrayList;

public class Toboggan {
    public final char openSquare = '.';
    public final char treeSquare = '#';

    private int right;
    private int down;
    private int startingIndex;
    private ArrayList<String> tobogganWorld;
    private int steps;
    private int trees;
    private int fields;

    public Toboggan(int right, int down, ArrayList<String> tobogganWorld) {
        this.right = right;
        this.down = down;
        this.tobogganWorld = tobogganWorld;
        this.startingIndex = setStartingIndex(tobogganWorld.get(0));
    }

    public int countTreesOnRide() {
        steps = 0;
        trees = 0;
        fields = 0;
        int position = startingIndex;
        for (String line:tobogganWorld) {
            steps++;
            if (line.charAt(position)==treeSquare){
                trees++;
            } else {
                fields ++;
            }
            position = (position+right) % line.length();
        }
        return trees;
    }

    private int setStartingIndex(String startingLine){
        boolean indexFound = false;
        return startingLine.indexOf('.');
    }

}
