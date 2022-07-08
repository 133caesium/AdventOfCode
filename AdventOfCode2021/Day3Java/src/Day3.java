import java.util.ArrayList;

public class Day3 {
    private ArrayList<String> inputStrings;

    public void run() {
        ReadFile day3input = new ReadFile();
        this.inputStrings = day3input.getFile_contents();
        String gamma = buildGamma();
        String epsilon = buildEpsilon();
        String oxygen = buildOxygenRating();
        String carbon = buildCarbonRating();

        int gammaValue = binaryStringToInt(gamma);
        int epsilonValue = binaryStringToInt(epsilon);
        int oxygenValue = binaryStringToInt(oxygen);
        int carbonValue = binaryStringToInt(carbon);
        System.out.println("Gamma: "+gamma+" which is decimal: "+String.valueOf(gammaValue));
        System.out.println("Epsilon: "+epsilon+" which is decimal: "+String.valueOf(epsilonValue));
        System.out.println("Answer: "+String.valueOf((gammaValue*epsilonValue)));
        System.out.println("Oxygen: "+oxygen+" which is decimal: "+String.valueOf(oxygenValue));
        System.out.println("Carbon: "+carbon+" which is decimal: "+String.valueOf(carbonValue));
        System.out.println("Answer: "+String.valueOf((carbonValue*oxygenValue)));
    }

    public void printInput() {
        for (String line: inputStrings) {
            System.out.println(line);
        }
    }

    public String getMostCommonBit(ArrayList<String> setOfStrings, int bitIndex) {
        int sum = 0;
        int threshold = inputStrings.size()/2;
        for (String line:inputStrings) {
            sum += Integer.parseInt(line.substring(bitIndex,bitIndex+1));
        }
        if (sum<threshold) {
            return "0";
        } else if (sum==threshold && (inputStrings.size()%2==0)){
            return "T";
        } else {
            return "1";
        }
    }

    public String buildGamma() {
        int outputLength = inputStrings.get(0).length();
        StringBuilder gamma = new StringBuilder();
        for (int bitIndex = 0; bitIndex < outputLength; bitIndex++) {
            gamma.append(getMostCommonBit(inputStrings, bitIndex));
        }
        return gamma.toString();
    }

    public String buildEpsilon() {
        String gamma = buildGamma();
        StringBuilder epsilon = new StringBuilder();
        for (int bitIndex = 0; bitIndex < gamma.length(); bitIndex++) {
            if (gamma.charAt(bitIndex) == '0') {
                epsilon.append("1");
            } else {
                epsilon.append("0");
            }
        }
        return epsilon.toString();
    }

    public String buildOxygenRating() {
        int outputLength = inputStrings.get(0).length();
        ArrayList<String> possibleOxygenRatings = (ArrayList) inputStrings.clone();
        for (int bitIndex = 0; bitIndex < outputLength; bitIndex++) {
            char mostCommonBit = getMostCommonBit(possibleOxygenRatings, bitIndex).charAt(0);

            int finalBitIndex = bitIndex;
            if (mostCommonBit=='T') {
                possibleOxygenRatings.removeIf(possibleRating -> (possibleRating.charAt(finalBitIndex)=='0'));
            } else if (possibleOxygenRatings.size()==1) {
                break;
            } else {
                possibleOxygenRatings.removeIf(possibleRating -> (possibleRating.charAt(finalBitIndex) != mostCommonBit));
            }
        }
        return possibleOxygenRatings.get(0);
    }

    public String buildCarbonRating() {
        int outputLength = inputStrings.get(0).length();
        ArrayList<String> possibleCarbonRatings = (ArrayList) inputStrings.clone();
        for (int bitIndex = 0; bitIndex < outputLength; bitIndex++) {
            char mostCommonBit = getMostCommonBit(possibleCarbonRatings, bitIndex).charAt(0);
            int finalBitIndex = bitIndex;
            if (mostCommonBit=='T') {
                possibleCarbonRatings.removeIf(possibleRating -> (possibleRating.charAt(finalBitIndex)=='1'));
            } else if (possibleCarbonRatings.size()==1) {
                break;
            } else {
                possibleCarbonRatings.removeIf(possibleRating -> (possibleRating.charAt(finalBitIndex) == mostCommonBit));
            }
        }
        return possibleCarbonRatings.get(0);
    }

    public int binaryStringToInt(String binaryNumberAsString) {
        return Integer.parseInt(binaryNumberAsString, 2);
    }

    public static void main(String[] args) {
        new Day3().run();
    }

}
