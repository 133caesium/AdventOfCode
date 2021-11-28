public class northPolePassword {
    private char policyChar;
    private int ruleIndexAlpha;
    private int ruleIndexBeta;
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
        this.ruleIndexAlpha = Integer.parseInt(rawPassword.substring(0,dashIndex));
        this.ruleIndexBeta = Integer.parseInt(rawPassword.substring(dashIndex+1,colonIndex-2));
        this.password = rawPassword.substring(colonIndex+2);
        this.isValid = checkPasswordValidTobogganRule();
    }

    public boolean checkPasswordValidSledRule(){
        int characterCount = 0;
        boolean valid = false;
        for (int letterIndex = 0; letterIndex < this.password.length(); letterIndex++) {
            if (this.password.charAt(letterIndex)==this.policyChar){
                characterCount++;
            }
        }
        if (ruleIndexAlpha <=characterCount && characterCount<= ruleIndexBeta){
            valid = true;
        }
        return valid;
    }

    public boolean checkPasswordValidTobogganRule(){
        int characterCount = 0;
        boolean valid = false;
        if (this.password.charAt(ruleIndexAlpha-1)==policyChar ^ this.password.charAt(ruleIndexBeta-1)==policyChar){
            valid = true;
        }
        return valid;
    }

    public char getPolicyChar() {
        return policyChar;
    }

    public int getRuleIndexAlpha() {
        return ruleIndexAlpha;
    }

    public int getMaximumOccurance() {
        return ruleIndexBeta;
    }

    public String getPassword() {
        return password;
    }

    public boolean isValid() {
        return isValid;
    }
}
