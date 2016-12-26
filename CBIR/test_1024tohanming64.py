#coding=utf-8


def data_1024t064(data):
    from keras.models import model_from_json
    from keras import backend as K
    #加载模型数据和weights
    json_file = open('model_1024to64.json', 'rb')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model_1024to64_weights.h5")
    f = K.function([loaded_model.layers[0].input, K.learning_phase()], [loaded_model.layers[0].output])
    output = f([data, 0])
    # output = loaded_model.predict(data, batch_size=1, verbose=0)
    return output[0][0]  #返回64维的数据array


def Feature_1024toFeature_64(feature_1024):
    data = data_1024t064(feature_1024)
    data[data < 0.5] = 0
    data[data >= 0.5] = 1
    data = map(int, data)
    data = map(str, data)
    data = ''.join(data)
    return [data]
