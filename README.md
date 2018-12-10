# sublime-swan

Sublime Text 3 syntax highlighting and auto completion for `.swan` file(Baidu 'smart program').

Baidu smart program is a new open ability. Developers can quickly develop an samrt program. Through searching, users can be easily acquired and disseminated within the Baidu Apps.
[document](https://smartprogram.baidu.com/docs/introduction/enter_application/)

## Install

- Package Control(Under review, temporarily unavailable)

Search `Sublime Swan` via Package Control: Install Package

- Git

Git clone this repository to Sublime Packages Path.

- Zip

Download zip and unzip to Sublime Packages Path.

## Setting

- In order to improve SWAN completion efficiency, Preferences.sublime-settings(User) should be edited and added config below:

		"auto_complete_triggers":
		[
		  {
		    "characters": "abcdefghijklmnopqrstuvwxyz< :.",
		    "selector": "text.swan"
		  }
		],


## Feature

- .swan file syntax highlighting

- Baidu smart app components auto-completion

- Baidu smart app apis auto-completion and suggestion

## Usage

- Swan
1. choose `view` ====> `<view></view>`
2. choose `view:id` ===> `<view id=""></view>`
3. `view.demo + tab` ===> `<view class="demo"></view>`
4. `view#demo + tab` ===> `<view id="demo"></view>`

- JavaScript(api and snippet)
1. choose `swan.login    api` ===> `swan.login();`
2. choose `swan.login    snippet` ===> 

		swan.login({
            success: function (res) {}
        });
**Note:** Snippets only include the necesssary keys

## Liscense
This plugin is published under the [MIT License](https://github.com/efe-blue/sublime-swan/blob/master/LICENSE)
