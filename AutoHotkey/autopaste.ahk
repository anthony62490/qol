;
; Enters and submits a series of strings kept in Array.
; Created to submit large numbers of commands to Discord because I don't want to
;

#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
CoordMode, Mouse, Screen ;

Array := []

Click, 1134, 1028

for index, element in Array ;
{
    SendRaw, %element%
	Sleep, 800
	Send, {enter}
	Sleep, 2200
}