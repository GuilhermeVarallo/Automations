import os

directory = r'caminho_do_arquivo'

for filename in os.listdir(directory):
    new_filename = 'prefix___' + filename
    os.rename(os.path.join(directory, filename), os.path.join(directory,new_filename))
