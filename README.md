# lbry-tweet-maker BETA
![](https://i.ibb.co/9sDXj0H/bird.png)
> by: Vlad and Simon Schubert 

## Tools for boosting your LBRY activity with Twitter 

## 0) LBRY-tweet Beta (t.py)
---
- **Tweet your last LBRY post**  

## 1.a) Auto-Tweet (for Windows) 
---

- **Auto-Tweet your last post everytime Windows Starts** 
Every time you start windows the script will autorun and post your last LBRY post (assuming LBRY is set to start along with windows startup) with a pre-made text before the link (you can change the text in the script if you wnat) 

[![Download](https://i.ibb.co/RYxvyf3/windows-button-download-1.png)](https://github.com/VladHZC/lbry-tweet-maker)
### Instructions:
---
1) Save the [files](https://github.com/VladHZC/lbry-tweet-maker) somewhere in your PC and then copy and paste a shortcut of the script on this folder

		``` C:\Users\**CURRENT USER**\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup ```

2) Set LBRY Desktop app to start along with windows startup set 

		OBS: python on PATH are also required
		
3) Set your twitter keys (offered to you on your twitter dev account) and channel in config.yaml file

![](https://i.ibb.co/6FLcwPN/Screenshot-1.png)
## 1.b) Auto-Tweet (for Linux) 

Open and edit [crontab](https://linuxcommandlibrary.com/man/crontab):

``` crontab -e ```

Add the following lines to either: 

**Check and Auto-Tweet your last post on every system start**

``` @reboot python3 [part to python script] ```

**Check and Auto-Tweet your last post every hour**

``` @hourly python3 [part to python script] ```

The ```[part to python script]``` could be for example ```/home/supermario/t.py```

## 2) Channel Posting ( beta testing ) 
---
- Post your entire LBRY Channel, post by post every X hours 
(For users that never posted their LBRY videos on Twitter) 

```python3 /path/to/script/channel_posting.py```
the ```/path/to/script/``` could be ```/home/user/```
---
** Twitter developer account is required for API KEYS configuration
** Set your twitter keys and channel in config.yaml file 

### Check More tools :tools: from [@vlad](https://odysee.com/@code:a) and from [@Simonschubert](https://odysee.com/@simonschubert:d)  
 - Wanna help ? Get in touch on [LBRY Discord Server](https://chat.lbry.org) or [LBRYnomics Server](https://lbrynomics.com)

### Check Other LBRY TOOLS

[LBRY TOOLS](https://odysee.com/@code:a/tools:4)

