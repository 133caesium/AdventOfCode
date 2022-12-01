"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = require("fs");
var message = "Hello world";
console.log(message);
var file = (0, fs_1.readFileSync)('./Day01/input.txt', 'utf-8');
console.log(file);
//# sourceMappingURL=Day01.js.map