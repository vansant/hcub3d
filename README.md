hcub3d
======

#Add SECRET_KEY to ~/.bash_profile

##1 Open ~/.bash_profile in a text editor
$ nano ~/.bash_profile

##2 Add this line and make sure to include your own secret key
export SECRET_KEY="You will add your secret key here"

##3 Save ~/.bash_profile
##4 Close and reopen terminal

##5 Verify SECRET_KEY environment variable was set
$ echo $SECRET_KEY

