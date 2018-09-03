const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
let mainWindow;

app.on('window-all-closed', function () {
    app.quit();
});

app.on('ready', function () {
    var subpy = require('child_process').spawn('python', ['./main.py']);
    var rq = require('request-promise');
    var mainAddr = 'http://localhost:8080'; // ポートはmain.pyで設定された値

    var openWindow = function () {
        mainWindow = new BrowserWindow({ width: 500, height: 400 });
        mainWindow.loadURL(mainAddr);
        mainWindow.on('closed', function () {
            mainWindow = null;
            subpy.kill('SIGINT');
        });
    };

    var startUp = function () {
        rq(mainAddr)
            .then(function (htmlString) {
                console.log('server started');
                openWindow();
            })
            .catch(function (err) {
                startUp();
            });
    };
    startUp();
});
