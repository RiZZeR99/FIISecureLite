from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

def plot_permissions():
    # size 1490 without classification column
    data_axis = [64,32,16,8]

    
    data_128_64={'loss': 0.5886040329933167, 'accuracy': 0.905636727809906, 'precision': 0.9332740306854248, 'recall': 0.8741666674613953, 'f1-score': 0.9027533779584969, 'f2-score': 0.8853813091485462}
    data_128_32={'loss': 0.8818657994270325, 'accuracy': 0.9081419706344604, 'precision': 0.8964401483535767, 'recall': 0.9233333468437195, 'f1-score': 0.9096875295360698, 'f2-score': 0.9178261861758711}    
    data_128_16={'loss': 0.3868510127067566, 'accuracy': 0.9010438323020935, 'precision': 0.8989229202270508, 'recall': 0.9041666388511658, 'f1-score': 0.901536654690797, 'f2-score': 0.9031128059925999}
    data_128_8={'loss': 0.6921842098236084, 'accuracy': 0.5031315088272095, 'precision': 0.5020920634269714, 'recall': 1.0, 'f1-score': 0.6685232435352128, 'f2-score': 0.8344920803989256}
        
    data_256_64={'loss': 0.7286839485168457, 'accuracy': 0.9052191972732544, 'precision': 0.9352890253067017, 'recall': 0.8770226240158081, 'f1-score': 0.9052186834256324, 'f2-score': 0.8880876059285224}
    data_256_32={'loss': 0.36113211512565613, 'accuracy': 0.9185803532600403, 'precision': 0.9370503425598145, 'recall': 0.8928877711296082, 'f1-score': 0.9144356613238336, 'f2-score': 0.9013839058485662}
    data_256_16={'loss': 0.4540802538394928, 'accuracy': 0.7870563864707947, 'precision': 0.9776315689086914, 'recall': 0.6011326909065247, 'f1-score': 0.7444885071793813, 'f2-score': 0.6512971944822548}
    data_256_8={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}

    data_512_64={'loss': 0.6915070414543152, 'accuracy': 0.4864300489425659, 'precision': 1.0, 'recall': 0.004854368977248669, 'f1-score': 0.009661826223189696, 'f2-score': 0.006060604603666832}
    data_512_32={'loss': 0.3910628855228424, 'accuracy': 0.8697286248207092, 'precision': 0.8725806474685669, 'recall': 0.8754045367240906, 'f1-score': 0.8739898110858724, 'f2-score': 0.8748380972211444}
    data_512_16={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_512_8={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}

    data_1024_64={'loss': 0.6931902766227722, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_32={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_16={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_8={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    

    fig, axes = plt.subplots(4)
    axes[0].plot(data_axis,[data_128_64['loss'],data_128_32['loss'], data_128_16['loss'],data_128_8['loss']],"black",label="loss")
    axes[0].plot(data_axis,[data_128_64['accuracy'],data_128_32['accuracy'], data_128_16['accuracy'],data_128_8['accuracy']],"red", label="accuracy")
    axes[0].plot(data_axis,[data_128_64['precision'],data_128_32['precision'], data_128_16['precision'],data_128_8['precision']],"green",label="precision")
    axes[0].plot(data_axis,[data_128_64['recall'],data_128_32['recall'], data_128_16['recall'],data_128_8['recall']],"purple", label="recall")
    axes[0].plot(data_axis,[data_128_64['f1-score'],data_128_32['f1-score'], data_128_16['f1-score'],data_128_8['f1-score']],"blue", label="F1-Score")
    axes[0].plot(data_axis,[data_128_64['f2-score'],data_128_32['f2-score'], data_128_16['f2-score'],data_128_8['f2-score']],"pink", label="F2-Score")
    axes[0].legend(loc='right')
    axes[0].title.set_text("128 first layer")
    axes[1].plot(data_axis,[data_256_64['loss'],data_256_32['loss'], data_256_16['loss'],data_256_8['loss']],"black",label="loss")
    axes[1].plot(data_axis,[data_256_64['accuracy'],data_256_32['accuracy'], data_256_16['accuracy'],data_256_8['accuracy']],"red", label="accuracy")
    axes[1].plot(data_axis,[data_256_64['precision'],data_256_32['precision'], data_256_16['precision'],data_256_8['precision']],"green",label="precision")
    axes[1].plot(data_axis,[data_256_64['recall'],data_256_32['recall'], data_256_16['recall'],data_256_8['recall']],"purple", label="recall")
    axes[1].plot(data_axis,[data_256_64['f1-score'],data_256_32['f1-score'], data_256_16['f1-score'],data_256_8['f1-score']],"blue", label="F1-Score")
    axes[1].plot(data_axis,[data_256_64['f2-score'],data_256_32['f2-score'], data_256_16['f2-score'],data_256_8['f2-score']],"pink", label="F2-Score")
    axes[1].legend(loc='right')
    axes[1].title.set_text("256 first layer")
    axes[2].plot(data_axis,[data_512_64['loss'],data_512_32['loss'], data_512_16['loss'],data_512_8['loss']],"black",label="loss")
    axes[2].plot(data_axis,[data_512_64['accuracy'],data_512_32['accuracy'], data_512_16['accuracy'],data_512_8['accuracy']],"red", label="accuracy")
    axes[2].plot(data_axis,[data_512_64['precision'],data_512_32['precision'], data_512_16['precision'],data_512_8['precision']],"green",label="precision")
    axes[2].plot(data_axis,[data_512_64['recall'],data_512_32['recall'], data_512_16['recall'],data_512_8['recall']],"purple", label="recall")
    axes[2].plot(data_axis,[data_512_64['f1-score'],data_512_32['f1-score'], data_512_16['f1-score'],data_512_8['f1-score']],"blue",label="F1-Score")
    axes[2].plot(data_axis,[data_512_64['f2-score'],data_512_32['f2-score'], data_512_16['f2-score'],data_512_8['f2-score']],"pink",label="F2-Score")
    axes[2].legend(loc='right')
    axes[2].title.set_text("512 first layer")
    axes[3].plot(data_axis,[data_1024_64['loss'],data_1024_32['loss'], data_1024_16['loss'],data_1024_8['loss']],"black",label="loss")
    axes[3].plot(data_axis,[data_1024_64['accuracy'],data_1024_32['accuracy'], data_1024_16['accuracy'],data_1024_8['accuracy']],"red", label="accuracy")
    axes[3].plot(data_axis,[data_1024_64['precision'],data_1024_32['precision'], data_1024_16['precision'],data_1024_8['precision']],"green",label="precision")
    axes[3].plot(data_axis,[data_1024_64['recall'],data_1024_32['recall'], data_1024_16['recall'],data_1024_8['recall']],"purple", label="recall")
    axes[3].plot(data_axis,[data_1024_64['f1-score'],data_1024_32['f1-score'], data_1024_16['f1-score'],data_1024_8['f1-score']],"blue",label="F1-Score")
    axes[3].plot(data_axis,[data_1024_64['f2-score'],data_1024_32['f2-score'], data_1024_16['f2-score'],data_1024_8['f2-score']],"pink",label="F2-Score")
    axes[3].legend(loc='right')
    axes[3].title.set_text("1024 first layer")
    
    plt.show()
    
    pass


def plot_receivers():
    # size 593 without classification column
    data_axis = [64,32,16,8]
    
    data_128_64={'loss': 0.9671230912208557, 'accuracy': 0.7703549265861511, 'precision': 0.950138509273529, 'recall': 0.5716666579246521, 'f1-score': 0.7138392758151764, 'f2-score': 0.6211516067228812}
    data_128_32={'loss': 0.8340794444084167, 'accuracy': 0.7766179442405701, 'precision': 0.9487179517745972, 'recall': 0.5858333110809326, 'f1-score': 0.724368393860767, 'f2-score': 0.634361863106474}
    data_128_16={'loss': 0.6932637095451355, 'accuracy': 0.4989561438560486, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_128_8={'loss': 0.49447116255760193, 'accuracy': 0.7912317514419556, 'precision': 0.73209547996521, 'recall': 0.9200000166893005, 'f1-score': 0.8153613970491992, 'f2-score': 0.8750790460446416}
    
    data_256_64={'loss': 0.7005413174629211, 'accuracy': 0.7720250487327576, 'precision': 0.9541666507720947, 'recall': 0.5724999904632568, 'f1-score': 0.7156245193293781, 'f2-score': 0.6222824565527216}
    data_256_32={'loss': 0.6551796197891235, 'accuracy': 0.7724425792694092, 'precision': 0.9303547739982605, 'recall': 0.5899999737739563, 'f1-score': 0.7220800698307192, 'f2-score': 0.6365759812046259}
    data_256_16={'loss': 0.6932637095451355, 'accuracy': 0.4989561438560486, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_256_8={'loss': 0.4864990711212158, 'accuracy': 0.7803757786750793, 'precision': 0.7064951062202454, 'recall': 0.9608333110809326, 'f1-score': 0.8142650458010293, 'f2-score': 0.8962995016966956}
    
    data_512_64={'loss': 0.5068426132202148, 'accuracy': 0.7586638927459717, 'precision': 0.682941198348999, 'recall': 0.9674999713897705, 'f1-score': 0.8006891752749318, 'f2-score': 0.8930766696371942}
    data_512_32={'loss': 0.6891919374465942, 'accuracy': 0.5048016905784607, 'precision': 1.0, 'recall': 0.011666666716337204, 'f1-score': 0.023064227710676528, 'f2-score': 0.014540918746999172}
    data_512_16={'loss': 0.47794845700263977, 'accuracy': 0.7711899876594543, 'precision': 0.975218653678894, 'recall': 0.5575000047683716, 'f1-score': 0.7094375035640534, 'f2-score': 0.6097337354216906}
    data_512_8={'loss': 0.6747533082962036, 'accuracy': 0.5294363498687744, 'precision': 0.5156989097595215, 'recall': 0.9991666674613953, 'f1-score': 0.6802832260292887, 'f2-score': 0.8414032264595709}
    
    data_1024_64={'loss': 0.6910821795463562, 'accuracy': 0.5022964477539062, 'precision': 1.0, 'recall': 0.006666666828095913, 'f1-score': 0.013245020273874258, 'f2-score': 0.008319465678786409}
    data_1024_32={'loss': 0.693263590335846, 'accuracy': 0.4989561438560486, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_16={'loss': 0.693263590335846, 'accuracy': 0.4989561438560486, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_8={'loss': 0.6901801824569702, 'accuracy': 0.4989561438560486, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}

    

    fig, axes = plt.subplots(4)
    axes[0].plot(data_axis,[data_128_64['loss'],data_128_32['loss'], data_128_16['loss'],data_128_8['loss']],"black",label="loss")
    axes[0].plot(data_axis,[data_128_64['accuracy'],data_128_32['accuracy'], data_128_16['accuracy'],data_128_8['accuracy']],"red", label="accuracy")
    axes[0].plot(data_axis,[data_128_64['precision'],data_128_32['precision'], data_128_16['precision'],data_128_8['precision']],"green",label="precision")
    axes[0].plot(data_axis,[data_128_64['recall'],data_128_32['recall'], data_128_16['recall'],data_128_8['recall']],"purple", label="recall")
    axes[0].plot(data_axis,[data_128_64['f1-score'],data_128_32['f1-score'], data_128_16['f1-score'],data_128_8['f1-score']],"blue", label="F1-Score")
    axes[0].plot(data_axis,[data_128_64['f2-score'],data_128_32['f2-score'], data_128_16['f2-score'],data_128_8['f2-score']],"pink", label="F2-Score")
    axes[0].legend(loc='right')
    axes[0].title.set_text("128 first layer")
    axes[1].plot(data_axis,[data_256_64['loss'],data_256_32['loss'], data_256_16['loss'],data_256_8['loss']],"black",label="loss")
    axes[1].plot(data_axis,[data_256_64['accuracy'],data_256_32['accuracy'], data_256_16['accuracy'],data_256_8['accuracy']],"red", label="accuracy")
    axes[1].plot(data_axis,[data_256_64['precision'],data_256_32['precision'], data_256_16['precision'],data_256_8['precision']],"green",label="precision")
    axes[1].plot(data_axis,[data_256_64['recall'],data_256_32['recall'], data_256_16['recall'],data_256_8['recall']],"purple", label="recall")
    axes[1].plot(data_axis,[data_256_64['f1-score'],data_256_32['f1-score'], data_256_16['f1-score'],data_256_8['f1-score']],"blue", label="F1-Score")
    axes[1].plot(data_axis,[data_256_64['f2-score'],data_256_32['f2-score'], data_256_16['f2-score'],data_256_8['f2-score']],"pink", label="F2-Score")
    axes[1].legend(loc='right')
    axes[1].title.set_text("256 first layer")
    axes[2].plot(data_axis,[data_512_64['loss'],data_512_32['loss'], data_512_16['loss'],data_512_8['loss']],"black",label="loss")
    axes[2].plot(data_axis,[data_512_64['accuracy'],data_512_32['accuracy'], data_512_16['accuracy'],data_512_8['accuracy']],"red", label="accuracy")
    axes[2].plot(data_axis,[data_512_64['precision'],data_512_32['precision'], data_512_16['precision'],data_512_8['precision']],"green",label="precision")
    axes[2].plot(data_axis,[data_512_64['recall'],data_512_32['recall'], data_512_16['recall'],data_512_8['recall']],"purple", label="recall")
    axes[2].plot(data_axis,[data_512_64['f1-score'],data_512_32['f1-score'], data_512_16['f1-score'],data_512_8['f1-score']],"blue",label="F1-Score")
    axes[2].plot(data_axis,[data_512_64['f2-score'],data_512_32['f2-score'], data_512_16['f2-score'],data_512_8['f2-score']],"pink",label="F2-Score")
    axes[2].legend(loc='right')
    axes[2].title.set_text("512 first layer")
    axes[3].plot(data_axis,[data_1024_64['loss'],data_1024_32['loss'], data_1024_16['loss'],data_1024_8['loss']],"black",label="loss")
    axes[3].plot(data_axis,[data_1024_64['accuracy'],data_1024_32['accuracy'], data_1024_16['accuracy'],data_1024_8['accuracy']],"red", label="accuracy")
    axes[3].plot(data_axis,[data_1024_64['precision'],data_1024_32['precision'], data_1024_16['precision'],data_1024_8['precision']],"green",label="precision")
    axes[3].plot(data_axis,[data_1024_64['recall'],data_1024_32['recall'], data_1024_16['recall'],data_1024_8['recall']],"purple", label="recall")
    axes[3].plot(data_axis,[data_1024_64['f1-score'],data_1024_32['f1-score'], data_1024_16['f1-score'],data_1024_8['f1-score']],"blue",label="F1-Score")
    axes[3].plot(data_axis,[data_1024_64['f2-score'],data_1024_32['f2-score'], data_1024_16['f2-score'],data_1024_8['f2-score']],"pink",label="F2-Score")
    axes[3].legend(loc='right')
    axes[3].title.set_text("1024 first layer")
    
    plt.show()
    
    


def plot_services():
    # size 855 without classification column
    data_axis = [64,32,16,8]

    data_128_64={'loss': 0.5770996809005737, 'accuracy': 0.8221294283866882, 'precision': 0.9640287756919861, 'recall': 0.6700000166893005, 'f1-score': 0.7905599993514459, 'f2-score': 0.7135248839793912}
    data_128_32={'loss': 0.5463465433849343, 'accuracy': 0.818371593952179, 'precision': 0.9526627063751221, 'recall': 0.6708333492279053, 'f1-score': 0.7872855842843106, 'f2-score': 0.7130202255336879}
    data_128_16={'loss': 0.45649394392967224, 'accuracy': 0.8167014718055725, 'precision': 0.9556885957717896, 'recall': 0.6650000214576721, 'f1-score': 0.7842747061976298, 'f2-score': 0.7080743928818815}
    data_128_8={'loss': 0.4330432415008545, 'accuracy': 0.8004175424575806, 'precision': 0.9878378510475159, 'recall': 0.60916668176651, 'f1-score': 0.7536077909331214, 'f2-score': 0.659747163101452}

    data_256_64={'loss': 1.0310988426208496, 'accuracy': 0.8141962289810181, 'precision': 0.9689440727233887, 'recall': 0.6499999761581421, 'f1-score': 0.7780543565748457, 'f2-score': 0.6958071365485754}
    data_256_32={'loss': 0.36646485328674316, 'accuracy': 0.8208768367767334, 'precision': 0.9605734944343567, 'recall': 0.6700000166893005, 'f1-score': 0.7893957042892982, 'f2-score': 0.713145149084035}
    data_256_16={'loss': 0.489030122756958, 'accuracy': 0.7803757786750793, 'precision': 0.7077682018280029, 'recall': 0.9566666483879089, 'f1-score': 0.8136068847477648, 'f2-score': 0.8938023095793327}
    data_256_8={'loss': 0.4649724066257477, 'accuracy': 0.7887265086174011, 'precision': 0.9614361524581909, 'recall': 0.6025000214576721, 'f1-score': 0.740778225810502, 'f2-score': 0.6511165867409585}

    data_512_64={'loss': 0.4948427677154541, 'accuracy': 0.7711899876594543, 'precision': 0.6959134340286255, 'recall': 0.9649999737739563, 'f1-score': 0.8086587032200512, 'f2-score': 0.8957299318807489}
    data_512_32={'loss': 0.6227512359619141, 'accuracy': 0.7035490870475769, 'precision': 0.9939516186714172, 'recall': 0.41083332896232605, 'f1-score': 0.5813675072904925, 'f2-score': 0.4654455089948124}
    data_512_16={'loss': 0.5471311807632446, 'accuracy': 0.7198329567909241, 'precision': 0.6476828455924988, 'recall': 0.9666666388511658, 'f1-score': 0.7756598154163814, 'f2-score': 0.8799875915740513}
    data_512_8={'loss': 0.4827224314212799, 'accuracy': 0.7732776403427124, 'precision': 0.9594405889511108, 'recall': 0.5716666579246521, 'f1-score': 0.7164486195957982, 'f2-score': 0.6219400163458845}

    data_1024_64={'loss': 0.693263590335846, 'accuracy': 0.4989561438560486, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_32={'loss': 0.693263590335846, 'accuracy': 0.4989561438560486, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_16={'loss': 0.693263590335846, 'accuracy': 0.4989561438560486, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_8={'loss': 0.4537144601345062, 'accuracy': 0.8100208640098572, 'precision': 0.9356725215911865, 'recall': 0.6666666865348816, 'f1-score': 0.7785883378417429, 'f2-score': 0.7073384966454311}

    



    fig, axes = plt.subplots(4)
    axes[0].plot(data_axis,[data_128_64['loss'],data_128_32['loss'], data_128_16['loss'],data_128_8['loss']],"black",label="loss")
    axes[0].plot(data_axis,[data_128_64['accuracy'],data_128_32['accuracy'], data_128_16['accuracy'],data_128_8['accuracy']],"red", label="accuracy")
    axes[0].plot(data_axis,[data_128_64['precision'],data_128_32['precision'], data_128_16['precision'],data_128_8['precision']],"green",label="precision")
    axes[0].plot(data_axis,[data_128_64['recall'],data_128_32['recall'], data_128_16['recall'],data_128_8['recall']],"purple", label="recall")
    axes[0].plot(data_axis,[data_128_64['f1-score'],data_128_32['f1-score'], data_128_16['f1-score'],data_128_8['f1-score']],"blue", label="F1-Score")
    axes[0].plot(data_axis,[data_128_64['f2-score'],data_128_32['f2-score'], data_128_16['f2-score'],data_128_8['f2-score']],"pink", label="F2-Score")    
    axes[0].legend(loc='right')
    axes[0].title.set_text("128 first layer")
    axes[1].plot(data_axis,[data_256_64['loss'],data_256_32['loss'], data_256_16['loss'],data_256_8['loss']],"black",label="loss")
    axes[1].plot(data_axis,[data_256_64['accuracy'],data_256_32['accuracy'], data_256_16['accuracy'],data_256_8['accuracy']],"red", label="accuracy")
    axes[1].plot(data_axis,[data_256_64['precision'],data_256_32['precision'], data_256_16['precision'],data_256_8['precision']],"green",label="precision")
    axes[1].plot(data_axis,[data_256_64['recall'],data_256_32['recall'], data_256_16['recall'],data_256_8['recall']],"purple", label="recall")
    axes[1].plot(data_axis,[data_256_64['f1-score'],data_256_32['f1-score'], data_256_16['f1-score'],data_256_8['f1-score']],"blue", label="F1-Score")
    axes[1].plot(data_axis,[data_256_64['f2-score'],data_256_32['f2-score'], data_256_16['f2-score'],data_256_8['f2-score']],"pink", label="F2-Score")
    axes[1].legend(loc='right')
    axes[1].title.set_text("256 first layer")
    axes[2].plot(data_axis,[data_512_64['loss'],data_512_32['loss'], data_512_16['loss'],data_512_8['loss']],"black",label="loss")
    axes[2].plot(data_axis,[data_512_64['accuracy'],data_512_32['accuracy'], data_512_16['accuracy'],data_512_8['accuracy']],"red", label="accuracy")
    axes[2].plot(data_axis,[data_512_64['precision'],data_512_32['precision'], data_512_16['precision'],data_512_8['precision']],"green",label="precision")
    axes[2].plot(data_axis,[data_512_64['recall'],data_512_32['recall'], data_512_16['recall'],data_512_8['recall']],"purple", label="recall")
    axes[2].plot(data_axis,[data_512_64['f1-score'],data_512_32['f1-score'], data_512_16['f1-score'],data_512_8['f1-score']],"blue",label="F1-Score")
    axes[2].plot(data_axis,[data_512_64['f2-score'],data_512_32['f2-score'], data_512_16['f2-score'],data_512_8['f2-score']],"pink",label="F2-Score")
    axes[2].legend(loc='right')
    axes[2].title.set_text("512 first layer")
    axes[3].plot(data_axis,[data_1024_64['loss'],data_1024_32['loss'], data_1024_16['loss'],data_1024_8['loss']],"black",label="loss")
    axes[3].plot(data_axis,[data_1024_64['accuracy'],data_1024_32['accuracy'], data_1024_16['accuracy'],data_1024_8['accuracy']],"red", label="accuracy")
    axes[3].plot(data_axis,[data_1024_64['precision'],data_1024_32['precision'], data_1024_16['precision'],data_1024_8['precision']],"green",label="precision")
    axes[3].plot(data_axis,[data_1024_64['recall'],data_1024_32['recall'], data_1024_16['recall'],data_1024_8['recall']],"purple", label="recall")
    axes[3].plot(data_axis,[data_1024_64['f1-score'],data_1024_32['f1-score'], data_1024_16['f1-score'],data_1024_8['f1-score']],"blue",label="F1-Score")
    axes[3].plot(data_axis,[data_1024_64['f2-score'],data_1024_32['f2-score'], data_1024_16['f2-score'],data_1024_8['f2-score']],"pink",label="F2-Score")
    axes[3].legend(loc='right')
    axes[3].title.set_text("1024 first layer")
    
    plt.show()
    
    pass


# plot_permissions()
# plot_receivers()
plot_services()
