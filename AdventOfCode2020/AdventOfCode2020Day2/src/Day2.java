public class Day2 {

    public static void main(String[] args){
        ReadFile file = new ReadFile();
        file.loadFile();
        System.out.println(file.getNextLine());
        System.out.println(file.getNextLine());
        file.closeFile();
    }

}
