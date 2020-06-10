#!/bin/bash

echo "Select your choice:"
echo "Press 1 to display a message"
echo "Press 2 to display another special message"
echo "Press 3 to display a message" 
	read CHOICE
	case $CHOICE in

		1)echo Hello world;;
		2)echo This message is cooler than you;;
		3)echo thinking...;;
	*	)echo Invalid selection;;
	esac
