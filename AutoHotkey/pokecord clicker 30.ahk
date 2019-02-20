#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#MaxThreadsPerHotkey 2
count := 0

^j::
    Toggle := !Toggle
	if(Toggle)
	{
		Send, start (press Ctrl J to exit)
		Send, {enter}
	}
    while Toggle
    {
        Sleep, 30000
		if(!Toggle)
		{
			Send, end
			Send, {enter}
			break
		}
        Send, %count%
		count := count +1
		Send, {enter}
    }
	if(!Toggle)
	{
		Send, stand by
		Send, {enter}
	}
return