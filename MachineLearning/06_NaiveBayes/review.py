import pickle

pos_list = pickle.load(open("posList.p", "rb"))
neg_list = pickle.load(open("negList.p", "rb"))
pos_counter = pickle.load(open("pos_counter.p", "rb"))
neg_counter = pickle.load(open("neg_counter.p", "rb"))
