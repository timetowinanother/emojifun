## What It Does

This code pads characters with colons or otherwise converts them into a form that might match common emoji letter libraries.  Its success will depend on the emoji's currently in your workplace emoji library. If you run this, paste the results into your slack, and some characters aren't converted to emojis, it means your slack is missing the necessary emojis.  You can add them to your slack or pull down this code and modify it to fit your specific library. 

This code works best on Firefox, but also functions on Chrome. I have not tested it on other browsers yet.

emojify.py is a standalone python program with two options for the format of the output. I run it in the terminal and then copy the output to later paste it into a slack message.
 
emojify.js is designed to be pasted into a bookmark's URL bar and saved as a bookmark. It produces output in the form of a browser alert as well as a message in the console log in the developer tools. I am working on the section that also copies the output to the user’s clipboard automatically but that is not 100% functional yet. 
 
  
  ## Known issues 
  
1.) Chrome: the emojify.js bookmark cannot be activated in a new Chrome browser window. You must actually be at a website first. 

2.) Chrome: if the text in the alert box is longer than one line, it cannot be selected and highlighted. You must copy-paste it from the dev 

3.) Chrome: The “(via navigator.clipboard.writeText(final).then(success_callback, failure_callback)” section of code, which is supposed to copy the bookmark’s output to the user’s clipboard, appears to miss occasionally on Chrome. It was originally introduced to make up for issues #2, but is not sufficiently reliable.
