import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner; // Import the Scanner class to read text files

public class ReadFile {
    Scanner myReader;

    public ReadFile(){
    }

    public void loadFile(){
        try {
            File myObj = new File("./resources/input.txt");
            myReader = new Scanner(myObj);
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
            e.printStackTrace();
        }
    }

    public void printFileToConsole(){
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            System.out.println(data);
        }
    }

    public String getNextLine(){
        String nextLine = myReader.nextLine();
        return nextLine;
    }

    public ArrayList<String> getListOfLines(){
        ArrayList<String> lineList = new ArrayList<String>();
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            lineList.add(data);
        }
        return lineList;
    }

    public void closeFile(){
        myReader.close();
    }
}