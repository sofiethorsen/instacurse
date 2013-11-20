instacurse - hipster client for Instagram
==========

Installation
==========

libevent
----------
To be able to install greenlet/gevent with pip, libevent must be installed:

    brew install libevent

The installation may be in the wrong place, if so export this:

    export LDFLAGS=-L/usr/local/lib/
    export CFLAGS=-I/usr/local/include/
    
libjpeg & PIL
----------
To be able to install PIL, libjpeg is required: 

    brew install libjpeg

For the installation to work you may also have to symlink to the X11 lib:

    ln -s  /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/System/Library/Frameworks/Tk.framework/Versions/8.5/Headers/X11 /usr/local/include/X11

requirements.txt
----------
Install the pip packages using:

    pip install -r requirements.txt
    
    
Running the client
----------
Just run: 

    python instacurse.py
   
Note that you will need a terminal with 256 colors to be able to run the client.

Screenshots
----------

![Startscreen](https://raw.github.com/sofiethorsen/instacurse/master/screenshots/img4.png)

![Sample](https://raw.github.com/sofiethorsen/instacurse/master/screenshots/img1.png)

![Sample](https://raw.github.com/sofiethorsen/instacurse/master/screenshots/img2.png)

![Sample](https://raw.github.com/sofiethorsen/instacurse/master/screenshots/img3.png)

![Sample](https://raw.github.com/sofiethorsen/instacurse/master/screenshots/img5.png)

