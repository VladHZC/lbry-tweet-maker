# lbry-tweet-maker BETA
![](https://i.ibb.co/9sDXj0H/bird.png)
> by: Vlad and Simon Schubert 

## Tools for boosting your LBRY activity with Twitter 

## 0) LBRY-tweet Beta (t.py)
---
- **Tweet your last LBRY post**  

## 1.a) Auto-Tweet (for Windows) 
---
- **Auto-Tweet your last post everytime Windows starts** 

** Save the [files](https://github.com/VladHZC/lbry-tweet-maker) somewhere in your PC and then copy and paste a shortcut of the script on this folder

``` C:\Users\**CURRENT USER**\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup ```

> ** LBRY Desktop app on windows startup set and python on PATH are also required
>
>** I expect to find a method to run the script everytime the user runs the LBRY app
>
>** I expect to use the description of the post as tweet text before the post link in the future

## 1.b) Auto-Tweet (for Linux) 

Open and edit [crontab](https://linuxcommandlibrary.com/man/crontab):

``` crontab -e ```

Add the following lines to either: 

**Check and Auto-Tweet your last post on every system start**

``` @reboot python3 [part to python script] ```

**Check and Auto-Tweet your last post every hour**

``` @hourly python3 [part to python script] ```

The ```[part to python script]``` could be for example ```/home/supermario/t.py```

## 2) Channel Posting ( comming ) 
---
- Post your entire LBRY Channel, post by post every X hours 
(For users that never posted their LBRY videos on Twitter) 


---
** Twitter developer account is required for API KEYS configuration
** Set your twitter keys and channel in config.yaml file 

### Check More tools :tools: from [@vlad](https://odysee.com/@code:a) and from [@Simonschubert](https://odysee.com/@simonschubert:d)  
 - Wanna help ? Get in touch on [LBRY Discord Server](https://chat.lbry.org) or [LBRYnomics Server](https://lbrynomics.com)

### Check Other LBRY TOOLS

[LBRY TOOLS](https://odysee.com/@code:a/tools:4)

