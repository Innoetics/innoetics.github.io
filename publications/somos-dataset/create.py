import os
from os import listdir
from os.path import isfile, join
import re


os.system('type template.html > index.html')
out = open('index.html', 'a')


out.write('</body>\n')
out.write('</html>\n')
out.close()
