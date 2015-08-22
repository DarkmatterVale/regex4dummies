# Setting Up a Development Environment

To setup a development environment, a few things must be done. Each of these steps are described in detail below.

- Make sure you have python and wget command-line commands installed<br>
- Download & extract the Github repository<br>
- "cd", or change directory, to the downloaded file<br>
- Test & Start messing with the code!


## Making sure you have python and the wget command-line commands installed

Both of these are required commands to get the library to work. To test to see whether you have python installed, type the following into the terminal:

```
~$ python
```

If you get an error, then you will have to install Python 2.7. This is very easy and can be completed by going to the Python website and downloading Python 2.7

Next up is checking whether you have wget installed. This is also a simple test, and can be done like the following:

```
~$ wget
```

You should get something like "usage: etc.", but if you get an error you will have to install wget. This varies by operating system and is well documented online, so I will not go into detail about it here.


## The next step is to download the Github repository. Since you are setting up a development environment, you will probably want the latest release. To get this, go to this link ( which is the link to the releases page on Github ): https://github.com/DarkmatterVale/regex4dummies/releases">https://github.com/DarkmatterVale/regex4dummies/releases

Once you have downloaded the file, extract it and you should be ready to move on to the next step.

## Luckily, this is a simple step. Open command-line or terminal, and cd to the downloaded folder containing the latest release. Then you're done!

## In this last step, you are going to need to test the library. Enter into the regex4dummies.py file, and near the bottom, you should see the following line of code:

```
exit( 0 )
```

Change that line to this:

```
#exit( 0 )
```

You just commented out the code that would exit the main library if you attempted to run it. Now, if everything was installed properly, you should be able to run the following command in command-line/terminal, and you should get some patterns!

```
~$ python regex4dummies.py
```

Now, feel free to look over the code and mess with anything you want!
