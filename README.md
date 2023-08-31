python script for saving tab contents, config and ssfn* files to your email from steam

before using the script you will need to already access a specific Steam account-

ssfn* is the steam guard file (Steam Guard, the Steam client generates a file named "ssfn" followed by a series of numbers. This file is stored on the device you're using and is associated with your Steam account. It is used as part of the two-factor authentication process to verify your identity when logging in. The ssfn file is stored locally on your device and is specific to that device.) (example: ssfn1000080598613390841 - this is your steam guard ID) 

using the ssfn string hackers can bypass your 2fa on steam and access all of your data

copying the config subfolder after gaining access to the account will give you all of the information that you need for the Steam account (most importantly the ssfn* which will help you log into the account even if the password was changed)



###
shutil.rmtree() Removes all traces of the copy that you made.
files that start with "ssfn" in the steam_folder are copied to the temp_folder.
