from talon.voice import Context, Key


def python(app, win):
    print(("win.doc", win.doc))
    print(("win.title", win.title))
    return win.doc.endswith(".py")


ctx = Context("python", func=python)

ctx.keymap({"state any": ["any()", Key("left")]})


# TODO: defined function
# TODO: defined class
# TODO: python-ast
# TODO: don't overload tab for quinn snippet navigation
