#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count;
  let occurence = 0;
  for (count = 0; count < list.length; count++) {
    if (list[count] === searchElement) {
      occurence += 1;
    }
  }
  return (occurence);
};
