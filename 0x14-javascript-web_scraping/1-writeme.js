#!/usr/bin/node
/*
 * This script writes a string to a file
 */

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) { console.log(err); }
});
