# sublime-swan

Sublime Text 3 syntax highlighting and auto completion for `.swan` file(Baidu 'smart apps').

## Install

- Package Control

Search `sublime sawn` via Package Control: Install Package

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
		    "selector": "text.wxml"
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