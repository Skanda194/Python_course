import os 

print(os.name)
# windows - nt    linux / Mac -  posix

cwd = os.getcwd()
# print(cwd)

ls = os.listdir('.')
# print(ls)

# mkdir  = os.mkdir('projects')
# os.rmdir('projects')
# os.rename('02.module.py','002.module.py')

print(os.path.getsize('004.Math.py'))

