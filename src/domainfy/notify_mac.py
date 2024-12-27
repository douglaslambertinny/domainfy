import subprocess

CMD = """
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
"""


def notify(title, text):
    try:
        subprocess.call(['osascript', '-e', CMD, title, text])
        return True
    except Exception as e:
        print('Error on notify: %s' % e)
        return False
