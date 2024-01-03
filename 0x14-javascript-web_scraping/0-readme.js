#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const file_error = `Usage: ${process.argv[1]} <filename>`;

if (!filePath){
	console.error(file_error);
	process.exit(1);
}

fs.readFile(filePath, 'utf-8', (err, data) =>{
	if (err){
		console.log(err);
		return;
	}
	return console.log(data);
});
