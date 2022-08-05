import java.util.ArrayList;

public class Day3Refactor {
    private ArrayList<String> inputStrings;
    private ArrayList<DiagnosticNumber> diagnosticNumbers;
    private int diagnosticNumberLength;
    private int diagnosticNumberCount;

    public Day3Refactor() {
        this.diagnosticNumbers = new ArrayList<>();
        populateDiagnosticsLists();
        diagnosticNumberLength = diagnosticNumbers.get(0).getDiagnosticNumber().length;
        diagnosticNumberCount = diagnosticNumbers.size();
    }

    public void run() {
        System.out.println("We have created " + diagnosticNumbers.size() + " diagnostic numbers");
        System.out.println("Part one answer is " + getEpsilonAsInt() * getGammaAsInt());
        System.out.println("Part two answer is " + getOxygenAsInt() * getCarbonAsInt());
    }

    public void populateDiagnosticsLists() {
        ReadFile day3input = new ReadFile(false);
        this.inputStrings = day3input.getFile_contents();
        for (String inputString : inputStrings) {
            diagnosticNumbers.add(new DiagnosticNumber(inputString));
        }
    }

    /**
     * Calculates the gamma number.
     *
     * @return a binary array of the most common values in the list of diagnostic numbers
     */
    public boolean[] getGamma() {
        boolean[] mostCommonDiagnonsticDigits = new boolean[diagnosticNumberLength];
        for (int i = 0; i < diagnosticNumberLength; i++) {
            mostCommonDiagnonsticDigits[i] = getMostCommonBitAtIndex(i);
        }
        return mostCommonDiagnonsticDigits;
    }

    public boolean[] getEpsiolon() {
        boolean[] leastCommonDiagnonsticDigits = getGamma();
        for (int i = 0; i < diagnosticNumberLength; i++) {
            leastCommonDiagnonsticDigits[i] = !leastCommonDiagnonsticDigits[i];
        }
        return leastCommonDiagnonsticDigits;
    }

    public DiagnosticNumber getOxygenRating() {
        ArrayList<DiagnosticNumber> possibleOxygenRatings = (ArrayList<DiagnosticNumber>) diagnosticNumbers.clone();
        for (int i = 0; i < diagnosticNumberLength; i++) {
            boolean value = getMostCommonBitAtIndex(i, possibleOxygenRatings);
            int finalI = i;
            possibleOxygenRatings.removeIf(number -> (number.getDiagnosticNumber()[finalI] != value));
        }
        return possibleOxygenRatings.get(0);
    }

    public DiagnosticNumber getCarbonRating() {
        ArrayList<DiagnosticNumber> possibleCarbonRatings = (ArrayList<DiagnosticNumber>) diagnosticNumbers.clone();
        for (int i = 0; i < diagnosticNumberLength; i++) {
            boolean value = getMostCommonBitAtIndex(i, possibleCarbonRatings);
            for (DiagnosticNumber possibleCarbonRating : possibleCarbonRatings) {
                if (possibleCarbonRating.getDiagnosticNumber()[i] != value) {
                    int finalI = i;
                    possibleCarbonRatings.removeIf(number -> (number.getDiagnosticNumber()[finalI] == value));
                    break;
                }
            }
        }
        return possibleCarbonRatings.get(0);
    }

    public int getGammaAsInt() {
        int gammaInt = binaryArrayToInt(getGamma());
        System.out.println("Calculating gamma as " + gammaInt);
        return gammaInt;
    }

    public int getEpsilonAsInt() {
        int epsilonInt = binaryArrayToInt(getEpsiolon());
        System.out.println("Calculating epsilon as " + epsilonInt);
        return epsilonInt;
    }

    public int getOxygenAsInt() {
        int OxygenInt = binaryArrayToInt(getOxygenRating().getDiagnosticNumber());
        System.out.println("Calculating Oxygen as " + OxygenInt);
        return OxygenInt;
    }

    public int getCarbonAsInt() {
        int CarbonInt = binaryArrayToInt(getCarbonRating().getDiagnosticNumber());
        System.out.println("Calculating Carbon as " + CarbonInt);
        return CarbonInt;
    }

    public int binaryArrayToInt(boolean[] binaryArray) {
        int value = 0;
        int powerOfTwo = 1;
        for (int i = binaryArray.length - 1; i >= 0; i--) {
            if (binaryArray[i]) {
                value += powerOfTwo;
            }
            powerOfTwo *= 2;
        }
        return value;
    }

    public boolean getMostCommonBitAtIndex(int index) {
        return getMostCommonBitAtIndex(index, diagnosticNumbers);
    }

    public boolean getMostCommonBitAtIndex(int index, ArrayList<DiagnosticNumber> numbers) {
        boolean mostCommonBit = false;
        int countTrues = 0;
        for (DiagnosticNumber number : numbers) {
            if (number.getDiagnosticNumber()[index]) {
                countTrues++;
            }
        }
        if (countTrues * 2 >= numbers.size()) {
            mostCommonBit = true;
        }
        return mostCommonBit;
    }

//    public void runOld() {
//        ReadFile day3input = new ReadFile();
//        this.inputStrings = day3input.getFile_contents();
//        String gamma = buildGamma();
//        String epsilon = buildEpsilon();
//        String oxygen = buildOxygenRating();
//        String carbon = buildCarbonRating();
//
//        int gammaValue = binaryStringToInt(gamma);
//        int epsilonValue = binaryStringToInt(epsilon);
//        int oxygenValue = binaryStringToInt(oxygen);
//        int carbonValue = binaryStringToInt(carbon);
//        System.out.println("Gamma: "+gamma+" which is decimal: "+String.valueOf(gammaValue));
//        System.out.println("Epsilon: "+epsilon+" which is decimal: "+String.valueOf(epsilonValue));
//        System.out.println("Answer: "+String.valueOf((gammaValue*epsilonValue)));
//        System.out.println("Oxygen: "+oxygen+" which is decimal: "+String.valueOf(oxygenValue));
//        System.out.println("Carbon: "+carbon+" which is decimal: "+String.valueOf(carbonValue));
//        System.out.println("Answer: "+String.valueOf((carbonValue*oxygenValue)));
//    }
//
//    public void printInput() {
//        for (String line: inputStrings) {
//            System.out.println(line);
//        }
//    }

//    public String getMostCommonBit(ArrayList<String> setOfStrings, int bitIndex) {
//        int sum = 0;
//        int threshold = inputStrings.size()/2;
//        for (String line:inputStrings) {
//            sum += Integer.parseInt(line.substring(bitIndex,bitIndex+1));
//        }
//        if (sum<threshold) {
//            return "0";
//        } else if (sum==threshold && (inputStrings.size()%2==0)){
//            return "T";
//        } else {
//            return "1";
//        }
//    }

//    public String buildGamma() {
//        int outputLength = inputStrings.get(0).length();
//        StringBuilder gamma = new StringBuilder();
//        for (int bitIndex = 0; bitIndex < outputLength; bitIndex++) {
//            gamma.append(getMostCommonBit(inputStrings, bitIndex));
//        }
//        return gamma.toString();
//    }

//    public String buildEpsilon() {
//        String gamma = buildGamma();
//        StringBuilder epsilon = new StringBuilder();
//        for (int bitIndex = 0; bitIndex < gamma.length(); bitIndex++) {
//            if (gamma.charAt(bitIndex) == '0') {
//                epsilon.append("1");
//            } else {
//                epsilon.append("0");
//            }
//        }
//        return epsilon.toString();
//    }
//
//    public String buildOxygenRating() {
//        int outputLength = inputStrings.get(0).length();
//        ArrayList<String> possibleOxygenRatings = (ArrayList) inputStrings.clone();
//        for (int bitIndex = 0; bitIndex < outputLength; bitIndex++) {
//            char mostCommonBit = getMostCommonBit(possibleOxygenRatings, bitIndex).charAt(0);
//
//            int finalBitIndex = bitIndex;
//            if (mostCommonBit=='T') {
//                possibleOxygenRatings.removeIf(possibleRating -> (possibleRating.charAt(finalBitIndex)=='0'));
//            } else if (possibleOxygenRatings.size()==1) {
//                break;
//            } else {
//                possibleOxygenRatings.removeIf(possibleRating -> (possibleRating.charAt(finalBitIndex) != mostCommonBit));
//            }
//        }
//        return possibleOxygenRatings.get(0);
//    }
//
//    public String buildCarbonRating() {
//        int outputLength = inputStrings.get(0).length();
//        ArrayList<String> possibleCarbonRatings = (ArrayList) inputStrings.clone();
//        for (int bitIndex = 0; bitIndex < outputLength; bitIndex++) {
//            char mostCommonBit = getMostCommonBit(possibleCarbonRatings, bitIndex).charAt(0);
//            int finalBitIndex = bitIndex;
//            if (mostCommonBit=='T') {
//                possibleCarbonRatings.removeIf(possibleRating -> (possibleRating.charAt(finalBitIndex)=='1'));
//            } else if (possibleCarbonRatings.size()==1) {
//                break;
//            } else {
//                possibleCarbonRatings.removeIf(possibleRating -> (possibleRating.charAt(finalBitIndex) == mostCommonBit));
//            }
//        }
//        return possibleCarbonRatings.get(0);
//    }
//
//    public int binaryStringToInt(String binaryNumberAsString) {
//        return Integer.parseInt(binaryNumberAsString, 2);
//    }

    public static void main(String[] args) {
        new Day3Refactor().run();
    }

}