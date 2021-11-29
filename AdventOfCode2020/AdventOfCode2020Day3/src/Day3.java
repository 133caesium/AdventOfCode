import java.util.ArrayList;

public class Day3 {


    public static void main(String[] args){
        ReadFile input = new ReadFile();
        input.loadFile();
        ArrayList<String> tobogganWorld = input.getListOfLines();
        input.closeFile();

        Toboggan toboggan = new Toboggan(3,1,tobogganWorld);

        System.out.println(toboggan.countTreesOnRide());

    }

}
