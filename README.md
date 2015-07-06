# SERVIT #


```
 ____  _____ ______     _____ _____ 
/ ___|| ____|  _ \ \   / /_ _|_   _|
\___ \|  _| | |_) \ \ / / | |  | |  
 ___) | |___|  _ < \ V /  | |  | |  
|____/|_____|_| \_\ \_/  |___| |_|  
                                   
```


MIT LICENSE

Contributors:

aerth

### CLI interface for Debian/Ubuntu server management, including support for: ###

* Apache2 Virtual Hosts
* Postfix / Dovecot Email Address Management
* EASY SSH / SCP
* ASCII ART
* Add User
* Easy to add your favorite scripts
* Super CLI Menu


### How do I get set up? (Developing) ###


* Clone it!
```
git clone https://github.com/aerth/servit.git

```


* Run it!


```
cp ./other/a2createsite /usr/sbin/
chmod +x SERVIT
cat ./README.md | less;cat ./SERVIT | less; ./SERVIT

```


* Dependencies
Debian or Ubuntu. SSH access (at least). Python + Ncurses. Includes Dependency Installer to get the most out of this script. wget or curl required, and automatically installed if not already present.


### Contributing? ###

* Write tests
* Review code
* Make sure your changes didn't break the app
* Describe changes in git commits

### Who do I talk to? ###

* Repo admin

aerth@isupon.us (email)

### Future Releases ###

Next release will have support for Red Hat, CentOS, and Arch servers.
If you know how that works, go ahead and do it. Pull requests are welcome.
