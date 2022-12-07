import { readFileSync } from 'fs';

class CrateStacks {
  stackData: string[] = [];
  numberOfStacks: number;
  tallestStack: number;
  stacks: string[][] = [];
  moves: string[] = [];

  constructor(data: string[]) {
    this.extractStackData(data);
    this.numberOfStacks = (this.stackData[0].length + 1) / 4;
    this.tallestStack = this.stackData.length;
    this.convertStringsToStackArray();
  }

  move(movesTotal: number, from: number, to: number): void {
    for (let move = 0; move < movesTotal; move++) {
      this.stacks[to].push(this.stacks[from].pop() ?? ' ');
    }
  }

  move2(movesTotal: number, from: number, to: number): void {
    const tempStack: string[] = [];
    for (let move = 0; move < movesTotal; move++) {
      tempStack.push(this.stacks[from].pop() ?? ' ');
    }
    for (let move = 0; move < movesTotal; move++) {
      this.stacks[to].push(tempStack.pop() ?? ' ');
    }
  }

  extractStackData(data): void {
    for (const line of data) {
      if (line === '') {
        break;
      }
      this.stackData.push(line);
    }
  }

  convertStringsToStackArray(): void {
    for (let stack = 0; stack < this.numberOfStacks; stack++) {
      const newStack: string[] = [];
      for (
        let crateLevel = this.tallestStack - 1;
        crateLevel > -1;
        crateLevel--
      ) {
        if (this.stackData[crateLevel].charAt(1 + 4 * stack) === ' ') {
          break;
        } else {
          newStack.push(this.stackData[crateLevel][1 + 4 * stack]);
        }
      }
      this.stacks.push(newStack);
    }
  }

  display(): void {
    for (const line of this.stackData) {
      console.log(`${line.length}:${line}`);
    }
    console.log(this.stacks);
  }
}

function printStack(carateStack: CrateStacks): void {
  for (const stack of carateStack.stacks) {
    const outputCharacter = stack.pop();
    process.stdout.write(
      outputCharacter !== undefined ? outputCharacter : '[ERROR}'
    );
  }
  console.log('');
}

function importData(): string[] {
  const rawFile = readFileSync('./Day05/input.txt', 'utf-8');
  const fileAsStringArray = rawFile.split('\r\n');
  return fileAsStringArray;
}

function solvePart1(data: string[]): void {
  const stacks = new CrateStacks(data);
  for (const line of data) {
    if (line.startsWith('move')) {
      const moveArray = line.split(' ');
      stacks.move(
        parseInt(moveArray[1]),
        parseInt(moveArray[3]) - 1,
        parseInt(moveArray[5]) - 1
      );
    }
  }
  printStack(stacks);
}

function solvePart2(data: string[]): void {
  const stacks = new CrateStacks(data);
  for (const line of data) {
    if (line.startsWith('move')) {
      const moveArray = line.split(' ');
      stacks.move2(
        parseInt(moveArray[1]),
        parseInt(moveArray[3]) - 1,
        parseInt(moveArray[5]) - 1
      );
    }
  }
  printStack(stacks);
}

const data = importData();
solvePart1(data);
solvePart2(data);
