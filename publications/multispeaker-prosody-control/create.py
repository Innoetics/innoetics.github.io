import os
from os import listdir
from os.path import isfile, join
import re


os.system('cat template.html > index.html')
out = open('index.html', 'a')

# End
out.write('</body>\n')
out.write('</html>\n')
out.close()
