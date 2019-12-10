After inspection of the source we see that we have to move ptr in order to pass the check at line 5 and be prompted with a shell in interactive mode. We can see ptr address by looking at the assembly code. It starts with ff and we need it to start with ca. There are 2 ways to do that:

	~ we can calculate the difference between 0xffffff and 0xcafffff and see that it is 89 000 000. That mean we have to move ptr 89 milion times before we face the check. Solution is in first.py
	python first.py > /vortex/vortex1 
Feed it /tmp/vortex_pass/vortex2 and type 'cat /etc/vortex_pass/vortex2'
	~ we can make the ptr pointer override its own value by assigning x to it (line 28) so its most significant bit is 0xca. 
	(python second.py; tee) | /vortex/vortex1

Setuid line is there in order to prevent us from directly changing the permissions of vortex3.
