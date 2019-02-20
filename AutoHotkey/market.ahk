#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
CoordMode, Mouse, Screen ;

^k::
	Send, ^c
	Click, 1134, 1028
	Sleep, 100
	Send, ^v
	Send, {enter}
	Sleep, 500
	MouseMove, 1290, 640
	Sleep, 600
	Click, down
	Sleep, 100
	MouseMove, 1158, 457
	Sleep, 100
	Click, up
	Sleep, 100
	Send, ^c
	Sleep, 100
	Send, ^c
	Sleep, 100
	Send, ^c
	Click, -453, 1049
	Sleep, 100
	Send, n
	Sleep, 100
	Send, {enter}
	Sleep, 100
	Send, ^v
	Sleep, 100
	Send, {enter}
	Sleep, 300
	Send, {Up}
	Send, {End}
	Send, {Shift down}
	Send, {Up}
	Send, {Up}
	Send, {Right}
	Send, {Shift up}
	Send, ^c
	Click, 1134, 1028
	Sleep, 100
	Send, ^v
	Send, {enter}