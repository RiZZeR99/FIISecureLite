import threading
import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

print(tf.__version__)

def train_model(first_layer_nodes, last_layer_nodes, path, path_to_save, classification_column):

    # print("[{}] importing data".format(path))
    dataset = pd.read_csv(path)
    # dataset=dataset.sample(frac=1)
    columns_names = dataset.columns
    string_results = "Test results with {} nodes first layer and {} nodes last layer (expect the layer with sigmoid function):\n".format(
        first_layer_nodes, last_layer_nodes)

    epsilon = 10**-6

    # dataset.dropna() # remove line by default which don't contains data
    data = dataset.drop(classification_column, axis=1)

    classifications = dataset[classification_column]

    data_train, data_test, results_train, results_test = train_test_split(
        data, classifications, test_size=0.2, random_state=46)

    tf.random.set_seed(46)

    # print("[{}] Creating and training model".format(path))

    # model = tf.keras.Sequential([
    #     tf.keras.layers.Dense(256, activation='relu',
    #                           input_dim=len(columns_names)-1),
    #     tf.keras.layers.Dense(128, activation='relu'),
    #     tf.keras.layers.Dense(64, activation='relu'),
    #     tf.keras.layers.Dense(32, activation='relu'),
    #     tf.keras.layers.Dense(1, activation='sigmoid')
    # ])

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(first_layer_nodes, activation='relu',
                                    input_dim=len(columns_names)-1))
    back_up_first_layer_nodes = first_layer_nodes
    first_layer_nodes //= 2
    while first_layer_nodes != last_layer_nodes//2:
        model.add(tf.keras.layers.Dense(first_layer_nodes, activation='relu'))
        first_layer_nodes //= 2
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.compile(
        loss=tf.keras.losses.binary_crossentropy,
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.03),
        metrics=[
            tf.keras.metrics.BinaryAccuracy(name='accuracy'),
            tf.keras.metrics.Precision(name='precision'),
            tf.keras.metrics.Recall(name='recall')
        ]
    )
    # training
    history = model.fit(data_train, results_train, epochs=50)

    map_history = {
        'loss': history.history['loss'],
        'accuracy': history.history['accuracy'],
        'precision': history.history['precision'],
        'recall': history.history['recall']
    }

    # print(str(map_history))

    model.summary()
    # print("///////////////////////////////////////////////")

    # print("[{}] Evaluating model".format(path))
    evaluations_results = model.evaluate(data_test, results_test)

    map_evaluation = {'loss': evaluations_results[0], 'accuracy': evaluations_results[1],
                      'precision': evaluations_results[2], 'recall': evaluations_results[3]}

    # f-beta = (1+Beta^2)(precision*recal)/((Beta^2*precision)+recall)
    map_evaluation['f1-score'] = 2*(map_evaluation['precision']*map_evaluation['recall'])/(
        map_evaluation['precision'] + map_evaluation['recall'] + epsilon)

    map_evaluation['f2-score'] = 5*(map_evaluation['precision']*map_evaluation['recall'])/(
        (4*map_evaluation['precision']) + map_evaluation['recall'] + epsilon)

    # print("Evaluation for {}:\n {}".format(
    #     path, str(map_evaluation)))

    string_results += "data_{}_{}=".format(
        back_up_first_layer_nodes, last_layer_nodes)+str(map_evaluation) + "\n"

    # first prediction try
    # first_dataset_instance = np.array(
    #     [[dataset[column][0] for column in columns_names if column != "class"]])  # this is a 1

    # last_dataset_instance = np.array(
    #     [[dataset[column][len(dataset)-1] for column in columns_names if column != "class"]])  # this is a 1

    # clear_instance_to_test = np.array(
    #     [[0 for i in range(0, len(columns_names)-1)]])

    # print(model.predict(first_dataset_instance))

    # print(model.predict(last_dataset_instance))

    # print(model.predict(clear_instance_to_test))

    # uncomment to save the model
    # depending on the results of the compute, we may need to save a model

    model.save(path_to_save)

    # convert with tflite_convert --saved_model_dir .\directory_model --output_file .\name.tflite
    # print(string_results)

    save_path=path_to_save.split("_")[0] + path_to_save.split("_")[1] 

    with open(save_path+".txt", "a") as f:
        f.write(string_results)


def compute_training_results(dataset, path_to_save, classification_column):

    train_model(128, 64, dataset,
                path_to_save + "_" + str(128) + "_" + str(64), classification_column)
    train_model(128, 32, dataset,
                path_to_save + "_" + str(128) + "_" + str(32), classification_column)
    train_model(128, 16, dataset,
                path_to_save + "_" + str(128) + "_" + str(16), classification_column)
    train_model(128, 8, dataset,
                path_to_save + "_" + str(128) + "_" + str(8), classification_column)

    train_model(256, 64, dataset,
                path_to_save + "_" + str(256) + "_" + str(64), classification_column)
    train_model(256, 32, dataset,
                path_to_save + "_" + str(256) + "_" + str(32), classification_column)
    train_model(256, 16, dataset,
                path_to_save + "_" + str(256) + "_" + str(16), classification_column)
    train_model(256, 8, dataset, 
                path_to_save + "_" + str(256) + "_" + str(8), classification_column)

    train_model(512, 64, dataset,
                path_to_save + "_" + str(512) + "_" + str(64), classification_column)
    train_model(512, 32, dataset,
                path_to_save + "_" + str(512) + "_" + str(32), classification_column)
    train_model(512, 16, dataset,
                path_to_save + "_" + str(512) + "_" + str(16), classification_column)
    train_model(512, 8, dataset, 
                path_to_save + "_" + str(512) + "_" + str(38), classification_column)

    train_model(1024, 64, dataset,
                path_to_save + "_" + str(1024) + "_" + str(64), classification_column)
    train_model(1024, 32, dataset,
                path_to_save + "_" + str(1024) + "_" + str(32), classification_column)
    train_model(1024, 16, dataset,
                path_to_save + "_" + str(1024) + "_" + str(16), classification_column)
    train_model(1024, 8, dataset,
                path_to_save + "_" + str(1024) + "_" + str(8), classification_column)


threading.Thread(target=compute_training_results, args=(
    "Permissions Dataset.csv", "Model_Permissions", 'class',)).start()
threading.Thread(target=compute_training_results, args=(
    "Receivers Dataset.csv", "Model_Receivers", 'class',)).start()
threading.Thread(target=compute_training_results, args=(
    "Services Dataset.csv", "Model_Services", 'class',)).start()


# threading.Thread(target=train_model,args=(256,32,"Permissions Dataset.csv",
#             "Model_Permissions","class")).start()  # learning rate 0.02 cu shuffle


# threading.Thread(target=train_model, args=(512, 16, "Receivers Dataset.csv",
#             "Model_Receivers", "class")).start() # learning rate 0.03 fara shuffle


# threading.Thread(target=train_model,args=(512, 8, "Services Dataset.csv",
#             "Model_Services", "class")).start() # learning rate 0.03 fara shuffle
