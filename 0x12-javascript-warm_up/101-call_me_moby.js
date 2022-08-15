#!/usr/bin/node
function callMeMOby (x, theFunction) {
  for (let i = 0; i <= x; i++) {
    theFunction();
  }
}
module.exports.callMeMOby = callMeMOby;
