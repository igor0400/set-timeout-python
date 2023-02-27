import threading
import time

stack = []
work_thread = True
stack_item_id = 0

def update_stack():
    global stack
    global work_thread
    global stack_item_id

    while work_thread:
        for i, item in enumerate(stack):
            if item['timeout'] <= round(time.time()):
                stack[i]['callback']()
                stack = list(filter(lambda x: x['id'] != item['id'], stack))

        if len(stack) == 0:
            work_thread = False

stack_thread = threading.Thread(target=update_stack)

def set_timeout(callback, timeout: int):
    global stack_item_id
    global stack_thread
    global work_thread

    if timeout < 0.004: timeout = 0.004

    stack.append({"id": stack_item_id, "callback": callback, "timeout": round(time.time()) + timeout})
    stack_item_id += 1
    
    if not stack_thread.is_alive():
        stack_thread = threading.Thread(target=update_stack)
        work_thread = True
        stack_thread.start()