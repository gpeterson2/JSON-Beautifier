===============
JSON Beautifier
===============

This is a program I created a while ago to take a raw JSON string and format
it to be human readable.

The actual logic is offloaded to the python json library.

This was created before Firefox, Chrome, etc. added tools to do this for you,
and so I mostly keep it around because it's a decent boilerplate example for
using pyside.

------------
Requirements
------------

- Pyside

----
Todo
----

Given that there are now much better tools to handle this, it's unlikely
these will be done, aside from the challenge.

- Format the response as a tree so items can be expanded (much like Chrome
  does it)
- Add a URL option to query the web so you don't have to copy/paste the text.

