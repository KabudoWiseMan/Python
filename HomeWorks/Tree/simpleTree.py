import os
 
def print_dir(path, prefix=u''):
        print(u'{}├── {}'.format(prefix, os.path.basename(path)))
 
        for item in os.listdir(path):
                p = os.path.join(path, item)
                if os.path.isdir(p):
                        print_dir(p, prefix + u'│  ')
                else:
                        print(u'{}│  ├── {}'.format(prefix, item))

print_dir('.')
