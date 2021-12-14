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
        trees = 0;
        fields = 0;
        int position = startingIndex;
        for (int steps = 0; steps < tobogganWorld.size(); steps+=down) {
            if (tobogganWorld.get(steps).charAt(position)==treeSquare){
                trees++;
            } else {
                fields ++;
            }
            position = (position+right) % tobogganWorld.get(steps).length();
        }
        return trees;
    }

    private int setStartingIndex(String startingLine){
        return startingLine.indexOf('.');
    }

}
