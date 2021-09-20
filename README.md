# Mobile Test Project

A Python based test client for web UI and backend testing.

Use
===
Install IntelliJ https://www.jetbrains.com/idea/download/
Community edition

**MacOS**
---

How to open Terminal on Mac
The Terminal app is in the Utilities folder in Applications. To open it, either open your Applications folder, then open Utilities and double-click on Terminal, or press Command - spacebar to launch Spotlight and type "Terminal," then double-click the search result.

You’ll see a small window with a white background open on your desktop. In the title bar are your username, the word "bash" and the dimensions of the window in pixels. Bash stands for "Bourne again shell". There are a number of different shells that can run Unix commands, and on the Mac Bash is the one used by Terminal.

1 You may need to disable SIP on a Mac: https://www.macworld.co.uk/how-to/how-turn-off-mac-os-x-system-integrity-protection-rootless-3638975/

2 Install Homebrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
3 Make sure Library folder permissions are set to Read & Write for everyone on the machine, and that you've applied the permissions to all enclosed items.

4 Install Pyton  & Install pip
```brew install python```

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
and then run
```
python get-pip.py
```

5 Install pytest
```
pip install -U pytest --ignore-installed
```

6 Install all other requirements-- Open this project in IntelliJ. Use the "Run Anything" terminal to run:
```
pip install -r requirements.txt
```

7 Install Appium Desktop to allow for inspection of mobile UI components: https://github.com/appium/appium-desktop/releases/tag/v1.21.0
 a) XCode is required https://apps.apple.com/us/app/xcode/id497799835?mt=12 | Run `sudo xcode-select --install` in a terminal
 b) Android Studio and Devices setup: * https://developer.android.com/studio *https://developer.android.com/studio/run/managing-avds

8 Install Brew if you don't already have it.
-Run `brew install node` to be sure you have node installed.

-Run `brew install carthage`

-Run `npm install -g appium` *NOTE: DO NOT install via Brew, the paths will conflict.*

-Run `npm install -g appium-webdriveragent`

-Run `npm install appium-doctor -g` ... to check specific requirement setup for ios or android, Run `appium-doctor --ios` or `appium-doctor --android`


**Windows**
---
Install chocolatey from here: https://chocolatey.org/install

-Run `choco install nodejs`

-Run `npm install -g appium` NOTE: DO NOT install via Chocolatey, the paths will conflict.

-Run `choco install python --version=3.9.0`


**Everyone**
---
-Be sure to have simulator platform versions installed in Xcode. To do this, open Xcode and go to 
***Xcode > Preferences > Components*** and install the Simulator platforms you intend to use. The Default that the appium service will try to use from the code here is **14.3**

-Install The Python Community Edition Plugin for IntelliJ https://plugins.jetbrains.com/plugin/7322-python-community-edition

-Install the Requirements Plugin for Intellij https://plugins.jetbrains.com/plugin/10837-requirements

-I built this project to be able to run using pytest runners https://docs.pytest.org
-You can run tests by
inputting `pytest --environment="{test, dev}" -s tests/{your directory path} --html=test-reports/runreport.html` into the command
line or, Using IntelliJ's pytest runner, you can run tests. Find the runner under /tests.

-Note that the test runner is configured to run using the Python interpreter of the project, so you will need to define
your python interpreter for your project, or change the runner to refer to another interpreter.

-You must define an *environment* variable when running like `--environment='test' or --environment='dev'`

-Optionally, you can define an *headless* variable when running like `--headless='true' or --headless='false'`

-To add logging output to the console, add `-o log_cli=true` to arguments

-To get a junit XML report, add `--junitxml=<path to save the output file to>.xml`; I like to save reports to
\test-reports

-To get an HTML report, add `--html=<path to save the file to>.html`; I like to save reports to \test-reports

-Find screenshots and HTML reports in test-reports/{environment}/screenshots.

Test Runner configurations are found in /runners

I use the `record_xml_attribute` in my tests because I want useable xml reporting output to integrate with XRay
importing capabilities with Jira. It is not necessary to use it if you do not care for that output in your xml document.

Screenshots are automatically named by the created date and saved in PNG format, with the option to add a name to append
to the date.
