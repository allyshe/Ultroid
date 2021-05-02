// Ultroid - UserBot
// Copyright (C) 2020 TeamUltroid
//
// This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
// PLease read the GNU Affero General Public License in
// <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

const { exec } = require('child_process');
const { appendFileSync, truncate } = require('fs');

(async () => {
    const bash = exec('node ./src/ecmaHelper/evalJs.run.js');

    truncate('./src/ecmaHelper/evalJs.result.d.js', 0, function() { 
        console.log('Result File Truncated') 
    }); 

    bash.stdout.on('data', (data) => {
        console.log(data.toString());
        appendFileSync('./src/ecmaHelper/evalJs.result.d.js', `${data.toString()}\n`, () => {});
    });

    bash.stderr.on('data', (error) => {
        appendFileSync('./src/ecmaHelper/evalJs.result.d.js', `${error}\n`, () => {});
    });
})();
