#!/usr/bin/python
#coding: utf-8
import alfred

def results(arg, com):
    uid = 0
    # read todo.txt
    path = alfred.work(False) + '/todo.txt'
    file = open(path)
    tasks = file.read().splitlines()
    file.close()

    for task in tasks:
        uid += 1
        # filter with keyword
        if arg in task:
            yield alfred.Item({'uid': alfred.uid(uid), 'arg': com + str(uid)}, task, 'Enter to display' + task, 'EBD226C2-1E22-4F65-BD43-556E6EF3C463.png')

def prioritize(id, com):
    # read todo.txt
    path = alfred.work(False) + '/todo.txt'
    file = open(path)
    tasks = file.readlines()
    file.close()
    
    pos = int(id) - 1
    task = tasks[pos]
    
    if com == 'p':      # prioritize
        if task[0] == '(' and task[2] == ')':
            if task[1] != 'A':
                tasks[pos] = '(' + chr(ord(task[1])-1) + task[2:]
        else:
            tasks[pos] = '(A) ' + task
    else:               # deprioritize
        if task[0] == '(' and task[2] == ')':
            if task[1] == 'C':
                tasks[pos] = task[4:]
            else:
                tasks[pos] = '(' + chr(ord(task[1])+1) + task[2:]
    
    file = open(path, 'w')
    file.writelines(tasks)
    file.close()

(query, com) = alfred.args()

if com!='e':    # command is p(rioritize) or d(eprioritize) | query is id
    alfred.write(alfred.xml(results(query, com)))
else:           # command is e(xecute)                      | query is com + id
    com = query[0]
    query = query[1:]
    prioritize(query, com)