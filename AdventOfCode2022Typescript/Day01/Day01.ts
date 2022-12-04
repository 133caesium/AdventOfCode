import { readFileSync } from 'fs';

class ElfInventory {
  individualCalories: number[] = [];
  totalCalories: number;

  constructor(foodItems: number[]) {
    this.individualCalories = foodItems;
    this.totalCalories = foodItems.reduce((sum, current) => sum + current, 0);
  }

  toString(): string {
    return `This elf has ${
      this.totalCalories
    } total calories from the items: ${this.individualCalories.toString()}`;
  }
}

function importData(): number[] {
  const rawFile = readFileSync('./Day01/input.txt', 'utf-8');
  const fileAsNumericArray = rawFile.split('\n').map((str) => {
    return parseInt(str);
  });
  return fileAsNumericArray;
}

function generateElvesFromNumericData(data: number[]): ElfInventory[] {
  const elves: ElfInventory[] = [];
  let bag: number[] = [];
  for (const item of data) {
    if (Number.isNaN(item)) {
      elves.push(new ElfInventory(bag));
      bag = [];
    } else {
      bag.push(item);
    }
  }
  if (bag.length > 0) {
    elves.push(new ElfInventory(bag));
  }
  const sortedElves: ElfInventory[] = elves.sort(
    (n1, n2) => n2.totalCalories - n1.totalCalories
  );
  return sortedElves;
}

const data = importData();
const sortedElves = generateElvesFromNumericData(data);

console.log(
  `The top 3 food carrying elves had ${sortedElves[0].totalCalories}, ${sortedElves[1].totalCalories}, and ${sortedElves[2].totalCalories} calories`
);
console.log(
  `for a total of ${
    sortedElves[0].totalCalories +
    sortedElves[1].totalCalories +
    sortedElves[2].totalCalories
  }`
);
