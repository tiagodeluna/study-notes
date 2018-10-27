# NPM Commands

A list of useful NPM commands.

| Command | Description |
| ----- | ----- |
| npm install [-g] `package name` [--save] | Install a package. Use `-g` to install globally. Use `--save` to include the package as a dependency in your project |
| npm uninstall `package name` | Uninstall a package, completely removing everything npm installed on its behalf |
| npm config set `key` `value` -g | Set a configuration entry. e.g. `npm config set proxy http://myproxy:8080`. |
| npm config get `key` `value` | Display a configuration entry |
| npm config delete `key` | Delete a configuration entry |
| npm config list | List all existing settings |
| npm start | Run whatever you have defined for the `start` command of the `scripts` object in your package.json file, e.g. `"scripts": { "start": "ng serve" }` |
| npm run `script` | Run the respective script configured in scripts section of the package.json, e.g `npm run build` |
| npm outdated | Display all outdated dependencies in a project |
| npm update [-g] [`package`] | Update the dependencies of a project to the latest version (default), or you can specify one or more packages to be updated. |
| npm shrinkwrap | Repurpose package-lock.json into a publishable npm-shrinkwrap.json or simply creates a new one. |


## How to Update your Project Dependencies

1. `npm outdated`
2. `npm update`
3. `npm shrinkwrap`


## Angular CLI

| Command | Description |
| ----- | ----- |
| npm install -g @angular/cli | Installs Angular CLI |
| ng new `app name` | Generates a new project and skeleton application |
| ng serve --open | Launches the server and opens the browser (with `--open` or `-o`) |
