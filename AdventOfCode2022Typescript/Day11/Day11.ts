// import { readFileSync } from 'fs';

// function importData(): string[] {
//   const rawFile = readFileSync('./Day11/sample_input.txt', 'utf-8');
//   const fileAsStringArray = rawFile.split('\r\n');
//   return fileAsStringArray;
// }

// function monkeyParser(data: string[]): Monkey[] {
//     const monkeyFamily: Monkey[] = [];

//     let monkeyNumber: number;
//     let testNumber: number;
//     let testTrueMonkey: number;
//     let testFalseMonkey: number;
//     let operation: string;
//     let operationValue: number;
//     let items: number[] = [];
//     for (let lineIndex = 0; lineIndex < data.length; lineIndex++) {
//         const line = data[lineIndex].trim().split(" ")
//         if (line[0] === "Monkey") {
//             monkeyNumber = extractNumber(line[1])
//         } else if (line[0] === "Starting") {
//             for (let numberIndex = 0; numberIndex < line.length; numberIndex++) {
//                 items.unshift(extractNumber(line[numberIndex]))
//             }
//         } else if (line[0] === "Operation") {
//             for (let numberIndex = 0; numberIndex < line.length; numberIndex++) {
//                 items.unshift(extractNumber(line[numberIndex]))
//             }
//         }
//     }
//     return [];
// }

// function extractNumber(numberText: string): number {
//   const matches = numberText.match(/^\d+$/);
//   if (matches?.[0] !== undefined) {
//     return parseInt(matches?.[0]);
//   } else {
//     console.log(`Uh oh, tried parsing "${numberText}" but no number found`);
//     return -1;
//   }
// }

class Monkey {
  monkeyNumber: number;
  testNumber: number;
  testTrueMonkey: number;
  testFalseMonkey: number;
  operation: string;
  operationValue: number;
  items: number[];
  inspectionCount: number;

  constructor(
    monkeyNumber: number,
    testNumber: number,
    testTrueMonkey: number,
    testFalseMonkey: number,
    operation: string,
    operationValue: number,
    items: number[]
  ) {
    this.monkeyNumber = monkeyNumber;
    this.testNumber = testNumber;
    this.testTrueMonkey = testTrueMonkey;
    this.testFalseMonkey = testFalseMonkey;
    this.operation = operation;
    this.operationValue = operationValue;
    this.items = items;
    this.inspectionCount = 0;
  }

  inspectItem(item: number): number {
    // console.log(`About to inspect ${item}`)
    let worryLevel: number = item;
    // console.log(`before inspection we have worry level ${worryLevel}`)
    if (this.operation === 'add') {
      worryLevel += this.operationValue;
      // console.log(`After adding we have worry level ${worryLevel}`)
    } else if (this.operation === 'multiply') {
      worryLevel *= this.operationValue;
      // console.log(`After multiplying we have worry level ${worryLevel}`)
    } else if (this.operation === 'square') {
      worryLevel = worryLevel * worryLevel;
      // console.log(`After squaring we have worry level ${worryLevel}`)
    } else {
      console.log(`ERROR: invalid operation, original value returned`);
    }
    worryLevel = Math.floor(worryLevel / 3);
    // console.log(`After divigind by 3 we have worry level ${worryLevel}`)
    // console.log(`after inspection we have inspect ${worryLevel}`)
    this.inspectionCount++;
    return worryLevel;
  }

  testItem(item: number): boolean {
    // console.log(`Testing item: ${item} gives ${((item % this.testNumber)===0)}`)
    return item % this.testNumber === 0;
  }

  throwItem(item: number, monkeyFamily: Monkey[]): number {
    // console.log(`About to throw item: ${item}`)
    // console.log(monkeyFamily)
    let targetMonkey: number;
    this.testItem(item)
      ? (targetMonkey = this.testTrueMonkey)
      : (targetMonkey = this.testFalseMonkey);
    const targetItemCount = monkeyFamily[targetMonkey].items.unshift(item);
    console.log(
      `Threw item [${item}] from Monkey:${this.monkeyNumber} to Monkey:${targetMonkey} who now has ${targetItemCount} items`
    );
    return this.items.length;
  }
}

function round(monkeyFamily: Monkey[]): void {
  monkeyFamily.forEach((monkey) => {
    const itemCount = monkey.items.length;
    for (let itemIndex = 0; itemIndex < itemCount; itemIndex++) {
      let item = monkey.items.pop();
      item = monkey.inspectItem(item);
      monkey.throwItem(item, monkeyFamily);
    }
  });
}

function createSampleInputMonkeys(): Monkey[] {
  const monkeyFamily: Monkey[] = [];
  monkeyFamily.push(
    new Monkey(0, 23, 2, 3, 'multiply', 19, [79, 98].reverse())
  );
  monkeyFamily.push(
    new Monkey(1, 19, 2, 0, 'add', 6, [54, 65, 75, 74].reverse())
  );
  monkeyFamily.push(
    new Monkey(2, 13, 1, 3, 'square', 19, [79, 60, 97].reverse())
  );
  monkeyFamily.push(new Monkey(3, 17, 0, 1, 'add', 3, [74].reverse()));
  return monkeyFamily;
}

function createInputMonkeys(): Monkey[] {
  const monkeyFamily: Monkey[] = [];
  monkeyFamily.push(
    new Monkey(0, 19, 6, 2, 'multiply', 13, [91, 66].reverse())
  );
  monkeyFamily.push(new Monkey(1, 5, 0, 3, 'add', 7, [78, 97, 59].reverse()));
  monkeyFamily.push(
    new Monkey(
      2,
      11,
      5,
      7,
      'add',
      6,
      [57, 59, 97, 84, 72, 83, 56, 76].reverse()
    )
  );
  monkeyFamily.push(
    new Monkey(3, 17, 6, 0, 'add', 5, [81, 78, 70, 58, 84].reverse())
  );
  monkeyFamily.push(new Monkey(4, 7, 1, 3, 'add', 8, [60].reverse()));
  monkeyFamily.push(
    new Monkey(
      5,
      13,
      7,
      4,
      'multiply',
      5,
      [57, 69, 63, 75, 62, 77, 72].reverse()
    )
  );
  monkeyFamily.push(
    new Monkey(6, 3, 5, 2, 'square', 0, [73, 66, 86, 79, 98, 87].reverse())
  );
  monkeyFamily.push(
    new Monkey(7, 2, 1, 4, 'add', 2, [95, 89, 63, 67].reverse())
  );
  return monkeyFamily;
}
function solvePart1(): number {
  const monkeyFamily: Monkey[] = createInputMonkeys();
  let monkeyInspectionCounts: number[] = [];
  monkeyFamily.forEach((monkey) => {
    console.log(`Monkey ${monkey.monkeyNumber} has ${monkey.items}`);
  });
  for (let index = 0; index < 20; index++) {
    round(monkeyFamily);
  }
  monkeyFamily.forEach((monkey) => {
    console.log(
      `Monkey ${monkey.monkeyNumber} inspected ${
        monkey.inspectionCount
      } items and has ${monkey.items.reverse()}`
    );
    monkeyInspectionCounts.push(monkey.inspectionCount);
  });
  monkeyInspectionCounts.sort((a, b) => b - a);
  const result = monkeyInspectionCounts[0] * monkeyInspectionCounts[1];
  console.log(monkeyInspectionCounts);
  console.log(`Part 1 answer: ${result}`);
  return result;
}

function solvePart2(monkeyFamily: Monkey[]): number {
  return 0;
}

// const data = importData();
// const monkeys = monkeyParser(data)
// console.log(monkeys)
// const instructions = new InstructionReader(data);
solvePart1();
// solvePart2(instructions);
