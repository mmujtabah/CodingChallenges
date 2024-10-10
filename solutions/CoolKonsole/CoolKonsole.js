const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter your text: ", (text) => {
    let i = 0;
    const interval = setInterval(() => {
        if (i <= text.length) {
            console.clear();
            console.log(text.substring(0, i++));
        } else {
            clearInterval(interval);
            rl.close();
        }
    }, 100);
});
