import yaml

with open('/home/sonic/ai/yolomask/dataset/data.yaml', 'r') as f:
  data = yaml.load(f)

print(data)

data['train'] = '/home/sonic/ai/yolomask/dataset/train.txt'
data['val'] = '/home/sonic/ai/yolomask/dataset/val.txt'

with open('/home/sonic/ai/yolomask/dataset/data.yaml', 'w') as f:
  yaml.dump(data, f)

print(data)