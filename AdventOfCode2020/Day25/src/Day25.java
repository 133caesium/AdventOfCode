public class Day25 {

    public static void main(String[] args){
        Day25 main = new Day25();
        main.decrypt(17807724, 5764801);
        main.decrypt(15733400, 6408062);
    }

    public void decrypt(int cardPublicKey, int doorPublicKey) {
        Key doorKey = new Key(cardPublicKey);
        Key cardKey = new Key(doorPublicKey);
        doorKey.setSubjectNumber(7);
        cardKey.setSubjectNumber(7);
        System.out.println(getLoopSizeOfKey(cardKey));
        System.out.println(getLoopSizeOfKey(doorKey));
        System.out.println(generateEncryptionKey(cardKey,doorKey));
        System.out.println(generateEncryptionKey(doorKey,cardKey));
    }

    public int getLoopSizeOfKey(Key key) {
//        key.scanLoopAndSubject();
        key.scanLoopSize();
        return key.getLoopSize();
    }

    public long generateEncryptionKey(Key card, Key door) {
        Key encrpytion = new Key(1);
        encrpytion.setSubjectNumber(card.getPublicKey());
        encrpytion.setLoopSize(door.getLoopSize());
        encrpytion.setPublicKey();
        return encrpytion.getPublicKey();
    }


}
