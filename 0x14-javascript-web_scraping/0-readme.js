#!/usr/bin/node
const fs = require('fs');

// Specify the file path
const filePath = process.argv[2];

// Read the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
