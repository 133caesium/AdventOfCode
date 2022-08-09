import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.ArrayList;
import java.util.Scanner; // Import the Scanner class to read text files

public class ReadFile {


    private Scanner myReader;
    private ArrayList<String> file_contents;

    public ReadFile(){
        loadFile(false);
        this.file_contents = getListOfLines();
        closeFile();
    }

    public ReadFile(boolean test){
        loadFile(test);
        this.file_contents = getListOfLines();
        closeFile();
    }

    private void loadFile(boolean test){
        String pathname = "./resources/input.txt";
        if (test) {
            pathname = "./resources/test_input.txt";
        }
        try {
            File myObj = new File(pathname);
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

    private ArrayList<String> getListOfLines(){
        ArrayList<String> lineList = new ArrayList<String>();
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            lineList.add(data);
        }
        return lineList;
    }

    private void closeFile(){
        myReader.close();
    }

    public ArrayList<String> getFile_contents() {
        return file_contents;
    }

}
