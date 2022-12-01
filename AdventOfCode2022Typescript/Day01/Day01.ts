import { readFileSync } from 'fs';


let message: string = "Hello world";
console.log(message)

const file = readFileSync('./Day01/input.txt', 'utf-8');
console.log(file)