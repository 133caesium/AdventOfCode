public class Key {
    private long publicKey;
    private long subjectNumber = 2;
    private int loopSize;
    private final int modulus = 20201227;

    public Key(int publicKey){
        this.publicKey = publicKey;
    }

    public void setSubjectNumber(long subjectNumber) {
        this.subjectNumber = subjectNumber;
    }

    public void setPublicKey() {
        this.publicKey = generateTempPublicKey();
    }

    public void setLoopSize(int loopSize) {
        this.loopSize = loopSize;
    }

    public void scanLoopSize() {
        this.loopSize = 0;
        while (generateTempPublicKey() != publicKey) {
            this.loopSize++;
            if ((loopSize%100 000)==0) {
                System.out.println(loopSize);
            }
        }
    }

    public void scanSubjectNumber() {
        this.subjectNumber = 1;
        while (subjectNumber<modulus) {
            this.subjectNumber++;
            if (generateTempPublicKey()==publicKey) {
                System.out.println("SOLVED with subject number: "+String.valueOf(subjectNumber)+" and loop size: "+String.valueOf(loopSize));
            }
        }
        System.out.println("FAILED all subject numbers with loop size: "+String.valueOf(loopSize));
    }

    public void scanLoopAndSubject() {
        this.loopSize = 0;
        while (generateTempPublicKey() != publicKey) {
            System.out.println("Scanning subject numbers with loop size: "+String.valueOf(loopSize));
            this.loopSize++;
            scanSubjectNumber();
        }
        System.out.println("SOLVED with subject number: "+String.valueOf(subjectNumber)+" and loop size: "+String.valueOf(loopSize));
    }

    public long generateTempPublicKey() {
        long generatedKey = 1;
        for (int i = 0; i < loopSize; i++) {
            generatedKey = (generatedKey * subjectNumber) % modulus;
        }
        return generatedKey;
    }

    public long getPublicKey() {
        return publicKey;
    }

    public long getSubjectNumber() {
        return subjectNumber;
    }

    public int getLoopSize() {
        return loopSize;
    }

    public int getModulus() {
        return modulus;
    }
}
