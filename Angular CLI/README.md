# NPM/AngularCLI Commands

Most useful commands from Angular CLI (Command Line Interface).

## NPM

| Command | Description |
| ----- | ----- |
| npm install -g @angular/cli | Installs Angular CLI |
| npm config set `key` `value` -g | Sets a configuration entry. e.g. `npm config set proxy http://myproxy:8080`. The `-g` is optional (equivalent to `--global`) |
| npm config get `key` `value` | Displays a configuration entry |
| npm config delete `key` | Deletes a configuration entry |
| npm config list | Lists all existing settings |
| npm start | Run whatever you have defined for the `start` command of the `scripts` object in your package.json file, e.g. `"scripts": { "start": "ng serve" }` |

## Angular CLI

| Command | Description |
| ----- | ----- |
| ng new `app name` | Generates a new project and skeleton application |
| ng serve --open | Launches the server and opens the browser (with `--open` or `-o`) |
