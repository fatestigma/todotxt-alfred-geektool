#!/usr/bin/python
#coding: utf-8
import os
import alfred

def results(arg, com):
    uid = 0
    tasks = os.popen('./todo.sh ls' + com + ' ' + arg).read().splitlines()
    for task in tasks:
        uid += 1
        task = task.rstrip()
        yield alfred.Item({'uid': alfred.uid(uid), 'arg': task}, task, 'Enter to display' + task, 'EBD226C2-1E22-4F65-BD43-556E6EF3C463.png')

(query, com) = alfred.args()
alfred.write(alfred.xml(results(query, com)))