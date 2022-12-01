import { readFileSync } from 'fs';

class ElfFood {
    foodItems: number[] = [];
    foodTotal: number;
   
    constructor(foodItems: number[]) {
      this.foodItems = foodItems;
      this.foodTotal = foodItems.reduce((sum, current) => sum + current, 0);
    }
   
    print() {
      return `Hello, this elf has ${this.foodTotal} calories from ${this.foodItems}`;
    }
  }

const rawFile = readFileSync('./Day01/input.txt', 'utf-8');
const fileAsNumericArray = rawFile.split("\n").map(str => {return parseInt(str)});
let bag: number[] = [];
let elves: ElfFood[] = [];
let maxElf = 0;
for (let item of fileAsNumericArray) {
    if (Number.isNaN(item)) {
        let newElf = new ElfFood(bag)
        elves.push(newElf)
        if(newElf.foodTotal>maxElf){maxElf = newElf.foodTotal};
        bag = [];
    } else {
        bag.push(item)
    }
}
if (bag.length > 0) {
    elves.push(new ElfFood(bag))
}
console.log(elves)
console.log(`The most food carried was ${maxElf}`)
