import _thread

from sslserver.keyserver1 import main_run as run_one
from sslserver.keyserver2 import main_run as run_two
from sslserver.keyserver3 import main_run as run_three
from sslserver.keyserver4 import main_run as run_four
from sslserver.keyserver5 import main_run as run_five

try:
    _thread.start_new_thread(run_one, ())
    _thread.start_new_thread(run_two, ())
    _thread.start_new_thread(run_three, ())
    _thread.start_new_thread(run_four, ())
    _thread.start_new_thread(run_five, ())
except Exception as e:
    print(e)

while True:
   pass
