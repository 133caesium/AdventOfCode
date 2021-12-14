import java.util.ArrayList;

public class Day3 {


    public static void main(String[] args){
        ReadFile input = new ReadFile();
        input.loadFile();
        ArrayList<String> tobogganWorld = input.getListOfLines();
        input.closeFile();

        ArrayList<Toboggan> toboggans = new ArrayList<Toboggan>();

        toboggans.add(new Toboggan(1,1,tobogganWorld));
        toboggans.add(new Toboggan(3,1,tobogganWorld));
        toboggans.add(new Toboggan(5,1,tobogganWorld));
        toboggans.add(new Toboggan(7,1,tobogganWorld));
        toboggans.add(new Toboggan(1,2,tobogganWorld));

        long answer = 1;
        for (Toboggan tobo:toboggans) {
            answer = answer * tobo.countTreesOnRide();
            System.out.println("There are "+String.valueOf(tobo.countTreesOnRide())+" trees in run "+String.valueOf(toboggans.indexOf(tobo))+" giving a mutiple of "+answer);
        }

    }

}
