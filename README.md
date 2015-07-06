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


### How do I get set up? ###


* Clone it!
```
git clone https://github.com/aerth/servit.git

```


* Install it!


```
sudo cp ./dependencies/a2createsite /usr/local/bin/
sudo cp ./SERVIT /usr/local/bin/
chmod +x /usr/local/bin/SERVIT
chmod +x /usr/local/bin/a2createsite

```

* Run it!

```
SERVIT
```

* Dependencies
a2createsite. Debian or Ubuntu (more linux servers coming soon). Superuser. Python + Ncurses. 


### Contributing? ###

* Review code
* Make sure your changes didn't break the app
* Describe changes in git commits

### Who do I talk to? ###

* Repo admin

aerth@isupon.us (email)

### Future Releases ###

Next release will have support for Red Hat, CentOS, and Arch servers.
If you know how that works, go ahead and do it. Pull requests are welcome.
