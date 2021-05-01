from glob import glob

train_img_list = glob('/home/sonic/ai/yolomask/dataset/train/images/*.jpg')
val_img_list = glob('/home/sonic/ai/yolomask/dataset/valid/images/*.jpg') 

with open('/home/sonic/ai/yolomask/dataset/train.txt', 'w') as f:
  f.write('\n'.join(train_img_list) + '\n')

with open('/home/sonic/ai/yolomask/dataset/val.txt', 'w') as f:
  f.write('\n'.join(val_img_list) + '\n')