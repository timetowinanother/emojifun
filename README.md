## What It Does

This code pads characters with colons or otherwise converts them into a form that might match common emoji letter libraries.  Its success will depend on the emoji's currently in your workplace emoji library. If you run this, paste the results into your slack, and some characters aren't converted to emojis, it means your slack is missing the necessary emojis.  You can add them to your slack or pull down this code and modify it to fit your specific library. 

This code is known to work well on Firefox and Safari, and also functions on Chrome (with the limitations explained in 'Known Issues'). I have not tested it on other browsers yet.

emojify.py is a standalone python program with two options for the format of the output. I run it in the terminal and then copy the output to later paste it into a slack message.
 
emojify.js is designed to be pasted into a bookmark's URL bar and saved as a bookmark. When you click on the bookmark, it creates a pop-up in your browser that asks you to enter the message you want to emojify. When you press "ok", it produces a browser alert with the emojified message (as well as logging the output in the console log in the developer tools). 
<img width="444" alt="image" src="https://github.com/timetowinanother/emojifun/assets/17504144/1321599a-29a3-41c5-a919-21b36d31e522">

<img width="518" alt="image" src="https://github.com/timetowinanother/emojifun/assets/17504144/49e9204c-5fa6-4017-86d5-2ac90d5353aa">

  
  ## Known issues 
  
1.) Chrome: the emojify.js bookmark cannot be activated in a new Chrome browser window. The browser must be pointed at any website before the user clicks the bookmark. 

2.) Chrome: if the text in the alert box is longer than one line, it cannot be selected and copied. You must copy-paste it from the console tab in the developer tools window output 

<img width="582" alt="image" src="https://github.com/timetowinanother/emojifun/assets/17504144/345cffbb-2caa-4168-ada6-75a3e8b5683a">






## Deprecated Features 

1.) I had been using "navigator.clipboard.writeText(final)" to try to copy the results of emojify.js to the clipboard as well as displaying it, but intermittently threw "DOMException: Document is not focused" errors. When it did work, it encouraged the less-than-ideal (from an end user training perspective) behavior of encouraging end users to grant copy-to-clipboard permissions to whatever random website the browser was pointed at when the bookmark script was initiated.
