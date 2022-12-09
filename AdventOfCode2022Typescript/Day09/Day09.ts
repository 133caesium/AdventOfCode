import { readFileSync } from 'fs';

function importData(): string[] {
  const rawFile = readFileSync('./Day09/input.txt', 'utf-8');
  const fileAsStringArray = rawFile.split('\r\n');
  return fileAsStringArray;
}

class Move {
  deltaX: number;
  deltaY: number;
  rawMove: string;

  constructor(data: string) {
    this.rawMove = data;
    const direction: string = data.split(' ')[0];
    const magnitude = parseInt(data.split(' ')[1]);
    if (direction === 'R') {
      this.deltaX = magnitude;
      this.deltaY = 0;
    } else if (direction === 'L') {
      this.deltaX = -magnitude;
      this.deltaY = 0;
    } else if (direction === 'U') {
      this.deltaX = 0;
      this.deltaY = magnitude;
    } else if (direction === 'D') {
      this.deltaX = 0;
      this.deltaY = -magnitude;
    } else {
      console.log(`ERROR: unexpected direction=${direction}`);
    }
  }

  toString(): string {
    return `A move of ${this.deltaX},${this.deltaY} generated from ${this.rawMove}`;
  }
}

class Point {
  x: number;
  y: number;

  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }
}

class Rope {
  headLocation: Point;
  tailLocation: Point;
  tailLocationsVisited: Point[] = [];

  constructor(headStart: Point, tailStart: Point) {
    this.headLocation = headStart;
    this.tailLocation = tailStart;
  }

  moveHead(move: Move): Point {
    for (let index = 0; index < Math.abs(move.deltaX + move.deltaY); index++) {
      const NewHeadLocation = new Point(
        this.headLocation.x + Math.sign(move.deltaX),
        this.headLocation.y + Math.sign(move.deltaY)
      );
      this.headLocation = NewHeadLocation;
      const newLocation = this.moveTail();
      let uniqueNewLocation = true;
      this.tailLocationsVisited.forEach((location) => {
        if (newLocation.y === location.y && newLocation.x === location.x) {
          uniqueNewLocation = false;
        }
      });
      if (uniqueNewLocation) {
        this.tailLocationsVisited.push(newLocation);
      }
    }
    return this.headLocation;
  }

  moveTail(): Point {
    const xDist = this.headLocation.x - this.tailLocation.x;
    const yDist = this.headLocation.y - this.tailLocation.y;
    if (Math.abs(xDist) > 1 || Math.abs(yDist) > 1) {
      this.tailLocation = new Point(
        this.tailLocation.x + Math.sign(xDist),
        this.tailLocation.y + Math.sign(yDist)
      );
    }
    return this.tailLocation;
  }
}

class TenKnotRope extends Rope {
  knots: Point[] = [];

  constructor(headStart: Point, tailStart: Point) {
    super(headStart, tailStart);
    this.knots.push(this.headLocation);
    for (let index = 1; index < 9; index++) {
      this.knots.push(this.tailLocation);
    }
    this.knots.push(this.tailLocation);
  }

  follow(leader: Point, follower: Point): Point {
    const xDist = leader.x - follower.x;
    const yDist = leader.y - follower.y;
    if (Math.abs(xDist) > 1 || Math.abs(yDist) > 1) {
      follower = new Point(
        follower.x + Math.sign(xDist),
        follower.y + Math.sign(yDist)
      );
    }
    return follower;
  }

  moveHead(move: Move): Point {
    for (let index = 0; index < Math.abs(move.deltaX + move.deltaY); index++) {
      const NewHeadLocation = new Point(
        this.headLocation.x + Math.sign(move.deltaX),
        this.headLocation.y + Math.sign(move.deltaY)
      );
      this.headLocation = NewHeadLocation;
      this.knots[0] = NewHeadLocation;
      for (let tailIndex = 1; tailIndex < this.knots.length; tailIndex++) {
        this.knots[tailIndex] = this.follow(
          this.knots[tailIndex - 1],
          this.knots[tailIndex]
        );
      }
      const newLocation = this.knots[9];
      let uniqueNewLocation = true;
      this.tailLocationsVisited.forEach((location) => {
        if (newLocation.y === location.y && newLocation.x === location.x) {
          uniqueNewLocation = false;
        }
      });
      if (uniqueNewLocation) {
        this.tailLocationsVisited.push(newLocation);
      }
    }
    return this.headLocation;
  }
}

function solvePart1(data: string[]): number {
  const origin = new Point(0, 0);
  const rope = new Rope(origin, origin);
  rope.tailLocationsVisited.push(origin);
  data.forEach((moveRaw) => {
    const move = new Move(moveRaw);
    rope.moveHead(move);
  });
  console.log(`Visited ${rope.tailLocationsVisited.length}`);
  return rope.tailLocationsVisited.length;
}

function solvePart2(data: string[]): number {
  const origin = new Point(0, 0);
  const rope = new TenKnotRope(origin, origin);
  rope.tailLocationsVisited.push(origin);
  data.forEach((moveRaw) => {
    const move = new Move(moveRaw);
    rope.moveHead(move);
  });
  console.log(`Visited ${rope.tailLocationsVisited.length}`);
  return rope.tailLocationsVisited.length;
}

const data = importData();

solvePart1(data);
solvePart2(data);
