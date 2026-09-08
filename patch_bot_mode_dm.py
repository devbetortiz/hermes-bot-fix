from pathlib import Path

path = Path("/opt/hermes/tools/bot_mode_dm.py")
text = path.read_text(encoding="utf-8")

def replace_once(old, new, label):
    global text
    if old not in text:
        raise SystemExit(f"Patch aborted: {label} was not found")
    text = text.replace(old, new, 1)

replace_once(
    "import shlex\nimport stat\n",
    "import shlex\nimport shutil\nimport stat\n",
    "import block",
)

default_home = '''def _default_home() -> str:
    return os.getenv("HERMES_HOME") or os.path.expanduser("~/.hermes")

'''

helper = default_home + '''def _hermes_cli() -> str:
    sibling = Path(sys.executable or "").parent / (
        "hermes.exe" if sys.platform == "win32" else "hermes"
    )
    return str(sibling) if sibling.is_file() else shutil.which("hermes") or "hermes"

'''

replace_once(default_home, helper, "_default_home block")

replace_once(
    '["hermes", "-p", _self_profile_name(root), "peer", "dm", dm_target]',
    '[_hermes_cli(), "-p", _self_profile_name(root), "peer", "dm", dm_target]',
    "peer CLI call",
)

replace_once(
    '["hermes", "-p", resolved, *BOT_CHAT_TURN_ARGS]',
    '[_hermes_cli(), "-p", resolved, *BOT_CHAT_TURN_ARGS]',
    "local CLI call",
)

path.write_text(text, encoding="utf-8")
