# not allowed to create account with these as username
DISALLOWED_USERNAMES = [
    "about",
    "abuse",
    "account",
    "accounts",
    "admin",
    "administration",
    "administrator",
    "api",
    "auth",
    "authentication",
    "billing",
    "blog",
    "blogs",
    "cdn",
    "collection",
    "config",
    "contact",
    "dash",
    "dashboard",
    "developer",
    "developers",
    "docs",
    "documentation",
    "help",
    "helpcenter",
    "home",
    "image",
    "images",
    "img",
    "index",
    "irc",
    "knowledgebase",
    "legal",
    "login",
    "logout",
    "man",
    "manual",
    "meta",
    "metrics",
    "on",
    "ops",
    "pricing",
    "privacy",
    "profile",
    "random",
    "register",
    "registration",
    "search",
    "settings",
    "setup",
    "signin",
    "signup",
    "smtp",
    "static",
    "status",
    "support",
    "terms",
    "test",
    "tests",
    "tmp",
    "up",
    "uptime",
    "wiki",
    "www",
]

# not allowed to create a blog page with these as slugs
DISALLOWED_PAGE_SLUGS = [
    "analytics",
    "billing",
    "blog",
    "dashboard",
    "export",
    "halsey",
    "images",
    "import",
    "newsletter",
    "notifications",
    "pages",
    "rss",
    "webring",
]

# elements allowed to exist inside the HTML of a markdown text
ALLOWED_HTML_ELEMENTS = [
    "a",
    "abbr",
    "acronym",
    "article",
    "audio",
    "b",
    "bdi",
    "bdo",
    "br",
    "blockquote",
    "cite",
    "colgroup",
    "code",
    "del",
    "div",
    "dfn",
    "em",
    "figcaption",
    "figure",
    "kbd",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "i",
    "iframe",
    "img",
    "li",
    "mark",
    "ol",
    "p",
    "pre",
    "q",
    "rb",
    "rt",
    "rtc",
    "ruby",
    "s",
    "samp",
    "section",
    "small",
    "span",
    "strong",
    "sub",
    "sup",
    "table",
    "tbody",
    "td",
    "th",
    "thead",
    "time",
    "tr",
    "u",
    "ul",
    "var",
    "wbr",
]

# attributes allowed to exist inside the elements of the HTML of a markdown text
ALLOWED_HTML_ATTRS = [
    "align",
    "allowfullscreen",
    "alt",
    "class",
    "controls",
    "frameborder",
    "height",
    "href",
    "id",
    "name",
    "preload",
    "rel",
    "seamless",
    "span",
    "src",
    "start",
    "style",
    "title",
    "width",
]

# css rules allowed to exist as inline styles on HTML elements of a markdown text
ALLOWED_CSS_STYLES = [
    "background",
    "border",
    "border-radius",
    "box-shadow",
    "color",
    "display",
    "font-family",
    "font-size",
    "height",
    "margin",
    "padding",
    "width",
]

# control characters of unicode category Cc except for \t, \n, \r
DISALLOWED_CHARACTERS = [
    "\x00",
    "\x01",
    "\x02",
    "\x03",
    "\x04",
    "\x05",
    "\x06",
    "\x07",
    "\x08",
    "\x0b",
    "\x0c",
    "\x0e",
    "\x0f",
    "\x10",
    "\x11",
    "\x12",
    "\x13",
    "\x14",
    "\x15",
    "\x16",
    "\x17",
    "\x18",
    "\x19",
    "\x1a",
    "\x1b",
    "\x1c",
    "\x1d",
    "\x1e",
    "\x1f",
    "\x7f",
    "\x80",
    "\x81",
    "\x82",
    "\x83",
    "\x84",
    "\x85",
    "\x86",
    "\x87",
    "\x88",
    "\x89",
    "\x8a",
    "\x8b",
    "\x8c",
    "\x8d",
    "\x8e",
    "\x8f",
    "\x90",
    "\x91",
    "\x92",
    "\x93",
    "\x94",
    "\x95",
    "\x96",
    "\x97",
    "\x98",
    "\x99",
    "\x9a",
    "\x9b",
    "\x9c",
    "\x9d",
    "\x9e",
    "\x9f",
]
