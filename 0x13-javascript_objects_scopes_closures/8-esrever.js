#!/usr/bin/node

exports.esrever = function (list) {
  let count;
  const reverseList = [];
  for (count = list.length - 1; count > -1; count--) {
    reverseList.push(list[count]);
  }
  return (reverseList);
};
