#!/usr/bin/node
exports.esrever = function (list) {
  const nlist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    nlist.push(list[i]);
  }
  return nlist;
};
