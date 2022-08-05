public class DiagnosticNumber {
    boolean[] diagnosticNumber;


    public DiagnosticNumber(String inputNumberString) {
        int inputNumberLength = inputNumberString.length();
        this.diagnosticNumber = new boolean[inputNumberLength];
        for (int i = 0; i < inputNumberLength; i++) {
            this.diagnosticNumber[i] = inputNumberString.charAt(i)=='1';
        }
    }

    public boolean[] getDiagnosticNumber() {
        return diagnosticNumber;
    }

    public void setDiagnosticNumber(boolean[] diagnosticNumber) {
        this.diagnosticNumber = diagnosticNumber;
    }
}
