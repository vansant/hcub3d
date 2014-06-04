hcub3d
======

#Add SECRET_KEY to ~/.bash_profile

## Open ~/.bash_profile in a text editor
$ nano ~/.bash_profile

## Add this line and make sure to include your own secret key
export SECRET_KEY="You will add your secret key here"

## Save ~/.bash_profile
# Close and reopen terminal

## Verify SECRET_KEY environment variable was set
$ echo $SECRET_KEY

