import { readFileSync } from 'fs';

function importData(): string[] {
  const rawFile = readFileSync('./Day10/input.txt', 'utf-8');
  const fileAsStringArray = rawFile.split('\r\n');
  return fileAsStringArray;
}

class InstructionReader {
  xValues: number[] = [1];
  instructions: number[] = [];
  signalStrength: number[] = [];

  constructor(data: string[]) {
    let extraSpaces = 0;
    for (
      let instructionCount = 0;
      instructionCount < data.length;
      instructionCount++
    ) {
      const instruction = data[instructionCount].split(' ');
      if (instruction[0] === 'addx') {
        extraSpaces++;
        this.instructions[instructionCount + extraSpaces + 1] = parseInt(
          instruction[1]
        );
      }
    }

    for (
      let instructionCount = 1;
      instructionCount <= this.instructions.length;
      instructionCount++
    ) {
      if (this.instructions[instructionCount] === undefined) {
        this.xValues[instructionCount] = this.xValues[instructionCount - 1];
      } else {
        this.xValues[instructionCount] =
          this.instructions[instructionCount] +
          this.xValues[instructionCount - 1];
      }
    }
    for (let signal = 0; signal < this.xValues.length; signal++) {
      this.signalStrength[signal] = this.xValues[signal] * (signal + 1);
    }
  }

  toString(): string {
    return `A string version of the object`;
  }
}

function solvePart1(instructions: InstructionReader): number {
  let finalAnswer = 0;
  for (
    let signalReading = 19;
    signalReading < instructions.signalStrength.length;
    signalReading += 40
  ) {
    console.log(
      `Taking reading at ${signalReading} of ${instructions.signalStrength[signalReading]}`
    );
    finalAnswer += instructions.signalStrength[signalReading];
  }
  console.log(`The sum of the signal strengths is ${finalAnswer}`);
  return finalAnswer;
}

function solvePart2(instructions: InstructionReader): number {
  for (
    let signalReading = 0;
    signalReading < instructions.signalStrength.length;
    signalReading += 1
  ) {
    // console.log(`Taking reading at ${signalReading} of ${instructions.signalStrength[signalReading]}`)
    if (signalReading % 40 === 0) {
      process.stdout.write(`\n`);
    }
    process.stdout.write(
      Math.abs(instructions.xValues[signalReading] - (signalReading % 40)) < 2
        ? '#'
        : '.'
    );
  }
  return 0;
}

const data = importData();
const instructions = new InstructionReader(data);
solvePart1(instructions);
solvePart2(instructions);
