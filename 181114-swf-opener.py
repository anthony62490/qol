# Anthony Magno - 2018/11/14
# Execute this file while passing in a single swf file path. It will output an
# html file that can open the swf in a browser
###############################################################################
import sys, re

def main(filename):
    title = re.search('([a-zA-Z_\-0-9]*)(\.swf$)', filename, re.M).group(1)
    print('\nfile:', filename)
    print('name:', title)
    out = """<!DOCTYPE html >
    <html lang="en" xml:lang="en">
            <head>
                    <title>""" + title + """</title>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                    <style type="text/css" media="screen">
                    html, body { height:100%; background-color: #000000;}
                    body { margin:0; padding:0; overflow:hidden; }
                    #flashContent { width:100%; height:100%; }
                    </style>
            </head>
            <body>
                    <div id="flashContent">
                            <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="100%" height="100%" id=\"""" + title + """\" align="middle">
                                    <param name="movie" value=\"""" + filename + """\" />
                                    <param name="quality" value="high" />
                                    <param name="bgcolor" value="#000000" />
                                    <param name="play" value="true" />
                                    <param name="loop" value="true" />
                                    <param name="wmode" value="window" />
                                    <param name="scale" value="default" />
                                    <param name="menu" value="true" />
                                    <param name="devicefont" value="false" />
                                    <param name="salign" value="" />
                                    <param name="allowScriptAccess" value="sameDomain" />
                                    <!--[if !IE]>-->
                                    <object type="application/x-shockwave-flash" data=\"""" + filename + """\" width="100%" height="100%">
                                            <param name="movie" value=\"""" + filename + """\" />
                                            <param name="quality" value="high" />
                                            <param name="bgcolor" value="#000000" />
                                            <param name="play" value="true" />
                                            <param name="loop" value="true" />
                                            <param name="wmode" value="window" />
                                            <param name="scale" value="default" />
                                            <param name="menu" value="true" />
                                            <param name="devicefont" value="false" />
                                            <param name="salign" value="" />
                                            <param name="allowScriptAccess" value="sameDomain" />
                                    <!--<![endif]-->
                                            <a href="http://www.adobe.com/go/getflash">
                                                    <img src="http://www.adobe.com/images/shared/download_buttons/get_flash_player.gif" alt="Get Adobe Flash player" />
                                            </a>
                                    <!--[if !IE]>-->
                                    </object>
                                    <!--<![endif]-->
                            </object>
                    </div>
            </body>
    </html>"""

if __name__== "__main__":
    main(str(sys.argv[1]))
