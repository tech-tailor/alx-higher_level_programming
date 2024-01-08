#!/usr/bin/node

const args = process.argv;
const argsLenght = args.length;
if (argsLenght === 2) {
  console.log('No argument');
} else if (argsLenght === 3) {
  console.log('Argment found');
} else {
  console.log('Arguments found');
}
