#!/usr/bin/node

const args = process.argv.slice(2);
let allArgs = 0;
args.forEach(arg => {
  allArgs += 1;
});
if (allArgs === 0) {
  console.log('No argument');
} else {
  console.log(process.argv.slice(2).join(','));
}
