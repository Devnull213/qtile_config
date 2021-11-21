

from libqtile import bar, layout, widget
from libqtile.config import Screen
from os import path

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#000000", "#000000"],
                    font='UbuntuMono Nerd Font',
                    fontsize=14,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#0f94d2", "#0f94d2"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    # highlight_method='border',
                    # highlight_color='#0f94d2',
                    # this_current_screen_border=["#0f94d2", "#0f94d2"],
                    # this_screen_border=["#0f94d2", "#0f94d2"],
                    #other_current_screen_border=["#0f101a", "#0f101a"],
                    #other_screen_border=["#0f101a", "#0f101a"]
                ),


                widget.Spacer(
                    lenght=50,
                    background=["#000000", "#000000"],

                ),

                widget.WindowName(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#000000", "#000000"],
                    font='UbuntuMono Nerd Font Bold',
                    fontsize=14,
                ),

                widget.Spacer(
                    lenght=200,
                    background=["#000000", "#000000"],

                ),

                # widget.CheckUpdates(
                    # distro='Arch',
                    # display_format='Pacman: {updates}',
                    # no_update_string='Pacman: 0',
                    # color_no_updates='#1bdd3a'
                # ),

                widget.Spacer(
                    lenght=200,
                    background=["#000000", "#000000"],

                ),

                widget.Sep(
                    background=["#000000","#000000"],
                    linewidth=0,
                    padding=6,
                ),


                widget.Image(
                    filename=path.join(path.expanduser('~'), 'Downloads', 'bar2.png')
                ),


                widget.CPU(
                    background=["#181a1b", "#181a1b"],
                    padding=5,
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold',
                    ),


                widget.Sep(
                    background=["#181a1b", "#181a1b"],
                    linewidth=0,
                    padding=6,
                ),

                widget.Image(
                    filename=path.join(path.expanduser('~'), 'Downloads', 'bar1.png')
                ),

                widget.Net(
                    format='{down} ↓↑ {up}',
                    padding=5,
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold',
                    ),

                widget.Sep(
                    background=["#000000","#000000"],
                    linewidth=0,
                    padding=6,
                ),


                widget.Image(
                    filename=path.join(path.expanduser('~'), 'Downloads', 'bar2.png')
                ),

                widget.CryptoTicker(
                    background=["#181a1b", "#181a1b"],
                    symbol='',
                    currency='USD',
                    crypto='BTC',
                    format='{symbol} {amount}',
                    update_interval=60,
                    padding=5,
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold',

                ),

                widget.Sep(
                    background=["#181a1b", "#181a1b"],
                    linewidth=0,
                    padding=6,
                ),

                widget.Image(
                    filename=path.join(path.expanduser('~'), 'Downloads', 'bar1.png')
                ),

                widget.CurrentLayoutIcon(
                    scale=0.65,
                    background=["#000000","#000000"],
                    foreground=["#0f101a", "#0f101a"],
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold',
                ),
                widget.CurrentLayout(
                    background=["#000000","#000000"],
                    foreground=["#f1ffff", "#f1ffff"],
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold',

                ),
                widget.Sep(
                    background=["#000000","#000000"],
                    linewidth=0,
                    padding=6,
                ),


                widget.Image(
                    filename=path.join(path.expanduser('~'), 'Downloads', 'bar2.png')
                ),


                widget.TextBox(
                    background=["#181a1b", "#181a1b"],
                    foreground=["#f1ffff", "#f1ffff"],
                    font='UbuntuMono Nerd Font Bold',
                    padding=5,
                    text='',
                    fontsize=16,
                ),
                widget.Clock(
                    background=["#181a1b", "#181a1b"],
                    foreground=["#f1ffff", "#f1ffff"],
                    padding=5,
                    font='UbuntuMono Nerd Font Bold',
                    fontsize=14,
                    format='%d/%m/%Y  %I:%M'),
            ],
            26,
            opacity=1,
            background="#000000",
        ),
    ),


    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#000000", "#000000"],
                    font='UbuntuMono Nerd Font',
                    fontsize=14,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#0f94d2", "#0f94d2"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    # highlight_method='border',
                    # highlight_color='#0f94d2',
                    # this_current_screen_border=["#0f94d2", "#0f94d2"],
                    # this_screen_border=["#0f94d2", "#0f94d2"],
                    #other_current_screen_border=["#0f101a", "#0f101a"],
                    #other_screen_border=["#0f101a", "#0f101a"]
                ),


                widget.Spacer(
                    lenght=50,
                    background=["#000000", "#000000"],

                ),

                widget.WindowName(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#000000", "#000000"],
                    font='UbuntuMono Nerd Font Bold',
                    fontsize=14,
                ),

                widget.Spacer(
                    lenght=200,
                    background=["#000000", "#000000"],

                ),

                # widget.CheckUpdates(
                    # distro='Arch',
                    # display_format='Pacman: {updates}',
                    # no_update_string='Pacman: 0',
                    # color_no_updates='#1bdd3a'
                # ),

                widget.Spacer(
                    lenght=200,
                    background=["#000000", "#000000"],

                ),

                widget.Sep(
                    background=["#000000","#000000"],
                    linewidth=0,
                    padding=6,
                ),


                widget.Image(
                    filename=path.join(path.expanduser('~'), 'Downloads', 'bar2.png')
                ),


                widget.CPU(
                    background=["#181a1b", "#181a1b"],
                    padding=5,
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold',
                    ),


                widget.Sep(
                    background=["#181a1b", "#181a1b"],
                    linewidth=0,
                    padding=6,
                ),

                widget.Image(
                    filename=path.join(path.expanduser('~'), 'Downloads', 'bar1.png')
                ),

                widget.Net(
                    format='{down} ↓↑ {up}',
                    padding=5,
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold',
                    ),

                widget.Sep(
                    background=["#000000","#000000"],
                    linewidth=0,
                    padding=6,
                ),


                widget.Image(
                    filename=path.join(path.expanduser('~'), 'Downloads', 'bar2.png')
                ),

                widget.CryptoTicker(
                    background=["#181a1b", "#181a1b"],
                    symbol='',
                    currency='USD',
                    crypto='BTC',
                    format='{symbol} {amount}',
                    update_interval=60,
                    padding=5,
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold',

                ),

                widget.Sep(
                    background=["#181a1b", "#181a1b"],
                    linewidth=0,
                    padding=6,
                ),

                widget.Image(
                    filename=path.join(path.expanduser('~'), 'Downloads', 'bar1.png')
                ),

                widget.CurrentLayoutIcon(
                    scale=0.65,
                    background=["#000000","#000000"],
                    foreground=["#0f101a", "#0f101a"],
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold',
                ),
                widget.CurrentLayout(
                    background=["#000000","#000000"],
                    foreground=["#f1ffff", "#f1ffff"],
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold',

                ),
                widget.Sep(
                    background=["#000000","#000000"],
                    linewidth=0,
                    padding=6,
                ),


                widget.Image(
                    filename=path.join(path.expanduser('~'), 'Downloads', 'bar2.png')
                ),


                widget.TextBox(
                    background=["#181a1b", "#181a1b"],
                    foreground=["#f1ffff", "#f1ffff"],
                    font='UbuntuMono Nerd Font Bold',
                    padding=5,
                    text='',
                    fontsize=16,
                ),
                widget.Clock(
                    background=["#181a1b", "#181a1b"],
                    foreground=["#f1ffff", "#f1ffff"],
                    padding=5,
                    font='UbuntuMono Nerd Font Bold',
                    fontsize=14,
                    format='%d/%m/%Y  %I:%M'),
            ],
            26,
            opacity=1,
            background="#000000",
        ),
    ),
]
