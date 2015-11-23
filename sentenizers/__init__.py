#!/usr/bin/python3.4

########################################################################################################################
##### INFORMATION ######################################################################################################
### @PROJECT_NAME:		SPLAT: Speech Processing and Linguistic Annotation Tool										 ###
### @VERSION_NUMBER:																								 ###
### @PROJECT_SITE:		github.com/meyersbs/SPLAT																     ###
### @AUTHOR_NAME:		Benjamin S. Meyers																			 ###
### @CONTACT_EMAIL:		bsm9339@rit.edu																				 ###
### @LICENSE_TYPE:																									 ###
########################################################################################################################
########################################################################################################################

"""
This package contains the following files:
	[01] CleanSentenizer.py
			Provides the functionality to generate a list of sentences from a text input with newlines removed.
	[02] RawSentenizer.py
			Provides the functionality to generate a list of unprocessed sentences from a text input.
	[03] Sentenizer.py
			An abstract class that is implemented by the other Sentenizers in this directory.
"""