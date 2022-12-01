"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = require("fs");
var ElfFood = /** @class */ (function () {
    function ElfFood(foodItems) {
        this.foodItems = [];
        this.foodItems = foodItems;
        this.foodTotal = foodItems.reduce(function (sum, current) { return sum + current; }, 0);
    }
    ElfFood.prototype.print = function () {
        return "Hello, this elf has ".concat(this.foodTotal, " calories from ").concat(this.foodItems);
    };
    return ElfFood;
}());
var rawFile = (0, fs_1.readFileSync)('./Day01/input.txt', 'utf-8');
var fileAsNumericArray = rawFile.split("\n").map(function (str) { return parseInt(str); });
var bag = [];
var elves = [];
var maxElf = 0;
for (var _i = 0, fileAsNumericArray_1 = fileAsNumericArray; _i < fileAsNumericArray_1.length; _i++) {
    var item = fileAsNumericArray_1[_i];
    if (Number.isNaN(item)) {
        var newElf = new ElfFood(bag);
        elves.push(newElf);
        if (newElf.foodTotal > maxElf) {
            maxElf = newElf.foodTotal;
        }
        ;
        bag = [];
    }
    else {
        bag.push(item);
    }
}
if (bag.length > 0) {
    elves.push(new ElfFood(bag));
}
console.log(elves);
console.log("The most food carried was ".concat(maxElf));
//# sourceMappingURL=Day01.js.map