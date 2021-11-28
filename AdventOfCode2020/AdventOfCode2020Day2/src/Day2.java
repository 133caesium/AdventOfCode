import java.util.ArrayList;

public class Day2 {

    public static void main(String[] args){
        ReadFile file = new ReadFile();
        file.loadFile();
        ArrayList<String> passwordList = file.getListOfLines();

        int validPasswordCount = 0;

        for (String password:passwordList) {
            northPolePassword passwordObject = new northPolePassword(password);
            if (passwordObject.checkPasswordValid()){
                validPasswordCount++;
            }
        }
        System.out.println(validPasswordCount);
        file.closeFile();
    }

}
