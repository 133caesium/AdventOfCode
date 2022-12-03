import { readFileSync } from 'fs';

class ElfBackpack {
    backpack: string;
    compartment1: string;
    compartment2: string;
    duplicateCharacters: string[];
    duplicateCharValue: number;
   
    constructor(backpack: string) {
      this.backpack = backpack;
      this.compartment1 = backpack.substring(0, backpack.length/2);
      this.compartment2 = backpack.substring(backpack.length/2);
      this.duplicateCharacters = [];
      this.findDuplicates()
      this.duplicateCharValue =  (this.duplicateCharacters[0].charCodeAt(0) -64)<27 ? 
        this.duplicateCharacters[0].charCodeAt(0) -64+26 :
        this.duplicateCharacters[0].charCodeAt(0) -64-32;
    }

    findDuplicates() {
        for (var i = 0; i < this.compartment1.length; i++) {
            if (this.compartment2.includes(this.compartment1.charAt(i))) {
                this.duplicateCharacters.push(this.compartment1.charAt(i))
            }
        }
    }
   
    toString() {
      return (
        `A backpack containing ${this.backpack} \n`+
        `Made up of two compatments:\n`+
        `${this.compartment1}\n`+
        `${this.compartment2}\n` +
        `Duplicate characters \n` +
        `${this.duplicateCharacters} \n`)+
        `By default this has the value ${
           this.duplicateCharValue}`
    }
  }

function importData(): string[] {
    const rawFile = readFileSync('./Day03/input.txt', 'utf-8');
    const fileAsStringArray = rawFile.split("\r\n");
    return fileAsStringArray;
}

const data = importData()
console.log(data)
let backpackDuplicatesum = 0;
for (let individualBackpackRaw of data) {
    const backpack = new ElfBackpack(individualBackpackRaw)
    console.log(backpack.toString())
    backpackDuplicatesum = backpackDuplicatesum + backpack.duplicateCharValue
}
console.log(`Final sum is ${backpackDuplicatesum}`)
