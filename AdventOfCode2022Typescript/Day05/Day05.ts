import { readFileSync } from 'fs';

class CrateStacks {
  stackData: string[] = [];
  numberOfStacks: number;
  tallestStack: number;
  stacks: string[][] = [];

  constructor(data: string[]) {
    this.extractStackData(data);
    this.numberOfStacks = (this.stackData[0].length+1)/4;
    this.tallestStack  = this.stackData.length;
    for (let stack = 0; stack<this.numberOfStacks; stack++) {
        console.log(`Creating stack ${stack}`)
        const newStack: string[] = [];
        for (let crateLevel = this.tallestStack-1; crateLevel > -1; crateLevel--) {
            if (this.stackData[crateLevel].charAt(1+4*stack)===' ') {
                console.log(`Blank space detected at stack:${stack} crateLevel:${crateLevel} `)
                break;
            } else {
            newStack.push(this.stackData[crateLevel][1+4*stack])
            }
        }
        this.stacks.push(newStack)
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

  display(): void {
    for (const line of this.stackData) {
      console.log(`${line.length}:${line}`);
    }
    // for (const line of this.stackData) {
        // console.log(`Extract ${line[1]},${line[5]},${line[9]}`)
    // }
    console.log(this.stacks)
  }
}

function importData(): string[] {
  const rawFile = readFileSync('./Day05/sample_input.txt', 'utf-8');
  const fileAsStringArray = rawFile.split('\r\n');
  return fileAsStringArray;
}

function solvePart1(data: string[]): number {
  return 0;
}

function solvePart2(data: string[]): number {
  return 0;
}

const data = importData();
const stacks = new CrateStacks(data);
stacks.display();

solvePart1(data);
solvePart2(data);
