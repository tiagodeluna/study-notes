# Angular

Most useful commands from Angular CLI (Command Line Interface).

## NPM

| Command | Description |
| ----- | ----- |
| npm install -g @angular/cli | Installs Angular CLI |
| npm config set `key` `value` -g | Sets a configuration entry. i.e: `npm config set proxy http://myproxy:8080`. The `-g` is optional (equivalent to `--global`) |
| npm config get `key` `value` | Displays a configuration entry |
| npm config delete `key` | Deletes a configuration entry |
| npm config list | Lists all existing settings |

## Angular CLI

| Command | Description |
| ----- | ----- |
| ng new `app name` | Generates a new project and skeleton application |
| ng serve --open | Launches the server and opens the browser (with `--open` or `-o`) |
