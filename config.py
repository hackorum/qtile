from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "st"

keys = [
    Key([mod], "p", lazy.spawn("dmenu_run -p 'Run:'")),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "t", lazy.window.toggle_floating()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "b", lazy.spawn("brave")),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +10%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -10%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute toggle")),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        ]
    )

layout_config = {
    "border_width": 2,
    "margin": 8,
    "border_focus": "98c379",
    "border_normal": "e5c07b",
}

layouts = [
    layout.MonadTall(**layout_config),
    layout.Columns(border_focus="#98c379", border_normal="#e5c07b", margin=8),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=12,
    padding=2,
)
extension_defaults = widget_defaults.copy()

colors = [
    "#282c34",
    "#e06c75",
    "#98c379",
    "#e5c07b",
    "#61afef",
    "#c678dd",
    "#56b6c2",
    "#ffffff",
]

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename="~/.config/qtile/icons/logo.png",
                    scale="True",
                    margin=4,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal)},
                ),
                widget.GroupBox(
                    font="FiraCode Nerd Font",
                    fontsize=12,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    rounded=False,
                    highlight_method="line",
                    this_current_screen_border=colors[2],
                    other_screen_border=colors[4],
                    foreground=colors[2],
                    active=colors[7],
                    inactive=colors[7],
                    highlight_color="#cccccc55",
                ),
                widget.WindowName(),
                widget.Sep(
                    linewidth=0,
                    padding=40,
                ),
                widget.Systray(),
                widget.TextBox(
                    text="",
                    padding=-9,
                    fontsize=50,
                    foreground=colors[4],
                ),
                widget.CurrentLayoutIcon(
                    foreground=colors[0], background=colors[4], padding=0, scale=0.7
                ),
                widget.CurrentLayout(background=colors[4], padding=5),
                widget.TextBox(
                    text="",
                    padding=-9,
                    fontsize=50,
                    foreground=colors[2],
                    background=colors[4],
                ),
                widget.TextBox(text="⟳", background=colors[2], padding=3),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_checkupdates",
                    display_format="{updates} Updates",
                    no_update_string="0 Updates",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            terminal + " -e sudo pacman -Syu"
                        )
                    },
                    background=colors[2],
                    padding=5,
                ),
                widget.TextBox(
                    text="",
                    padding=-9,
                    fontsize=50,
                    foreground=colors[4],
                    background=colors[2],
                ),
                widget.TextBox(text="", background=colors[4]),
                widget.Battery(update_interval=10, background=colors[4], padding=10),
                widget.TextBox(
                    text="",
                    padding=-9,
                    fontsize=50,
                    background=colors[4],
                    foreground=colors[2],
                ),
                widget.TextBox(text="", background=colors[2], padding=3),
                widget.Clock(
                    background=colors[2], format="%A, %B %d - %H:%M ", padding=10
                ),
            ],
            24,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename="~/.config/qtile/icons/logo.png",
                    scale="True",
                    margin=4,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal)},
                ),
                widget.GroupBox(
                    font="FiraCode Nerd Font",
                    fontsize=12,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    rounded=False,
                    highlight_method="line",
                    this_current_screen_border=colors[2],
                    other_screen_border=colors[4],
                    foreground=colors[2],
                    active=colors[7],
                    inactive=colors[7],
                    highlight_color="#cccccc55",
                ),
                widget.WindowName(),
                widget.Sep(
                    linewidth=0,
                    padding=40,
                ),
                widget.Systray(),
                widget.TextBox(
                    text="",
                    padding=-9,
                    fontsize=50,
                    foreground=colors[4],
                ),
                widget.CurrentLayoutIcon(
                    foreground=colors[0], background=colors[4], padding=0, scale=0.7
                ),
                widget.CurrentLayout(background=colors[4], padding=5),
                widget.TextBox(
                    text="",
                    padding=-9,
                    fontsize=50,
                    foreground=colors[2],
                    background=colors[4],
                ),
                widget.TextBox(text="⟳", background=colors[2], padding=3),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_checkupdates",
                    display_format="{updates} Updates",
                    no_update_string="0 Updates",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            terminal + " -e sudo pacman -Syu"
                        )
                    },
                    background=colors[2],
                    padding=5,
                ),
                widget.TextBox(
                    text="",
                    padding=-9,
                    fontsize=50,
                    foreground=colors[4],
                    background=colors[2],
                ),
                widget.TextBox(text="", background=colors[4]),
                widget.Battery(update_interval=10, background=colors[4], padding=10),
                widget.TextBox(
                    text="",
                    padding=-9,
                    fontsize=50,
                    background=colors[4],
                    foreground=colors[2],
                ),
                widget.TextBox(text="", background=colors[2], padding=3),
                widget.Clock(
                    background=colors[2], format="%A, %B %d - %H:%M ", padding=10
                ),
            ],
            24,
        ),
    ),
]

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
