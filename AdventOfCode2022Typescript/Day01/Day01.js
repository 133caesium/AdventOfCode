"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = require("fs");
var ElfInventory = /** @class */ (function () {
    function ElfInventory(foodItems) {
        this.individualCalories = [];
        this.individualCalories = foodItems;
        this.totalCalories = foodItems.reduce(function (sum, current) { return sum + current; }, 0);
    }
    ElfInventory.prototype.toString = function () {
        return "This elf has ".concat(this.totalCalories, " total calories from the items: ").concat(this.individualCalories);
    };
    return ElfInventory;
}());
function importData() {
    var rawFile = (0, fs_1.readFileSync)('./Day01/input.txt', 'utf-8');
    var fileAsNumericArray = rawFile.split("\n").map(function (str) { return parseInt(str); });
    return fileAsNumericArray;
}
function generateElvesFromNumericData(data) {
    var elves = [];
    var bag = [];
    for (var _i = 0, data_1 = data; _i < data_1.length; _i++) {
        var item = data_1[_i];
        if (Number.isNaN(item)) {
            elves.push(new ElfInventory(bag));
            bag = [];
        }
        else {
            bag.push(item);
        }
    }
    if (bag.length > 0) {
        elves.push(new ElfInventory(bag));
    }
    var sortedElves = elves.sort(function (n1, n2) { return n2.totalCalories - n1.totalCalories; });
    return sortedElves;
}
var data = importData();
var sortedElves = generateElvesFromNumericData(data);
console.log("The top 3 food carrying elves had ".concat(sortedElves[0].totalCalories, ", ").concat(sortedElves[1].totalCalories, ", and ").concat(sortedElves[2].totalCalories, " calories"));
console.log("for a total of ".concat(sortedElves[0].totalCalories + sortedElves[1].totalCalories + sortedElves[2].totalCalories));
//# sourceMappingURL=Day01.js.map