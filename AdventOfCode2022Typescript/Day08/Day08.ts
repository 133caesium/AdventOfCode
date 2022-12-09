import { readFileSync } from 'fs';

class Tree {
  treeHeight: number;
  xCoord: number;
  yCoord: number;
  treeVisible: boolean;

  constructor(height: number, x: number, y: number) {
    this.treeHeight = height;
    this.xCoord = x;
    this.yCoord = y;
    this.treeVisible = true;
  }

  valueOf(): number {
    return this.treeHeight;
  }

  toString(): string {
    return `A tree of height ${this.treeHeight} at ${this.xCoord},${this.yCoord}`;
  }
}

function importData(): string[] {
  const rawFile = readFileSync('./Day08/sample_input.txt', 'utf-8');
  const fileAsStringArray = rawFile.split('\r\n');
  return fileAsStringArray;
}

function solvePart1(data: string[]): number {
  return 0;
}

function solvePart2(data: string[]): number {
  return 0;
}

// Select the current tree
// select the other trees in the same row and column
// If all the trees above, below, left, or right are shorter, it is visible
// If any direction has all trees below, then it is visible

function checkVisibility(trees: Tree[][]): void {
  for (let yIndex = 1; yIndex < trees.length - 1; yIndex++) {
    for (let xIndex = 1; xIndex < trees[yIndex].length - 1; xIndex++) {
      const tree = trees[yIndex][xIndex];
      let visibleUp = true;
      let visibleDown = true;
      let visibleLeft = true;
      let visibleRight = true;
      tree.treeVisible = false;
      // check above visible
      for (let checkYIndex = 0; checkYIndex < tree.yCoord; checkYIndex++) {
        if (trees[checkYIndex][xIndex] >= tree) {
          visibleUp = false;
        }
      }
      // check below visible
      for (
        let checkYIndex = tree.yCoord + 1;
        checkYIndex < trees.length;
        checkYIndex++
      ) {
        if (trees[checkYIndex][xIndex] >= tree) {
          visibleDown = false;
        }
      }
      // check left visible
      for (let checkXIndex = 0; checkXIndex < tree.xCoord; checkXIndex++) {
        if (trees[yIndex][checkXIndex] >= tree) {
          visibleLeft = false;
        }
      }
      // check right visible
      for (
        let checkXIndex = xIndex + 1;
        checkXIndex < trees[yIndex].length;
        checkXIndex++
      ) {
        if (trees[yIndex][checkXIndex] >= tree) {
          visibleRight = false;
        }
      }
      tree.treeVisible =
        visibleUp || visibleDown || visibleLeft || visibleRight;
    }
  }
}

function createTrees(data): Tree[][] {
  const trees: Tree[][] = [];
  for (let yIndex = 0; yIndex < data.length; yIndex++) {
    const treeRowRaw = data[yIndex];
    const treeRow: Tree[] = [];
    for (let xIndex = 0; xIndex < treeRowRaw.length; xIndex++) {
      const tree = new Tree(parseInt(treeRowRaw[xIndex]), xIndex, yIndex);
      treeRow.push(tree);
    }
    trees.push(treeRow);
  }
  return trees;
}

function countVisibleTrees(trees: Tree[][]): number {
  let visibleTreeCount = 0;
  trees.forEach((treeRow) => {
    treeRow.forEach((tree) => {
      if (tree.treeVisible) {
        visibleTreeCount++;
      }
    });
  });
  return visibleTreeCount;
}

const data = importData();
const trees = createTrees(data);
checkVisibility(trees);
console.log(`The number of visible trees is ${countVisibleTrees(trees)}`);
solvePart1(data);
solvePart2(data);
