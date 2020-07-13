import TAADToolbox as tat

def main():
    word_vector = tat.DataManager.load("Glove")
    model = tat.DataManager.load("Victim.BiLSTM.SST")
    dataset = tat.DataManager.load("Dataset.SST.sample")[:10]

    clsf = tat.classifiers.PytorchClassifier(model, 
                word2id=word_vector.word2id, embedding=word_vector.get_vecmatrix(), 
                token_unk= "UNK", require_length=True, device="cpu")
    attacker = tat.attackers.GNLAEAttacker()
    attack_eval = tat.attack_evals.DefaultAttackEval(attacker, clsf)
    print( attack_eval.eval(dataset) )

if __name__ == "__main__":
    main()