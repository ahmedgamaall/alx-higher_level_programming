#!/usr/bin/node

const argvLen = process.argv.length;

if (argvLen === 2) {
 console.log('No argument');
} else if (argvLen === 3) {
 console.log('Argument found');
} else {
 console.log('Arguments found');
}
