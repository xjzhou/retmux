# retmux change log

## 2020-08-26 VERSION 1.0.2
- bugfix: support for tmux 2.
<pre>
https://raw.githubusercontent.com/tmux/tmux/master/CHANGES
Support for windows larger than the client. This adds two new options,
 window-size and default-size, and a new command, resize-window. The
 force-width and force-height options and the session_width and session_height
 formats have been removed.
 default-size = 318x37

CMD_LIST_SESSIONS    = config.CMD_SEP.join(['tmux', 'list-sessions', '-F#S:=:(#{session_width},#{session_height}):=:#{session_attached}'])
</pre>

## 2013-12-31 VERSION 1.0.1
- bugfix: session/window names with spaces

## 2013-12-23 VERSION 1.0.0       
- first release
