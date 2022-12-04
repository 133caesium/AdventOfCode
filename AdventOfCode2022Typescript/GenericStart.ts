import { readFileSync } from 'fs';

class GenericClass {
    stringThing: string;
    numberThing: number;
   
    constructor(data: string) {
      this.stringThing = data;
    }
   
    toString(): string {
      return (
        `A string version of the object`
      )
    }
  }



function importData(): string[] {
    const rawFile = readFileSync('./Day0X/sample_input.txt', 'utf-8');
    const fileAsStringArray = rawFile.split("\r\n");
    return fileAsStringArray;
}

function solvePart1(data: string[]): number {
    return 0;
}

function solvePart2(data: string[]): number {
    return 0;           
}

const data = importData()
solvePart1(data)
solvePart2(data)


