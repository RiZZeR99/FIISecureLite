from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

def plot_permissions():
    # size 1490 without classification column
    data_axis = [64,32,16,8]
        
    data_256_64={'loss': 0.7286839485168457, 'accuracy': 0.9052191972732544, 'precision': 0.9352890253067017, 'recall': 0.8770226240158081, 'f1-score': 0.9052186834256324, 'f2-score': 0.8880876059285224}
    data_256_32={'loss': 0.41002440452575684, 'accuracy': 0.8392484188079834, 'precision': 0.9493136405944824, 'recall': 0.7273463010787964, 'f1-score': 0.8236367268876149, 'f2-score': 0.7630282021350347}
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
    axes[0].plot(data_axis,[data_128_64['loss'],data_256_32['loss'], data_256_16['loss'],data_256_8['loss']],"black",label="loss")
    axes[0].plot(data_axis,[data_128_64['accuracy'],data_256_32['accuracy'], data_256_16['accuracy'],data_256_8['accuracy']],"red", label="accuracy")
    axes[0].plot(data_axis,[data_128_64['precision'],data_256_32['precision'], data_256_16['precision'],data_256_8['precision']],"green",label="precision")
    axes[0].plot(data_axis,[data_128_64['recall'],data_256_32['recall'], data_256_16['recall'],data_256_8['recall']],"purple", label="recall")
    axes[0].plot(data_axis,[data_128_64['f1-score'],data_256_32['f1-score'], data_256_16['f1-score'],data_256_8['f1-score']],"blue", label="F1-Score")
    axes[0].plot(data_axis,[data_128_64['f2-score'],data_256_32['f2-score'], data_256_16['f2-score'],data_256_8['f2-score']],"pink", label="F2-Score")
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
            
    data_256_64={'loss': 2.1354994773864746, 'accuracy': 0.7457202672958374, 'precision': 0.9630723595619202, 'recall': 0.5275080800056458, 'f1-score': 0.6816513849070871, 'f2-score': 0.57996783320254}
    data_256_32={'loss': 1.0637532472610474, 'accuracy': 0.7674321532249451, 'precision': 0.9484808444976807, 'recall': 0.5809061527252197, 'f1-score': 0.7205213579695864, 'f2-score': 0.6297139448514217}
    data_256_16={'loss': 0.6715701818466187, 'accuracy': 0.5194154381752014, 'precision': 0.9775280952453613, 'recall': 0.07038834691047668, 'f1-score': 0.13132062491738852, 'f2-score': 0.08642954002598566}
    data_256_8={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_512_64={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_512_32={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_512_16={'loss': 0.5499252676963806, 'accuracy': 0.7064718008041382, 'precision': 0.9801802039146423, 'recall': 0.44012945890426636, 'f1-score': 0.6074814391964187, 'f2-score': 0.494635285195403}
    data_512_8={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_64={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_32={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_16={'loss': 0.6953974366188049, 'accuracy': 0.48726513981819153, 'precision': 1.0, 'recall': 0.006472492124885321, 'f1-score': 0.012861723980868045, 'f2-score': 0.008077542678876618}
    data_1024_8={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    

    fig, axes = plt.subplots(4)
    axes[0].plot(data_axis,[data_128_64['loss'],data_256_32['loss'], data_256_16['loss'],data_256_8['loss']],"black",label="loss")
    axes[0].plot(data_axis,[data_128_64['accuracy'],data_256_32['accuracy'], data_256_16['accuracy'],data_256_8['accuracy']],"red", label="accuracy")
    axes[0].plot(data_axis,[data_128_64['precision'],data_256_32['precision'], data_256_16['precision'],data_256_8['precision']],"green",label="precision")
    axes[0].plot(data_axis,[data_128_64['recall'],data_256_32['recall'], data_256_16['recall'],data_256_8['recall']],"purple", label="recall")
    axes[0].plot(data_axis,[data_128_64['f1-score'],data_256_32['f1-score'], data_256_16['f1-score'],data_256_8['f1-score']],"blue", label="F1-Score")
    axes[0].plot(data_axis,[data_128_64['f2-score'],data_256_32['f2-score'], data_256_16['f2-score'],data_256_8['f2-score']],"pink", label="F2-Score")
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
        
    data_256_64={'loss': 0.4865851104259491, 'accuracy': 0.7970772385597229, 'precision': 0.9606879353523254, 'recall': 0.6326860785484314, 'f1-score': 0.7629263384002197, 'f2-score': 0.6790550680934032}
    data_256_32={'loss': 0.4831761121749878, 'accuracy': 0.7649269104003906, 'precision': 0.9693166017532349, 'recall': 0.5622977614402771, 'f1-score': 0.7117251085237083, 'f2-score': 0.6138490309430898}
    data_256_16={'loss': 0.6931905746459961, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_256_8={'loss': 0.4669460654258728, 'accuracy': 0.8041753768920898, 'precision': 0.9246954321861267, 'recall': 0.6755663156509399, 'f1-score': 0.780738146989396, 'f2-score': 0.7140411977658843}
    data_512_64={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_512_32={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_512_16={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_512_8={'loss': 0.5362588763237, 'accuracy': 0.7139874696731567, 'precision': 0.9791304469108582, 'recall': 0.45550161600112915, 'f1-score': 0.6217555030253265, 'f2-score': 0.5100560514621298}
    data_1024_64={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_32={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_16={'loss': 0.6931906342506409, 'accuracy': 0.48392483592033386, 'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'f2-score': 0.0}
    data_1024_8={'loss': 0.5327364206314087, 'accuracy': 0.7419624328613281, 'precision': 0.6751700639724731, 'recall': 0.9635922312736511, 'f1-score': 0.7939995120951229, 'f2-score': 0.8877457301038132}
    



    fig, axes = plt.subplots(4)
    axes[0].plot(data_axis,[data_128_64['loss'],data_256_32['loss'], data_256_16['loss'],data_256_8['loss']],"black",label="loss")
    axes[0].plot(data_axis,[data_128_64['accuracy'],data_256_32['accuracy'], data_256_16['accuracy'],data_256_8['accuracy']],"red", label="accuracy")
    axes[0].plot(data_axis,[data_128_64['precision'],data_256_32['precision'], data_256_16['precision'],data_256_8['precision']],"green",label="precision")
    axes[0].plot(data_axis,[data_128_64['recall'],data_256_32['recall'], data_256_16['recall'],data_256_8['recall']],"purple", label="recall")
    axes[0].plot(data_axis,[data_128_64['f1-score'],data_256_32['f1-score'], data_256_16['f1-score'],data_256_8['f1-score']],"blue", label="F1-Score")
    axes[0].plot(data_axis,[data_128_64['f2-score'],data_256_32['f2-score'], data_256_16['f2-score'],data_256_8['f2-score']],"pink", label="F2-Score")
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



plot_services()
