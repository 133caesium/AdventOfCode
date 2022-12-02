"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = require("fs");
var RockPaperScissorsRound = /** @class */ (function () {
    function RockPaperScissorsRound(rounds) {
        var _this = this;
        this.rounds = rounds;
        this.finalScore = this.rounds.reduce(function (sum, current) { return sum + _this.evaluateRound(current); }, 0);
    }
    RockPaperScissorsRound.prototype.evaluateRound = function (round) {
        var roundValue = 0;
        switch (round) {
            // Ties
            case 'A X':
                roundValue = 4;
                break;
            case 'B Y':
                roundValue = 5;
                break;
            case 'C Z':
                roundValue = 6;
                break;
            // Wins
            case 'C X':
                roundValue = 7;
                break;
            case 'A Y':
                roundValue = 8;
                break;
            case 'B Z':
                roundValue = 9;
                break;
            // Losses
            case 'B X':
                roundValue = 1;
                break;
            case 'C Y':
                roundValue = 2;
                break;
            case 'A Z':
                roundValue = 3;
                break;
        }
        return roundValue;
    };
    RockPaperScissorsRound.prototype.toString = function () {
        return ("This set of scores has final score ".concat(RPS.finalScore));
    };
    return RockPaperScissorsRound;
}());
function importData() {
    var rawFile = (0, fs_1.readFileSync)('./Day02/input.txt', 'utf-8');
    var fileAsStringArray = rawFile.split("\r\n");
    // .map(str => {return parseInt(str)});
    return fileAsStringArray;
}
var data = importData();
console.log(data);
var RPS = new RockPaperScissorsRound(data);
console.log(RPS.toString());
//# sourceMappingURL=Day02.js.map