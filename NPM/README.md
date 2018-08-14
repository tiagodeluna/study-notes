# NPM Commands

A list of useful NPM commands.

## NPM

| Command | Description |
| ----- | ----- |
| npm install [-g] `package name` [--save] | Installs a package. Use `-g` to install globally. Use `--save` to include the package as a dependency in your project |
| npm config set `key` `value` -g | Sets a configuration entry. e.g. `npm config set proxy http://myproxy:8080`. |
| npm config get `key` `value` | Displays a configuration entry |
| npm config delete `key` | Deletes a configuration entry |
| npm config list | Lists all existing settings |
| npm start | Run whatever you have defined for the `start` command of the `scripts` object in your package.json file, e.g. `"scripts": { "start": "ng serve" }` |
| npm run `script` | Runs the respective script configured in scripts section of the package.json, e.g `npm run build` |
| npm outdated | Displays all outdated dependencies in a project |
| npm update [-g] [`package`] | Updates the dependencies of a project to the latest version (default), or you can specify one or more packages to be updated. |
| npm shrinkwrap | Repurposes package-lock.json into a publishable npm-shrinkwrap.json or simply creates a new one. |

## HOW TO UPDATE YOUR PROJECT DEPENDENCIES

1. `npm outdated`
2. `npm update`
3. `npm shrinkwrap`

## Angular CLI

| Command | Description |
| ----- | ----- |
| npm install -g @angular/cli | Installs Angular CLI |
| ng new `app name` | Generates a new project and skeleton application |
| ng serve --open | Launches the server and opens the browser (with `--open` or `-o`) |
