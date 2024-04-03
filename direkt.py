import os
import zipfile
    	
fantasy_zip = zipfile.ZipFile('C:/Users/tanze/Downloads/main.zip')
fantasy_zip.extractall('C:/Users/tanze/Downloads')
fantasy_zip.close()

os.chdir('C:/Users/tanze/Downloads')

with open('result.txt', 'a') as f:
    for current_dir, dirs, files in os.walk('main'):
        if list(filter(lambda x: x.endswith('.py'), files)):
            f.write('{}\n'.format(current_dir))