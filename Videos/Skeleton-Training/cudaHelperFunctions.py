import matplotlib
import pickle
import numpy as np 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import torch
from torch import autograd

def getData():
	model = pickle.load(open('../datasets/trainData.npy', 'rb'))
	for i in range(len(model)):
		model[i] = model[i].type(torch.cuda.FloatTensor)
	return model

def getLabels():
	labels = np.load('../datasets/trainLabels.npy')
	return torch.from_numpy(labels).type(torch.cuda.LongTensor)


def getValData():
	model = pickle.load(open('../datasets/valData.npy', 'rb'))
	for i in range(len(model)):
		model[i] = model[i].type(torch.cuda.FloatTensor)
	return model

def getValLabels():
	labels = np.load('../datasets/valLabels.npy')
	return torch.from_numpy(labels).type(torch.cuda.LongTensor)



def checkAcc(model0,data,labels, start = 0, length = 500):
	if length == -1:
		l = labels.size()[0]
	else:
		l = length
		labels = labels[start:start + l]
	labelsdash = labels.view(l)
	out_labels = torch.zeros(l, 1).type(torch.cuda.FloatTensor)
	for i in range(start, start + l):
		model0.hidden = (model0.hidden[0].detach(), model0.hidden[1].detach())
		model0.zero_grad()
		
		temp = model0(data[i])
		# print(temp)
		# print(temp.size(), type(temp))
		if i%50 == 0 and l > 100:
			print("checking", i, "of", length)
		out_labels[i-start] = (temp.data.max(1)[1]).type(torch.cuda.FloatTensor)[0]
	return(torch.mean((labelsdash[:l].type(torch.cuda.LongTensor)==out_labels.type(torch.cuda.LongTensor)).type(torch.cuda.FloatTensor)))	



def PlotLoss(l,name = 'currentLoss.png'):
	plt.clf()
	plt.cla()
	plt.close()
	plt.plot(l)			
	plt.show()
	plt.savefig(name)

def PlotAccuracies(l1, l2, name="accuracies.png"):
	plt.clf()
	plt.cla()
	plt.close()
	plt.plot(l1)
	plt.plot(l2)
	plt.show()
	plt.savefig(name)
