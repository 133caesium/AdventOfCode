import java.awt.*;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Move {

    public enum Direction {
        FORWARD,
        BACKWARD,
        UP,
        DOWN
    }

    private Direction direction;
    private int magnitude;

    public Move(String moveString) {
        Pattern directionRegex = Pattern.compile("[a-z]+");
        Pattern magnitudeRegex = Pattern.compile("\\d+");
        Matcher directionMatcher = directionRegex.matcher(moveString);
        Matcher magnitudeMatcher = magnitudeRegex.matcher(moveString);
        directionMatcher.find();
        magnitudeMatcher.find();
        String directionString = directionMatcher.group();
        if (directionString.equals("up")) {
            this.direction = Direction.UP;
        } else if (directionString.equals("down")) {
            this.direction = Direction.DOWN;

        } else if (directionString.equals("forward")) {
            this.direction = Direction.FORWARD;
        } else {
            this.direction = null;
            throw new InputMismatchException("No valid direction");
        }
        this.magnitude = Integer.parseInt(magnitudeMatcher.group());
    }

    public Direction getDirection() {
        return direction;
    }

    public int getMagnitude() {
        return magnitude;
    }
}
