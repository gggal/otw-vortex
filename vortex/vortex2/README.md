First we need to create the archive, ignoring the leading '/' message. Then we can examine its content by ouputing it to stdout by: 
tar xf '/tmp/ownership.$$.tar' -O

It's important to put the path in quotes so $$ doesn't resolve to process id.
