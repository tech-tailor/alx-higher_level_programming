#!/usr/bin/node

const args = process.argv;
let allArgs = 0;
args.forEach(arg => {
  allArgs += 1;
});
if (allArgs === 2) {
  console.log('No argument');
} else if (allArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
