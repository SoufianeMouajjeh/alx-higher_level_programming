const fs = require('fs');

// Specify the file path
const filePath = process.argv[2];

// Read the file
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    
    // Print the file content
    console.log(data);
});
