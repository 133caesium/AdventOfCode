public class northPolePassword {
    private char policyChar;
    private int minimumOccurance;
    private int maximumOccurance;
    private String password;
    private boolean isValid;

    /*
    This class captures a password as described by Day 2 of Advent of Code 2020.
    1-3 a: abcde
     */
    public northPolePassword(String rawPassword) {
        int dashIndex = rawPassword.indexOf("-");
        int colonIndex = rawPassword.indexOf(":");
        this.policyChar = rawPassword.charAt(colonIndex-1);
        this.minimumOccurance = Integer.parseInt(rawPassword.substring(0,dashIndex));
        this.maximumOccurance = Integer.parseInt(rawPassword.substring(dashIndex+1,colonIndex-2));
        this.password = rawPassword.substring(colonIndex+2);
        this.isValid = checkPasswordValid();
    }

    public boolean checkPasswordValid(){
        int characterCount = 0;
        boolean valid = false;
        for (int letterIndex = 0; letterIndex < this.password.length(); letterIndex++) {
            if (this.password.charAt(letterIndex)==this.policyChar){
                characterCount++;
            }
        }
        if (minimumOccurance<=characterCount && characterCount<=maximumOccurance){
            valid = true;
        }
        return valid;
    }

    public char getPolicyChar() {
        return policyChar;
    }

    public int getMinimumOccurance() {
        return minimumOccurance;
    }

    public int getMaximumOccurance() {
        return maximumOccurance;
    }

    public String getPassword() {
        return password;
    }

    public boolean isValid() {
        return isValid;
    }
}
