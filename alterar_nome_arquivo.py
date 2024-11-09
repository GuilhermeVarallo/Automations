import os

directory = r'C:\Users\gvara\Documents\Estudos\Automacoes'

for filename in os.listdir(directory):
    new_filename = '08/11/2024' + filename
    os.rename(os.path.join(directory, filename), os.path.join(directory,new_filename))