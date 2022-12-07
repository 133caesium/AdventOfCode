import { readFileSync } from 'fs';

class File {
  name: string;
  size: number;
  constructor(name: string, size: number) {
    this.name = name;
    this.size = size;
  }
}

class Folder extends File {
  contents: File[] = [];

  constructor(name: string) {
    super(name, 0);
  }

  addItem(item: File): void {
    this.contents.push(item);
    this.size += item.size;
  }
}

function importData(): string[] {
  const rawFile = readFileSync('./Day07/input.txt', 'utf-8');
  const fileAsStringArray = rawFile.split('\r\n');
  return fileAsStringArray;
}

function addFilesToFolder(rawFileList: string[], targetFolder: Folder): void {
  rawFileList.forEach((line) => {
    if (line[0].match(/^\d+$/) != null) {
      const name = line.split(' ')[1];
      const size = parseInt(line.split(' ')[0]);
      targetFolder.addItem(new File(name, size));
    }
  });
}

function addFoldersToFolder(rawFileList: string[], targetFolder: Folder): void {
  rawFileList.forEach((line) => {
    if (line.substring(0, 3) === 'dir') {
      const name = line.split(' ')[1];
      targetFolder.addItem(new Folder(name));
    }
  });
}

function recalculateFolderSize(targetFolder: Folder): void {
  targetFolder.size = 0;
  targetFolder.contents.forEach((item) => {
    if (item instanceof Folder) {
      recalculateFolderSize(item);
    }
    targetFolder.size += item.size;
  });
}

function queueFolders(targetFolder): Folder[] {
  const folderQueue: Folder[] = [];
  targetFolder.contents.forEach((item) => {
    if (item instanceof Folder) {
      folderQueue.push(item);
      queueFolders(item).forEach((folder) => {
        folderQueue.push(folder);
      });
    }
  });
  return folderQueue;
}

function sumFoldersLessThanSize(
  targetFolder: Folder,
  maxFolderSize: number
): number {
  let totalFolderSizeSum = 0;
  queueFolders(targetFolder).forEach((folder) => {
    if (folder.size < maxFolderSize) {
      totalFolderSizeSum += folder.size;
    }
  });

  return totalFolderSizeSum;
}

function generateRoot(data: string[]): Folder {
  const root: Folder = new Folder('/');
  let folderCursor: Folder = root;
  const folderPath: Folder[] = [];

  let lineCache: string[] = [];
  data.forEach((line) => {
    if (line[0] === '$') {
      addFilesToFolder(lineCache, folderCursor);
      addFoldersToFolder(lineCache, folderCursor);
      lineCache = [];
      // console.log(`Adding files triggered by ${line}`)
    }
    if (line.substring(0, 5) === '$ cd ') {
      if (line[6] !== '.') {
        folderCursor.contents.forEach((possibleFolder) => {
          if (
            possibleFolder.name === line.substring(5, line.length) &&
            possibleFolder instanceof Folder
          ) {
            folderPath.push(folderCursor);
            folderCursor = possibleFolder;
            // console.log(`Navigated down to ${folderCursor.name}`)
          }
        });
      } else {
        folderCursor = folderPath.pop();
        // console.log(`Navigated up to ${folderCursor.name}`)
      }
    } else {
      lineCache.push(line);
    }
  });
  addFilesToFolder(lineCache, folderCursor);
  addFoldersToFolder(lineCache, folderCursor);

  recalculateFolderSize(root);
  return root;
}

function solvePart1(root: Folder): number {
  const solution = sumFoldersLessThanSize(root, 100000);
  console.log(`Part one calcuation is: ${solution}`);
  return solution;
}

function solvePart2(root: Folder): number {
  const TotalDiskSpace = 70000000;
  const RequiredDiskSpace = 30000000;
  const SpaceRequired = RequiredDiskSpace - (TotalDiskSpace - root.size);

  let smallestFolder = TotalDiskSpace;

  queueFolders(root).forEach((folder) => {
    if (folder.size > SpaceRequired && folder.size < smallestFolder) {
      smallestFolder = folder.size;
    }
  });
  console.log(`Part two calcuation is: ${smallestFolder}`);
  return smallestFolder;
}

const data = importData();
const root = generateRoot(data);
solvePart1(root);
solvePart2(root);
