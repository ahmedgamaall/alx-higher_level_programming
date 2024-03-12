#!/usr/bin/node
exports.esrever = function (list) {
  const reversedListFromRealList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedListFromRealList.push(list[i]);
  }
  return reversedListFromRealList;
};
