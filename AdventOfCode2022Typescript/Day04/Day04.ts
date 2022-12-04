import { readFileSync } from 'fs';

class ElfPair {
  elf1start: number;
  elf1end: number;
  elf2start: number;
  elf2end: number;
  anElfIsContained: boolean;

  constructor(data: string) {
    this.elf1start = parseInt(data.split(',')[0].split('-')[0]);
    this.elf1end = parseInt(data.split(',')[0].split('-')[1]);
    this.elf2start = parseInt(data.split(',')[1].split('-')[0]);
    this.elf2end = parseInt(data.split(',')[1].split('-')[1]);
    this.anElfIsContained = this.checkContainment();
  }

  checkContainment(): boolean {
    return (
      (this.elf1start <= this.elf2start && this.elf2end <= this.elf1end) ||
      (this.elf1start >= this.elf2start && this.elf2end >= this.elf1end)
    );
  }

  checkOverlap(): boolean {
    return (
      (this.elf1start <= this.elf2start && this.elf1end >= this.elf2start) ||
      (this.elf2start <= this.elf1start && this.elf2end >= this.elf1start)
    );
  }

  toString(): string {
    return (
      `A pair of elves who are cleaning:\n` +
      `${this.elf1start} to ${this.elf1end} and\n` +
      `${this.elf2start} to ${this.elf2end}\n` +
      (this.anElfIsContained
        ? `One's range contains the other`
        : `No containment`)
    );
  }
}

function importData(): string[] {
  const rawFile = readFileSync('./Day04/input.txt', 'utf-8');
  const fileAsStringArray = rawFile.split('\r\n');
  return fileAsStringArray;
}

function solvePart1(data: string[]): number {
  let containmentCount = 0;
  let overlapCount = 0;
  for (const elfRangeRaw of data) {
    const elfRange = new ElfPair(elfRangeRaw);
    if (elfRange.anElfIsContained) {
      containmentCount++;
    }
    if (elfRange.checkOverlap()) {
      overlapCount++;
    }
  }
  console.log(`There were ${containmentCount} pairs that had containment`);
  console.log(`There were ${overlapCount} pairs that had overlap`);
  return containmentCount;
}

function solvePart2(data: string[]): number {
  return 0;
}

const data = importData();
// const elfArray: ElfPair[] = []
solvePart1(data);
solvePart2(data);
