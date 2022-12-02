import { readFileSync } from 'fs';

class RockPaperScissorsRound {
    rounds: string[];
    finalScore: number;
   
    constructor(rounds: string[]) {
      this.rounds = rounds;
      this.finalScore = this.rounds.reduce((sum, current) => sum + this.evaluateRoundPart2(current), 0);
    }

    evaluateRoundPart1(round: string): number {
        let roundValue = 0;
        switch(round){
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
    }

    evaluateRoundPart2(round: string): number {
        let roundValue = 0;
        switch(round){
            // Ties
            case 'A Y':
                roundValue = 4;
                break;
            case 'B Y':
                roundValue = 5;
                break;
            case 'C Y':
                roundValue = 6;
                break;
            // Wins
            case 'A Z':
                roundValue = 8;
                break;
            case 'B Z':
                roundValue = 9;
                break;
            case 'C Z':
                roundValue = 7;
                break;
            // Losses
            case 'A X':
                roundValue = 3;
                break;
            case 'B X':
                roundValue = 1;
                break;
            case 'C X':
                roundValue = 2;
                break;
        }
        return roundValue;
    }
   
    toString() {
      return (`This set of scores has final score ${RPS.finalScore}`);
    }
  }

function importData(): string[] {
    const rawFile = readFileSync('./Day02/input.txt', 'utf-8');
    const fileAsStringArray = rawFile.split("\r\n")
    return fileAsStringArray
}

const data = importData()
console.log(data)
const RPS = new RockPaperScissorsRound(data)
console.log(RPS.toString())
