#!env python
# coding: utf-8
import os
import sys

from pyinotify import ProcessEvent, WatchManager, Notifier, IN_MODIFY


class AutoRunner(ProcessEvent):
    def __init__(self, watch_path, callback):
        super(AutoRunner, self).__init__()
        self.watch_path = watch_path
        self.callback = callback

    def process_IN_MODIFY(self, event):
        if event.pathname.startswith(self.watch_path):
            self.callback()


def monitor(watch_path, callback):
    watch_path = os.path.abspath(watch_path)
    if os.path.isfile(watch_path):
        path_for_manager = os.path.dirname(watch_path)
    else:
        path_for_manager = watch_path

    manager = WatchManager()
    notifier = Notifier(manager,
                        AutoRunner(watch_path, callback))
    manager.add_watch(path_for_manager, IN_MODIFY)

    notifier.loop()


def build_command_callback(command):
    def callback():
        os.system(command)

    return callback


def main():
    if len(sys.argv) != 3:
        print 'Syntax:'
        print 'ponytor PATH_TO_WATCH COMMAND_TO_RUN'
        print 'Example:'
        print 'ponytor working_on_this.py "echo `date` && python working_on_this.py"'
        sys.exit(1)
    else:
        print '(running, stop with Ctrl-C)'
        monitor(sys.argv[1],
                build_command_callback(sys.argv[2]))


if __name__ == '__main__':
    main()
