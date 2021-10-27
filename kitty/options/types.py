# generated by gen-config.py DO NOT edit

import typing
from array import array
from kitty.conf.utils import KeyAction
import kitty.conf.utils
from kitty.constants import is_macos
import kitty.constants
from kitty.options.utils import KeyDefinition, KeyMap, MouseMap, MouseMapping, SequenceMap, TabBarMarginHeight
import kitty.options.utils
from kitty.rgb import Color
import kitty.rgb
from kitty.types import FloatEdges, SingleKey
import kitty.types

if typing.TYPE_CHECKING:
    choices_for_background_image_layout = typing.Literal['mirror-tiled', 'scaled', 'tiled']
    choices_for_default_pointer_shape = typing.Literal['arrow', 'beam', 'hand']
    choices_for_linux_display_server = typing.Literal['auto', 'wayland', 'x11']
    choices_for_macos_show_window_title_in = typing.Literal['all', 'menubar', 'none', 'window']
    choices_for_placement_strategy = typing.Literal['center', 'top-left']
    choices_for_pointer_shape_when_dragging = typing.Literal['arrow', 'beam', 'hand']
    choices_for_pointer_shape_when_grabbed = typing.Literal['arrow', 'beam', 'hand']
    choices_for_strip_trailing_spaces = typing.Literal['always', 'never', 'smart']
    choices_for_tab_bar_align = typing.Literal['left', 'center', 'right']
    choices_for_tab_bar_style = typing.Literal['fade', 'hidden', 'powerline', 'separator', 'slant', 'custom']
    choices_for_tab_powerline_style = typing.Literal['angled', 'round', 'slanted']
    choices_for_tab_switch_strategy = typing.Literal['last', 'left', 'previous', 'right']
else:
    choices_for_background_image_layout = str
    choices_for_default_pointer_shape = str
    choices_for_linux_display_server = str
    choices_for_macos_show_window_title_in = str
    choices_for_placement_strategy = str
    choices_for_pointer_shape_when_dragging = str
    choices_for_pointer_shape_when_grabbed = str
    choices_for_strip_trailing_spaces = str
    choices_for_tab_bar_align = str
    choices_for_tab_bar_style = str
    choices_for_tab_powerline_style = str
    choices_for_tab_switch_strategy = str

option_names = (  # {{{
 'active_border_color',
 'active_tab_background',
 'active_tab_font_style',
 'active_tab_foreground',
 'active_tab_title_template',
 'adjust_baseline',
 'adjust_column_width',
 'adjust_line_height',
 'allow_hyperlinks',
 'allow_remote_control',
 'background',
 'background_image',
 'background_image_layout',
 'background_image_linear',
 'background_opacity',
 'background_tint',
 'bell_border_color',
 'bell_on_tab',
 'bell_path',
 'bold_font',
 'bold_italic_font',
 'box_drawing_scale',
 'clear_all_mouse_actions',
 'clear_all_shortcuts',
 'click_interval',
 'clipboard_control',
 'clipboard_max_size',
 'close_on_child_death',
 'color0',
 'color1',
 'color2',
 'color3',
 'color4',
 'color5',
 'color6',
 'color7',
 'color8',
 'color9',
 'color10',
 'color11',
 'color12',
 'color13',
 'color14',
 'color15',
 'color16',
 'color17',
 'color18',
 'color19',
 'color20',
 'color21',
 'color22',
 'color23',
 'color24',
 'color25',
 'color26',
 'color27',
 'color28',
 'color29',
 'color30',
 'color31',
 'color32',
 'color33',
 'color34',
 'color35',
 'color36',
 'color37',
 'color38',
 'color39',
 'color40',
 'color41',
 'color42',
 'color43',
 'color44',
 'color45',
 'color46',
 'color47',
 'color48',
 'color49',
 'color50',
 'color51',
 'color52',
 'color53',
 'color54',
 'color55',
 'color56',
 'color57',
 'color58',
 'color59',
 'color60',
 'color61',
 'color62',
 'color63',
 'color64',
 'color65',
 'color66',
 'color67',
 'color68',
 'color69',
 'color70',
 'color71',
 'color72',
 'color73',
 'color74',
 'color75',
 'color76',
 'color77',
 'color78',
 'color79',
 'color80',
 'color81',
 'color82',
 'color83',
 'color84',
 'color85',
 'color86',
 'color87',
 'color88',
 'color89',
 'color90',
 'color91',
 'color92',
 'color93',
 'color94',
 'color95',
 'color96',
 'color97',
 'color98',
 'color99',
 'color100',
 'color101',
 'color102',
 'color103',
 'color104',
 'color105',
 'color106',
 'color107',
 'color108',
 'color109',
 'color110',
 'color111',
 'color112',
 'color113',
 'color114',
 'color115',
 'color116',
 'color117',
 'color118',
 'color119',
 'color120',
 'color121',
 'color122',
 'color123',
 'color124',
 'color125',
 'color126',
 'color127',
 'color128',
 'color129',
 'color130',
 'color131',
 'color132',
 'color133',
 'color134',
 'color135',
 'color136',
 'color137',
 'color138',
 'color139',
 'color140',
 'color141',
 'color142',
 'color143',
 'color144',
 'color145',
 'color146',
 'color147',
 'color148',
 'color149',
 'color150',
 'color151',
 'color152',
 'color153',
 'color154',
 'color155',
 'color156',
 'color157',
 'color158',
 'color159',
 'color160',
 'color161',
 'color162',
 'color163',
 'color164',
 'color165',
 'color166',
 'color167',
 'color168',
 'color169',
 'color170',
 'color171',
 'color172',
 'color173',
 'color174',
 'color175',
 'color176',
 'color177',
 'color178',
 'color179',
 'color180',
 'color181',
 'color182',
 'color183',
 'color184',
 'color185',
 'color186',
 'color187',
 'color188',
 'color189',
 'color190',
 'color191',
 'color192',
 'color193',
 'color194',
 'color195',
 'color196',
 'color197',
 'color198',
 'color199',
 'color200',
 'color201',
 'color202',
 'color203',
 'color204',
 'color205',
 'color206',
 'color207',
 'color208',
 'color209',
 'color210',
 'color211',
 'color212',
 'color213',
 'color214',
 'color215',
 'color216',
 'color217',
 'color218',
 'color219',
 'color220',
 'color221',
 'color222',
 'color223',
 'color224',
 'color225',
 'color226',
 'color227',
 'color228',
 'color229',
 'color230',
 'color231',
 'color232',
 'color233',
 'color234',
 'color235',
 'color236',
 'color237',
 'color238',
 'color239',
 'color240',
 'color241',
 'color242',
 'color243',
 'color244',
 'color245',
 'color246',
 'color247',
 'color248',
 'color249',
 'color250',
 'color251',
 'color252',
 'color253',
 'color254',
 'color255',
 'command_on_bell',
 'confirm_os_window_close',
 'copy_on_select',
 'cursor',
 'cursor_beam_thickness',
 'cursor_blink_interval',
 'cursor_shape',
 'cursor_stop_blinking_after',
 'cursor_text_color',
 'cursor_underline_thickness',
 'default_pointer_shape',
 'detect_urls',
 'dim_opacity',
 'disable_ligatures',
 'draw_minimal_borders',
 'dynamic_background_opacity',
 'editor',
 'enable_audio_bell',
 'enabled_layouts',
 'env',
 'file_transfer_confirmation_bypass',
 'focus_follows_mouse',
 'font_family',
 'font_features',
 'font_size',
 'force_ltr',
 'foreground',
 'hide_window_decorations',
 'inactive_border_color',
 'inactive_tab_background',
 'inactive_tab_font_style',
 'inactive_tab_foreground',
 'inactive_text_alpha',
 'initial_window_height',
 'initial_window_width',
 'input_delay',
 'italic_font',
 'kitten_alias',
 'kitty_mod',
 'linux_display_server',
 'listen_on',
 'macos_custom_beam_cursor',
 'macos_hide_from_tasks',
 'macos_option_as_alt',
 'macos_quit_when_last_window_closed',
 'macos_show_window_title_in',
 'macos_thicken_font',
 'macos_titlebar_color',
 'macos_traditional_fullscreen',
 'macos_window_resizable',
 'map',
 'mark1_background',
 'mark1_foreground',
 'mark2_background',
 'mark2_foreground',
 'mark3_background',
 'mark3_foreground',
 'mouse_hide_wait',
 'mouse_map',
 'open_url_with',
 'placement_strategy',
 'pointer_shape_when_dragging',
 'pointer_shape_when_grabbed',
 'remember_window_size',
 'repaint_delay',
 'resize_debounce_time',
 'resize_draw_strategy',
 'resize_in_steps',
 'scrollback_fill_enlarged_window',
 'scrollback_lines',
 'scrollback_pager',
 'scrollback_pager_history_size',
 'select_by_word_characters',
 'selection_background',
 'selection_foreground',
 'shell',
 'shell_integration',
 'single_window_margin_width',
 'startup_session',
 'strip_trailing_spaces',
 'symbol_map',
 'sync_to_monitor',
 'tab_activity_symbol',
 'tab_bar_align',
 'tab_bar_background',
 'tab_bar_edge',
 'tab_bar_margin_color',
 'tab_bar_margin_height',
 'tab_bar_margin_width',
 'tab_bar_min_tabs',
 'tab_bar_style',
 'tab_fade',
 'tab_powerline_style',
 'tab_separator',
 'tab_switch_strategy',
 'tab_title_template',
 'term',
 'touch_scroll_multiplier',
 'update_check_interval',
 'url_color',
 'url_excluded_characters',
 'url_prefixes',
 'url_style',
 'visual_bell_duration',
 'watcher',
 'wayland_titlebar_color',
 'wheel_scroll_multiplier',
 'window_alert_on_bell',
 'window_border_width',
 'window_margin_width',
 'window_padding_width',
 'window_resize_step_cells',
 'window_resize_step_lines')  # }}}


class Options:
    active_border_color: typing.Optional[kitty.rgb.Color] = Color(red=0, green=255, blue=0)
    active_tab_background: Color = Color(red=238, green=238, blue=238)
    active_tab_font_style: typing.Tuple[bool, bool] = (True, True)
    active_tab_foreground: Color = Color(red=0, green=0, blue=0)
    active_tab_title_template: typing.Optional[str] = None
    adjust_baseline: typing.Union[int, float] = 0
    adjust_column_width: typing.Union[int, float] = 0
    adjust_line_height: typing.Union[int, float] = 0
    allow_hyperlinks: int = 1
    allow_remote_control: str = 'n'
    background: Color = Color(red=0, green=0, blue=0)
    background_image: typing.Optional[str] = None
    background_image_layout: choices_for_background_image_layout = 'tiled'
    background_image_linear: bool = False
    background_opacity: float = 1.0
    background_tint: float = 0
    bell_border_color: Color = Color(red=255, green=90, blue=0)
    bell_on_tab: bool = True
    bell_path: typing.Optional[str] = None
    bold_font: str = 'auto'
    bold_italic_font: str = 'auto'
    box_drawing_scale: typing.Tuple[float, float, float, float] = (0.001, 1.0, 1.5, 2.0)
    clear_all_mouse_actions: bool = False
    clear_all_shortcuts: bool = False
    click_interval: float = -1.0
    clipboard_control: typing.Tuple[str, ...] = ('write-clipboard', 'write-primary', 'read-clipboard-ask', 'read-primary-ask')
    clipboard_max_size: float = 64.0
    close_on_child_death: bool = False
    command_on_bell: typing.List[str] = ['none']
    confirm_os_window_close: int = 0
    copy_on_select: str = ''
    cursor: Color = Color(red=204, green=204, blue=204)
    cursor_beam_thickness: float = 1.5
    cursor_blink_interval: float = -1.0
    cursor_shape: int = 1
    cursor_stop_blinking_after: float = 15.0
    cursor_text_color: typing.Optional[kitty.rgb.Color] = Color(red=17, green=17, blue=17)
    cursor_underline_thickness: float = 2.0
    default_pointer_shape: choices_for_default_pointer_shape = 'beam'
    detect_urls: bool = True
    dim_opacity: float = 0.75
    disable_ligatures: int = 0
    draw_minimal_borders: bool = True
    dynamic_background_opacity: bool = False
    editor: str = '.'
    enable_audio_bell: bool = True
    enabled_layouts: typing.List[str] = ['fat', 'grid', 'horizontal', 'splits', 'stack', 'tall', 'vertical']
    file_transfer_confirmation_bypass: str = ''
    focus_follows_mouse: bool = False
    font_family: str = 'monospace'
    font_size: float = 11.0
    force_ltr: bool = False
    foreground: Color = Color(red=221, green=221, blue=221)
    hide_window_decorations: int = 0
    inactive_border_color: Color = Color(red=204, green=204, blue=204)
    inactive_tab_background: Color = Color(red=153, green=153, blue=153)
    inactive_tab_font_style: typing.Tuple[bool, bool] = (False, False)
    inactive_tab_foreground: Color = Color(red=68, green=68, blue=68)
    inactive_text_alpha: float = 1.0
    initial_window_height: typing.Tuple[int, str] = (400, 'px')
    initial_window_width: typing.Tuple[int, str] = (640, 'px')
    input_delay: int = 3
    italic_font: str = 'auto'
    kitty_mod: int = 5
    linux_display_server: choices_for_linux_display_server = 'auto'
    listen_on: str = 'none'
    macos_custom_beam_cursor: bool = False
    macos_hide_from_tasks: bool = False
    macos_option_as_alt: int = 0
    macos_quit_when_last_window_closed: bool = False
    macos_show_window_title_in: choices_for_macos_show_window_title_in = 'all'
    macos_thicken_font: float = 0
    macos_titlebar_color: int = 0
    macos_traditional_fullscreen: bool = False
    macos_window_resizable: bool = True
    mark1_background: Color = Color(red=152, green=211, blue=203)
    mark1_foreground: Color = Color(red=0, green=0, blue=0)
    mark2_background: Color = Color(red=242, green=220, blue=211)
    mark2_foreground: Color = Color(red=0, green=0, blue=0)
    mark3_background: Color = Color(red=242, green=116, blue=188)
    mark3_foreground: Color = Color(red=0, green=0, blue=0)
    mouse_hide_wait: float = 0.0 if is_macos else 3.0
    open_url_with: typing.List[str] = ['default']
    placement_strategy: choices_for_placement_strategy = 'center'
    pointer_shape_when_dragging: choices_for_pointer_shape_when_dragging = 'beam'
    pointer_shape_when_grabbed: choices_for_pointer_shape_when_grabbed = 'arrow'
    remember_window_size: bool = True
    repaint_delay: int = 10
    resize_debounce_time: float = 0.1
    resize_draw_strategy: int = 0
    resize_in_steps: bool = False
    scrollback_fill_enlarged_window: bool = False
    scrollback_lines: int = 2000
    scrollback_pager: typing.List[str] = ['less', '--chop-long-lines', '--RAW-CONTROL-CHARS', '+INPUT_LINE_NUMBER']
    scrollback_pager_history_size: int = 0
    select_by_word_characters: str = '@-./_~?&=%+#'
    selection_background: Color = Color(red=255, green=250, blue=205)
    selection_foreground: typing.Optional[kitty.rgb.Color] = Color(red=0, green=0, blue=0)
    shell: str = '.'
    shell_integration: str = 'enabled'
    single_window_margin_width: FloatEdges = FloatEdges(left=-1.0, top=-1.0, right=-1.0, bottom=-1.0)
    startup_session: typing.Optional[str] = None
    strip_trailing_spaces: choices_for_strip_trailing_spaces = 'never'
    sync_to_monitor: bool = True
    tab_activity_symbol: typing.Optional[str] = None
    tab_bar_align: choices_for_tab_bar_align = 'left'
    tab_bar_background: typing.Optional[kitty.rgb.Color] = None
    tab_bar_edge: int = 3
    tab_bar_margin_color: typing.Optional[kitty.rgb.Color] = None
    tab_bar_margin_height: TabBarMarginHeight = TabBarMarginHeight(outer=0, inner=0)
    tab_bar_margin_width: float = 0
    tab_bar_min_tabs: int = 2
    tab_bar_style: choices_for_tab_bar_style = 'fade'
    tab_fade: typing.Tuple[float, ...] = (0.25, 0.5, 0.75, 1.0)
    tab_powerline_style: choices_for_tab_powerline_style = 'angled'
    tab_separator: str = ' ┇'
    tab_switch_strategy: choices_for_tab_switch_strategy = 'previous'
    tab_title_template: str = '{title}'
    term: str = 'xterm-kitty'
    touch_scroll_multiplier: float = 1.0
    update_check_interval: float = 24.0
    url_color: Color = Color(red=0, green=135, blue=189)
    url_excluded_characters: str = ''
    url_prefixes: typing.Tuple[str, ...] = ('http', 'https', 'file', 'ftp', 'gemini', 'irc', 'gopher', 'mailto', 'news', 'git')
    url_style: int = 3
    visual_bell_duration: float = 0
    wayland_titlebar_color: int = 0
    wheel_scroll_multiplier: float = 5.0
    window_alert_on_bell: bool = True
    window_border_width: typing.Tuple[float, str] = (0.5, 'pt')
    window_margin_width: FloatEdges = FloatEdges(left=0, top=0, right=0, bottom=0)
    window_padding_width: FloatEdges = FloatEdges(left=0, top=0, right=0, bottom=0)
    window_resize_step_cells: int = 2
    window_resize_step_lines: int = 2
    env: typing.Dict[str, str] = {}
    font_features: typing.Dict[str, typing.Tuple[kitty.fonts.FontFeature, ...]] = {}
    kitten_alias: typing.Dict[str, typing.List[str]] = {}
    symbol_map: typing.Dict[typing.Tuple[int, int], str] = {}
    watcher: typing.Dict[str, str] = {}
    map: typing.List[kitty.options.utils.KeyDefinition] = []
    keymap: KeyMap = {}
    sequence_map: SequenceMap = {}
    mouse_map: typing.List[kitty.options.utils.MouseMapping] = []
    mousemap: MouseMap = {}
    color_table: "array[int]" = array("L", (
        0x000000, 0xcc0403, 0x19cb00, 0xcecb00, 0x0d73cc, 0xcb1ed1, 0x0dcdcd, 0xdddddd,
        0x767676, 0xf2201f, 0x23fd00, 0xfffd00, 0x1a8fff, 0xfd28ff, 0x14ffff, 0xffffff,
        0x000000, 0x00005f, 0x000087, 0x0000af, 0x0000d7, 0x0000ff, 0x005f00, 0x005f5f,
        0x005f87, 0x005faf, 0x005fd7, 0x005fff, 0x008700, 0x00875f, 0x008787, 0x0087af,
        0x0087d7, 0x0087ff, 0x00af00, 0x00af5f, 0x00af87, 0x00afaf, 0x00afd7, 0x00afff,
        0x00d700, 0x00d75f, 0x00d787, 0x00d7af, 0x00d7d7, 0x00d7ff, 0x00ff00, 0x00ff5f,
        0x00ff87, 0x00ffaf, 0x00ffd7, 0x00ffff, 0x5f0000, 0x5f005f, 0x5f0087, 0x5f00af,
        0x5f00d7, 0x5f00ff, 0x5f5f00, 0x5f5f5f, 0x5f5f87, 0x5f5faf, 0x5f5fd7, 0x5f5fff,
        0x5f8700, 0x5f875f, 0x5f8787, 0x5f87af, 0x5f87d7, 0x5f87ff, 0x5faf00, 0x5faf5f,
        0x5faf87, 0x5fafaf, 0x5fafd7, 0x5fafff, 0x5fd700, 0x5fd75f, 0x5fd787, 0x5fd7af,
        0x5fd7d7, 0x5fd7ff, 0x5fff00, 0x5fff5f, 0x5fff87, 0x5fffaf, 0x5fffd7, 0x5fffff,
        0x870000, 0x87005f, 0x870087, 0x8700af, 0x8700d7, 0x8700ff, 0x875f00, 0x875f5f,
        0x875f87, 0x875faf, 0x875fd7, 0x875fff, 0x878700, 0x87875f, 0x878787, 0x8787af,
        0x8787d7, 0x8787ff, 0x87af00, 0x87af5f, 0x87af87, 0x87afaf, 0x87afd7, 0x87afff,
        0x87d700, 0x87d75f, 0x87d787, 0x87d7af, 0x87d7d7, 0x87d7ff, 0x87ff00, 0x87ff5f,
        0x87ff87, 0x87ffaf, 0x87ffd7, 0x87ffff, 0xaf0000, 0xaf005f, 0xaf0087, 0xaf00af,
        0xaf00d7, 0xaf00ff, 0xaf5f00, 0xaf5f5f, 0xaf5f87, 0xaf5faf, 0xaf5fd7, 0xaf5fff,
        0xaf8700, 0xaf875f, 0xaf8787, 0xaf87af, 0xaf87d7, 0xaf87ff, 0xafaf00, 0xafaf5f,
        0xafaf87, 0xafafaf, 0xafafd7, 0xafafff, 0xafd700, 0xafd75f, 0xafd787, 0xafd7af,
        0xafd7d7, 0xafd7ff, 0xafff00, 0xafff5f, 0xafff87, 0xafffaf, 0xafffd7, 0xafffff,
        0xd70000, 0xd7005f, 0xd70087, 0xd700af, 0xd700d7, 0xd700ff, 0xd75f00, 0xd75f5f,
        0xd75f87, 0xd75faf, 0xd75fd7, 0xd75fff, 0xd78700, 0xd7875f, 0xd78787, 0xd787af,
        0xd787d7, 0xd787ff, 0xd7af00, 0xd7af5f, 0xd7af87, 0xd7afaf, 0xd7afd7, 0xd7afff,
        0xd7d700, 0xd7d75f, 0xd7d787, 0xd7d7af, 0xd7d7d7, 0xd7d7ff, 0xd7ff00, 0xd7ff5f,
        0xd7ff87, 0xd7ffaf, 0xd7ffd7, 0xd7ffff, 0xff0000, 0xff005f, 0xff0087, 0xff00af,
        0xff00d7, 0xff00ff, 0xff5f00, 0xff5f5f, 0xff5f87, 0xff5faf, 0xff5fd7, 0xff5fff,
        0xff8700, 0xff875f, 0xff8787, 0xff87af, 0xff87d7, 0xff87ff, 0xffaf00, 0xffaf5f,
        0xffaf87, 0xffafaf, 0xffafd7, 0xffafff, 0xffd700, 0xffd75f, 0xffd787, 0xffd7af,
        0xffd7d7, 0xffd7ff, 0xffff00, 0xffff5f, 0xffff87, 0xffffaf, 0xffffd7, 0xffffff,
        0x080808, 0x121212, 0x1c1c1c, 0x262626, 0x303030, 0x3a3a3a, 0x444444, 0x4e4e4e,
        0x585858, 0x626262, 0x6c6c6c, 0x767676, 0x808080, 0x8a8a8a, 0x949494, 0x9e9e9e,
        0xa8a8a8, 0xb2b2b2, 0xbcbcbc, 0xc6c6c6, 0xd0d0d0, 0xdadada, 0xe4e4e4, 0xeeeeee,
    ))
    config_paths: typing.Tuple[str, ...] = ()
    config_overrides: typing.Tuple[str, ...] = ()

    def __init__(self, options_dict: typing.Optional[typing.Dict[str, typing.Any]] = None) -> None:
        self.color_table = array(self.color_table.typecode, self.color_table)
        if options_dict is not None:
            null = object()
            for key in option_names:
                val = options_dict.get(key, null)
                if val is not null:
                    setattr(self, key, val)

    @property
    def _fields(self) -> typing.Tuple[str, ...]:
        return option_names

    def __iter__(self) -> typing.Iterator[str]:
        return iter(self._fields)

    def __len__(self) -> int:
        return len(self._fields)

    def _copy_of_val(self, name: str) -> typing.Any:
        ans = getattr(self, name)
        if isinstance(ans, dict):
            ans = ans.copy()
        elif isinstance(ans, list):
            ans = ans[:]
        return ans

    def _asdict(self) -> typing.Dict[str, typing.Any]:
        return {k: self._copy_of_val(k) for k in self}

    def _replace(self, **kw: typing.Any) -> "Options":
        ans = Options()
        for name in self:
            setattr(ans, name, self._copy_of_val(name))
        for name, val in kw.items():
            setattr(ans, name, val)
        return ans

    def __getitem__(self, key: typing.Union[int, str]) -> typing.Any:
        k = option_names[key] if isinstance(key, int) else key
        try:
            return getattr(self, k)
        except AttributeError:
            pass
        raise KeyError(f"No option named: {k}")

    def __getattr__(self, key: str) -> typing.Any:
        if key.startswith("color"):
            q = key[5:]
            if q.isdigit():
                k = int(q)
                if 0 <= k <= 255:
                    x = self.color_table[k]
                    return Color((x >> 16) & 255, (x >> 8) & 255, x & 255)
        raise AttributeError(key)

    def __setattr__(self, key: str, val: typing.Any) -> typing.Any:
        if key.startswith("color"):
            q = key[5:]
            if q.isdigit():
                k = int(q)
                if 0 <= k <= 255:
                    self.color_table[k] = int(val)
                    return
        object.__setattr__(self, key, val)


defaults = Options()
defaults.env = {}
defaults.font_features = {}
defaults.kitten_alias = {}
defaults.symbol_map = {}
defaults.watcher = {}
defaults.map = [
    # copy_to_clipboard
    KeyDefinition(False, KeyAction('copy_to_clipboard'), 1024, False, 99, ()),
    # paste_from_clipboard
    KeyDefinition(False, KeyAction('paste_from_clipboard'), 1024, False, 118, ()),
    # paste_from_selection
    KeyDefinition(False, KeyAction('paste_from_selection'), 1024, False, 115, ()),
    # paste_from_selection
    KeyDefinition(False, KeyAction('paste_from_selection'), 1, False, 57348, ()),
    # pass_selection_to_program
    KeyDefinition(False, KeyAction('pass_selection_to_program'), 1024, False, 111, ()),
    # scroll_line_up
    KeyDefinition(False, KeyAction('scroll_line_up'), 1024, False, 57352, ()),
    # scroll_line_up
    KeyDefinition(False, KeyAction('scroll_line_up'), 1024, False, 107, ()),
    # scroll_line_down
    KeyDefinition(False, KeyAction('scroll_line_down'), 1024, False, 57353, ()),
    # scroll_line_down
    KeyDefinition(False, KeyAction('scroll_line_down'), 1024, False, 106, ()),
    # scroll_page_up
    KeyDefinition(False, KeyAction('scroll_page_up'), 1024, False, 57354, ()),
    # scroll_page_down
    KeyDefinition(False, KeyAction('scroll_page_down'), 1024, False, 57355, ()),
    # scroll_home
    KeyDefinition(False, KeyAction('scroll_home'), 1024, False, 57356, ()),
    # scroll_end
    KeyDefinition(False, KeyAction('scroll_end'), 1024, False, 57357, ()),
    # scroll_to_previous_prompt
    KeyDefinition(False, KeyAction('scroll_to_prompt', (-1,)), 1024, False, 122, ()),
    # scroll_to_next_prompt
    KeyDefinition(False, KeyAction('scroll_to_prompt', (1,)), 1024, False, 120, ()),
    # show_scrollback
    KeyDefinition(False, KeyAction('show_scrollback'), 1024, False, 104, ()),
    # show_last_command_output
    KeyDefinition(False, KeyAction('show_last_command_output'), 1024, False, 103, ()),
    # new_window
    KeyDefinition(False, KeyAction('new_window'), 1024, False, 57345, ()),
    # new_os_window
    KeyDefinition(False, KeyAction('new_os_window'), 1024, False, 110, ()),
    # close_window
    KeyDefinition(False, KeyAction('close_window'), 1024, False, 119, ()),
    # next_window
    KeyDefinition(False, KeyAction('next_window'), 1024, False, 93, ()),
    # previous_window
    KeyDefinition(False, KeyAction('previous_window'), 1024, False, 91, ()),
    # move_window_forward
    KeyDefinition(False, KeyAction('move_window_forward'), 1024, False, 102, ()),
    # move_window_backward
    KeyDefinition(False, KeyAction('move_window_backward'), 1024, False, 98, ()),
    # move_window_to_top
    KeyDefinition(False, KeyAction('move_window_to_top'), 1024, False, 96, ()),
    # start_resizing_window
    KeyDefinition(False, KeyAction('start_resizing_window'), 1024, False, 114, ()),
    # first_window
    KeyDefinition(False, KeyAction('first_window'), 1024, False, 49, ()),
    # second_window
    KeyDefinition(False, KeyAction('second_window'), 1024, False, 50, ()),
    # third_window
    KeyDefinition(False, KeyAction('third_window'), 1024, False, 51, ()),
    # fourth_window
    KeyDefinition(False, KeyAction('fourth_window'), 1024, False, 52, ()),
    # fifth_window
    KeyDefinition(False, KeyAction('fifth_window'), 1024, False, 53, ()),
    # sixth_window
    KeyDefinition(False, KeyAction('sixth_window'), 1024, False, 54, ()),
    # seventh_window
    KeyDefinition(False, KeyAction('seventh_window'), 1024, False, 55, ()),
    # eighth_window
    KeyDefinition(False, KeyAction('eighth_window'), 1024, False, 56, ()),
    # ninth_window
    KeyDefinition(False, KeyAction('ninth_window'), 1024, False, 57, ()),
    # tenth_window
    KeyDefinition(False, KeyAction('tenth_window'), 1024, False, 48, ()),
    # focus_visible_window
    KeyDefinition(False, KeyAction('focus_visible_window'), 1024, False, 57370, ()),
    # swap_with_window
    KeyDefinition(False, KeyAction('swap_with_window'), 1024, False, 57371, ()),
    # next_tab
    KeyDefinition(False, KeyAction('next_tab'), 1024, False, 57351, ()),
    # next_tab
    KeyDefinition(False, KeyAction('next_tab'), 4, False, 57346, ()),
    # previous_tab
    KeyDefinition(False, KeyAction('previous_tab'), 1024, False, 57350, ()),
    # previous_tab
    KeyDefinition(False, KeyAction('previous_tab'), 5, False, 57346, ()),
    # new_tab
    KeyDefinition(False, KeyAction('new_tab'), 1024, False, 116, ()),
    # close_tab
    KeyDefinition(False, KeyAction('close_tab'), 1024, False, 113, ()),
    # move_tab_forward
    KeyDefinition(False, KeyAction('move_tab_forward'), 1024, False, 46, ()),
    # move_tab_backward
    KeyDefinition(False, KeyAction('move_tab_backward'), 1024, False, 44, ()),
    # set_tab_title
    KeyDefinition(False, KeyAction('set_tab_title'), 1026, False, 116, ()),
    # next_layout
    KeyDefinition(False, KeyAction('next_layout'), 1024, False, 108, ()),
    # increase_font_size
    KeyDefinition(False, KeyAction('change_font_size', (True, '+', 2.0)), 1024, False, 61, ()),
    # increase_font_size
    KeyDefinition(False, KeyAction('change_font_size', (True, '+', 2.0)), 1024, False, 43, ()),
    # increase_font_size
    KeyDefinition(False, KeyAction('change_font_size', (True, '+', 2.0)), 1024, False, 57413, ()),
    # decrease_font_size
    KeyDefinition(False, KeyAction('change_font_size', (True, '-', 2.0)), 1024, False, 45, ()),
    # decrease_font_size
    KeyDefinition(False, KeyAction('change_font_size', (True, '-', 2.0)), 1024, False, 57412, ()),
    # reset_font_size
    KeyDefinition(False, KeyAction('change_font_size', (True, None, 0.0)), 1024, False, 57347, ()),
    # open_url
    KeyDefinition(False, KeyAction('open_url_with_hints'), 1024, False, 101, ()),
    # insert_selected_path
    KeyDefinition(True, KeyAction('kitten', ('hints', '--type path --program -')), 1024, False, 112, (SingleKey(mods=0, is_native=False, key=102),)),
    # open_selected_path
    KeyDefinition(True, KeyAction('kitten', ('hints', '--type path')), 1024, False, 112, (SingleKey(mods=1, is_native=False, key=102),)),
    # insert_selected_line
    KeyDefinition(True, KeyAction('kitten', ('hints', '--type line --program -')), 1024, False, 112, (SingleKey(mods=0, is_native=False, key=108),)),
    # insert_selected_word
    KeyDefinition(True, KeyAction('kitten', ('hints', '--type word --program -')), 1024, False, 112, (SingleKey(mods=0, is_native=False, key=119),)),
    # insert_selected_hash
    KeyDefinition(True, KeyAction('kitten', ('hints', '--type hash --program -')), 1024, False, 112, (SingleKey(mods=0, is_native=False, key=104),)),
    # goto_file_line
    KeyDefinition(True, KeyAction('kitten', ('hints', '--type linenum')), 1024, False, 112, (SingleKey(mods=0, is_native=False, key=110),)),
    # open_selected_hyperlink
    KeyDefinition(True, KeyAction('kitten', ('hints', '--type hyperlink')), 1024, False, 112, (SingleKey(mods=0, is_native=False, key=121),)),
    # toggle_fullscreen
    KeyDefinition(False, KeyAction('toggle_fullscreen'), 1024, False, 57374, ()),
    # toggle_maximized
    KeyDefinition(False, KeyAction('toggle_maximized'), 1024, False, 57373, ()),
    # input_unicode_character
    KeyDefinition(False, KeyAction('kitten', ('unicode_input',)), 1024, False, 117, ()),
    # edit_config_file
    KeyDefinition(False, KeyAction('edit_config_file'), 1024, False, 57365, ()),
    # kitty_shell
    KeyDefinition(False, KeyAction('kitty_shell', ('window',)), 1024, False, 57344, ()),
    # increase_background_opacity
    KeyDefinition(True, KeyAction('set_background_opacity', ('+0.1',)), 1024, False, 97, (SingleKey(mods=0, is_native=False, key=109),)),
    # decrease_background_opacity
    KeyDefinition(True, KeyAction('set_background_opacity', ('-0.1',)), 1024, False, 97, (SingleKey(mods=0, is_native=False, key=108),)),
    # full_background_opacity
    KeyDefinition(True, KeyAction('set_background_opacity', ('1',)), 1024, False, 97, (SingleKey(mods=0, is_native=False, key=49),)),
    # reset_background_opacity
    KeyDefinition(True, KeyAction('set_background_opacity', ('default',)), 1024, False, 97, (SingleKey(mods=0, is_native=False, key=100),)),
    # reset_terminal
    KeyDefinition(False, KeyAction('clear_terminal', ('reset', True)), 1024, False, 57349, ()),
    # reload_config_file
    KeyDefinition(False, KeyAction('load_config_file'), 1024, False, 57368, ()),
    # debug_config
    KeyDefinition(False, KeyAction('debug_config'), 1024, False, 57369, ()),
]
if is_macos:
    defaults.map.append(KeyDefinition(False, KeyAction('copy_to_clipboard'), 8, False, 99, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('paste_from_clipboard'), 8, False, 118, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('scroll_line_up'), 10, False, 57354, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('scroll_line_up'), 8, False, 57352, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('scroll_line_down'), 10, False, 57355, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('scroll_line_down'), 8, False, 57353, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('scroll_page_up'), 8, False, 57354, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('scroll_page_down'), 8, False, 57355, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('scroll_home'), 8, False, 57356, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('scroll_end'), 8, False, 57357, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('new_window'), 8, False, 57345, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('new_os_window'), 8, False, 110, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('close_window'), 9, False, 100, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('start_resizing_window'), 8, False, 114, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('first_window'), 8, False, 49, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('second_window'), 8, False, 50, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('third_window'), 8, False, 51, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('fourth_window'), 8, False, 52, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('fifth_window'), 8, False, 53, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('sixth_window'), 8, False, 54, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('seventh_window'), 8, False, 55, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('eighth_window'), 8, False, 56, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('ninth_window'), 8, False, 57, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('next_tab'), 9, False, 93, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('previous_tab'), 9, False, 91, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('new_tab'), 8, False, 116, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('close_tab'), 8, False, 119, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('close_os_window'), 9, False, 119, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('set_tab_title'), 9, False, 105, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('change_font_size', (True, '+', 2.0)), 8, False, 43, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('change_font_size', (True, '+', 2.0)), 8, False, 61, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('change_font_size', (True, '+', 2.0)), 9, False, 61, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('change_font_size', (True, '-', 2.0)), 8, False, 45, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('change_font_size', (True, '-', 2.0)), 9, False, 45, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('change_font_size', (True, None, 0.0)), 8, False, 48, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('kitten', ('unicode_input',)), 12, False, 32, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('edit_config_file'), 8, False, 44, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('clear_terminal', ('reset', True)), 10, False, 114, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('load_config_file'), 12, False, 44, ()))
    defaults.map.append(KeyDefinition(False, KeyAction('debug_config'), 10, False, 44, ()))
defaults.mouse_map = [
    # click_url_or_select
    MouseMapping(0, 0, -2, False, KeyAction('mouse_handle_click', ('selection', 'link', 'prompt'))),
    # click_url_or_select_grabbed
    MouseMapping(0, 1, -2, True, KeyAction('mouse_handle_click', ('selection', 'link', 'prompt'))),
    # click_url_or_select_grabbed
    MouseMapping(0, 1, -2, False, KeyAction('mouse_handle_click', ('selection', 'link', 'prompt'))),
    # click_url
    MouseMapping(0, 5, -1, True, KeyAction('mouse_handle_click', ('link',))),
    # click_url
    MouseMapping(0, 5, -1, False, KeyAction('mouse_handle_click', ('link',))),
    # click_url_discard
    MouseMapping(0, 5, 1, True, KeyAction('discard_event')),
    # paste_selection
    MouseMapping(2, 0, -1, False, KeyAction('paste_from_selection')),
    # start_simple_selection
    MouseMapping(0, 0, 1, False, KeyAction('mouse_selection', (0,))),
    # start_rectangle_selection
    MouseMapping(0, 6, 1, False, KeyAction('mouse_selection', (2,))),
    # select_word
    MouseMapping(0, 0, 2, False, KeyAction('mouse_selection', (3,))),
    # select_line
    MouseMapping(0, 0, 3, False, KeyAction('mouse_selection', (4,))),
    # select_line_from_point
    MouseMapping(0, 6, 3, False, KeyAction('mouse_selection', (5,))),
    # extend_selection
    MouseMapping(1, 0, 1, False, KeyAction('mouse_selection', (1,))),
    # paste_selection_grabbed
    MouseMapping(2, 1, -1, True, KeyAction('paste_selection')),
    # paste_selection_grabbed
    MouseMapping(2, 1, -1, False, KeyAction('paste_selection')),
    # paste_selection_grabbed
    MouseMapping(2, 1, 1, True, KeyAction('discard_event')),
    # start_simple_selection_grabbed
    MouseMapping(0, 1, 1, True, KeyAction('mouse_selection', (0,))),
    # start_simple_selection_grabbed
    MouseMapping(0, 1, 1, False, KeyAction('mouse_selection', (0,))),
    # start_rectangle_selection_grabbed
    MouseMapping(0, 7, 1, True, KeyAction('mouse_selection', (2,))),
    # start_rectangle_selection_grabbed
    MouseMapping(0, 7, 1, False, KeyAction('mouse_selection', (2,))),
    # select_word_grabbed
    MouseMapping(0, 1, 2, True, KeyAction('mouse_selection', (3,))),
    # select_word_grabbed
    MouseMapping(0, 1, 2, False, KeyAction('mouse_selection', (3,))),
    # select_line_grabbed
    MouseMapping(0, 1, 3, True, KeyAction('mouse_selection', (4,))),
    # select_line_grabbed
    MouseMapping(0, 1, 3, False, KeyAction('mouse_selection', (4,))),
    # select_line_from_point_grabbed
    MouseMapping(0, 7, 3, True, KeyAction('mouse_selection', (5,))),
    # select_line_from_point_grabbed
    MouseMapping(0, 7, 3, False, KeyAction('mouse_selection', (5,))),
    # extend_selection_grabbed
    MouseMapping(1, 1, 1, True, KeyAction('mouse_selection', (1,))),
    # extend_selection_grabbed
    MouseMapping(1, 1, 1, False, KeyAction('mouse_selection', (1,))),
]
